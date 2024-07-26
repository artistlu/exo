import requests
import os
from pathlib import Path

def get_model(model_name: str, local_cache_dir: Path):
    registry_url = "http://localhost:8081/models"
    local_file_server = "http://localhost:8082/"

    # Check if model is in local registry
    response = requests.get(f"{registry_url}/{model_name}")
    if response.status_code == 200:
        # Model is available locally
        model_url = f"{local_file_server}/{model_name}"

        print("==================good job ====================\n", model_url)
    else:
        # Model not available locally, use Hugging Face
        model_url = f"https://huggingface.co/{model_name}/resolve/main/model.safetensors"

    # Download the model
    response = requests.get(model_url, stream=True)
    model_path = local_cache_dir / f"{model_name}.safetensors"
    with open(model_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    # If downloaded from Hugging Face, update registry and copy to file server
    if "huggingface.co" in model_url:
        requests.post(f"{registry_url}/{model_name}", json={"path": str(model_path)})
        copy_to_file_server(model_path, model_name)

    return model_path

def copy_to_file_server(model_path: Path, model_name: str):
    # Implementation depends on your file server setup
    # This could be a file copy, an HTTP POST, or any other method to transfer the file
    pass