import os

from dotenv import load_dotenv

from web3 import Web3
from web3.constants import ABI, CONTRACT_ADDRESS


class PredictionPublisher:

    PRIVATE_KEY = os.getenv('PRIVATE_KEY')
    PUBLIC_KEY = os.getenve("PUBLIC_KEY")
    WEB3_PROVIDER_URL = os.getenv('WEB3_PROVIDER_URL')

    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(this.WEB3_PROVIDER_URL))

    def submit_prediction(address, prediction, proof):
        contract = self.web3.eth.contract(address=contract_address, abi=abi)
        # Prepare transaction details
        transaction = contract.functions.submitAutoDelegatorVote(
            prediction,
            proof,
            address
        ).buildTransaction({
            'chainId': 1,
            'gas': 2000000,
            'gasPrice': web3.toWei('50', 'gwei'),
            'nonce': web3.eth.getTransactionCount(self.PUBLIC_KEY)
        })
        signed_tx = web3.eth.account.signTransaction(
            transaction,
            self.PRIVATE_KEY
        )
        # Send the transaction
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

        # Get transaction receipt (optional)
        receipt = web3.eth.waitForTransactionReceipt(tx_hash)