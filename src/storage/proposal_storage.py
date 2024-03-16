from typing import List

from loguru import logger


class ProposalStorage:

    def __init__(self):
        self.proposal_id_to_embedding = {}

    def save_embedding(self, proposal_id: int, embedding: List[int]):
        logger.info(
            f"saving embedding: {embedding} for proposal id: {proposal_id}"
        )
        self.proposal_id_to_embedding[proposal_id] = embedding
        logger.info("saved proposal")

    def get_embedding(self, proposal_id: int) -> List[float]:
        logger.info(f"retrieving embedding for id: {proposal_id}")
        return self.proposal_id_to_embedding.get(proposal_id, [0.0] * 384)
