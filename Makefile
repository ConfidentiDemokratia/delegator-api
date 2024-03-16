IMAGE_NAME=multivac_ml_image
CONTAINER_NAME=multivac_ml
PORT=80

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
build-run:
	docker build -t $(IMAGE_NAME) . && \
	docker run --rm -it --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

run:
	docker run --rm -it --name --name $(CONTAINER_NAME) -p $(PORT):$(PORT) $(IMAGE_NAME)

# Stop and remove the Docker container
kill:
	docker kill $(CONTAINER_NAME) && \
	docker rm $(CONTAINER_NAME)
