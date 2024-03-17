import json
from typing import List

import torch
from loguru import logger

# from zk.process_model import process_model


class Predictor:

    def __init__(self, model):
        logger.info("Initialize model")
        self.model = model
        self.model.eval()

    def predict(
        self,
        user_embedding: List[float],
        proposal_embedding: List[float]
    ) -> int:
        logger.info("Perform predict")
        user_emb = torch.tensor(user_embedding).float()
        proposal_emb = torch.tensor(proposal_embedding).float()
        model_input = torch.cat((user_emb, proposal_emb)).unsqueeze(0)
        with torch.no_grad():
            prediction = int(self.model(model_input).item())
        # return prediction
        return {
            "prediction": prediction,
            "proof": generate_proof(user_embedding + proposal_embedding)
        }

    def get_proof(self, input: List[float]):
        onnx_input = dict(
            input_data=[input]
        )
        json.dump(onnx_input, open("onnx_input.json", "w"))
        proof = process_model(
            "./models/model.onnx",
            "onnx_input.json"
        )
        return proof
