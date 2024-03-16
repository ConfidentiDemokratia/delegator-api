## Introduction
This is multivac api which is responsible for making autonomous predictions, saving user and proposal embeddings

## Running
To run the the app do
```make build-run```
which makes and runs the docker image

## Endpoints
The API is accessible at `http://165.22.115.171:8080/`
- `/ping` - health check
- `/predict` - POST request to, make predictions recieves json of format
```{address: string}```
- `/save_user_embedding` - POST request tosave user embedding
```{address: String, user_embedding: List[int]}```
- `/save_proposal_embedding` - POST request tosave user embedding
```{address: String, proposal_embedding: List[int]}```

## Testing
Pinging the service
```curl -i http://165.22.115.171/```