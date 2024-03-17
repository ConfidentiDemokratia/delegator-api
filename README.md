## Introduction
This is the backend service facilitating autonomous voting through ZK ML. The service has the following components:
- predictions - handle modelling and predictions
- web3 - handles interactions with smart contracts through web3.py

## Running
To run the the app do
```make build-run```
which makes and runs the docker image

## Testing
Pinging the service
```curl -i http://localhost:80/```

## Endpoints
- `/ping` - health check
- `/predict` - POST request to, make predictions recieves json of format
```{address: string}```
- `/save_user_embedding` - POST request tosave user embedding
```{address: String, user_embedding: List[int]}```
- `/save_proposal_embedding` - POST request tosave user embedding
```{address: String, proposal_embedding: List[int]}```
`