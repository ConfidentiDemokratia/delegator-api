import json
from typing import List

from flask import Flask, jsonify, request
from loguru import logger

from predictions.predictor import Predictor
from storage.proposal_storage import ProposalStorage
from storage.user_storage import UserStorage


import torch
import torch.nn as nn
import torch.nn.functional as F


PORT = 8080


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.fc1 = nn.Linear(768, 128)
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return torch.argmax(x, dim=1)


logger.info("Starting server application")
# Create a Flask application
app = Flask(__name__)

# initialise variables
MODEL_CONFIG_PT = "./configuration/config.json"
with open(MODEL_CONFIG_PT, 'r') as file:
    MODEL_CONFIG = json.load(file)
user_storage, proposal_storage = UserStorage(), ProposalStorage()
model = torch.load(MODEL_CONFIG["torch_model_pt"])
predictor = Predictor(model)


# get predictions
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"healthy": True}), 200


@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data (assumed to be JSON here)
    data = request.get_json(force=True)
    # validate input
    assert "address" in data.keys()
    assert "proposal_id" in data.keys()
    assert isinstance(data["address"], str)
    assert isinstance(data["proposal_id"], int)

    # get embeddings
    logger.info("make predictions")
    user_embedding = user_storage.get_embedding(data["address"])
    proposal_embedding = proposal_storage.get_embedding(data["proposal_id"])
    prediction = predictor.predict(user_embedding, proposal_embedding)
    try:
        return jsonify({'prediction': prediction}), 200
    except Exception as e:
        logger.error(f"Unable to predict: {e}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# save user embedding
@app.route('/save_user_embedding', methods=['POST'])
def save_user_embedding():
    # Get the request data (assumed to be JSON here)
    data = request.get_json(force=True)

    # validate input
    assert "address" in data.keys()
    assert "user_embedding" in data.keys()
    assert isinstance(data["address"], str)
    assert isinstance(data["user_embedding"], List[float])

    # save embedding
    logger.info("saving user embedding")
    try:
        user_storage.save_embedding(data["address"], data["user_embedding"])
        return jsonify({}), 201
    except Exception as e:
        logger.error(f"Unable to save user embedding: {e}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# save proposal embedding
@app.route('/save_proposal_embedding', methods=['POST'])
def save_proposal_embedding():
    # Get the request data (assumed to be JSON here)
    data = request.get_json(force=True)

    # validate input
    assert "proposal_id" in data.keys()
    assert "proposal_embedding" in data.keys()
    assert isinstance(data["address"], int)
    assert isinstance(data["user_embedding"], List[float])

    # save embedding
    logger.info("saving proposal embedding")
    try:
        proposal_storage.save_embedding(
            data["address"],
            data["user_embedding"]
        )
        return jsonify({}), 201
    except Exception as e:
        logger.error(f"Unable to save proposal embedding: {e}")
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
