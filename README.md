# HuggingFace Diffusion Models on Seldon Core

### Requirements

-   [Helm](https://helm.sh/docs/intro/install/) (`helm`)
-   (for this README's example only) [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) ( `az` ) setup with your login credentials
    -   You can use `gcloud` or `aws` or even a local k8s cluster if you prefer

# Setup

### Cluster Setup (Azure Kubernetes Service example)

1. Setup the resource group and cluster name

    ```bash
    export RESOURCE_GROUP_NAME=<your resource group name of choice>
    export CLUSTER_NAME=<your cluster name of choice>
    ```

1. Create a new resource group and a new cluster

    ```bash
    az group create --name $RESOURCE_GROUP_NAME \
        --location eastus
    az aks create -g $RESOURCE_GROUP_NAME \
        -n $CLUSTER_NAME --enable-managed-identity \
        --node-count 1 \
        --enable-addons monitoring \
        --generate-ssh-keys
    ```

1. Get the cluster credentials

    ```bash
    az aks get-credentials --resource-group $RESOURCE_GROUP_NAME \
        --name $CLUSTER_NAME
    ```

### Seldon Core Setup

1. Install Seldon Core

```
kubectl create namespace seldon-system

helm install seldon-core seldon-core-operator \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --namespace seldon-system \
    --set istio.enabled=true
```

2. Create the model namespace

```
kubectl create namespace diffusion
```
