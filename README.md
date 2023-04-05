# buildpacks-demo

# Run server on the host
    uvicorn --reload --host 0.0.0.0 'main:app'
    curl -s localhost:8000 | jq .

# Build an OCI image
    pack build --builder gcr.io/buildpacks/builder buildpacks-demo

# Run server in container created from the OCI image
    docker run -p 8000:8000 buildpacks-demo

# Publish image to Docker Registry
    docker login
    pack build --builder gcr.io/buildpacks/builder --publish docker.io/argoniton/buildpacks-demo

# Rebase (update run image)
    pack rebase buildpacks-demo
    pack rebase --publish docker.io/argoniton/buildpacks-demo
