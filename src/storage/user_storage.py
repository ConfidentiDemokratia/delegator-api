from typing import List

from loguru import logger


class UserStorage:

    def __init__(self):
        self.address_to_embedding = {}

    def save_embedding(self, address: str, embedding: List[int]):
        logger.info(f"saving embedding: {embedding} for address: {address}")
        self.address_to_embedding[address] = embedding

    def get_embedding(self, address: str) -> List[float]:
        logger.info(f"retrieving embedding for address: {address}")
        return self.address_to_embedding.get(address, [0.0] * 384)
