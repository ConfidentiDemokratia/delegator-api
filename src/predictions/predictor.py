from typing import List
from loguru import logger
import torch


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
        return prediction
