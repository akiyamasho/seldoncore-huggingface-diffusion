FROM --platform=linux/amd64 python:3.9-slim
WORKDIR /app

# Install python packages
COPY setup.py setup.py
RUN pip install .

# Copy source code
COPY . .

# Port for GRPC
EXPOSE 5000
# Port for REST
EXPOSE 9000

# Define environment variables
ENV MODEL_NAME StableDiffusionModel
ENV SERVICE_TYPE MODEL

# Changing folder to default user
RUN chown -R 8888 /app

# HuggingFace
RUN mkdir /.cache
RUN chown -R 8888 /.cache

CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE
