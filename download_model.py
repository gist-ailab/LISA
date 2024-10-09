from huggingface_hub import hf_hub_download

# Model repository
repo_id = "xinlai/LISA-7B-v1"

# Download the files
config_path = hf_hub_download(repo_id=repo_id, filename="config.json")
model_path = hf_hub_download(repo_id=repo_id, filename="pytorch_model.bin")
tokenizer_path = hf_hub_download(repo_id=repo_id, filename="tokenizer_config.json")
tokenizer_model_path = hf_hub_download(repo_id=repo_id, filename="tokenizer.model")

print("Files downloaded:")
print(f"Config: {config_path}")
print(f"Model: {model_path}")
print(f"Tokenizer config: {tokenizer_path}")
print(f"Tokenizer model: {tokenizer_model_path}")
