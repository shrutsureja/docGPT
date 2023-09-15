import os 
import logging 

from huggingface_hub import hf_hub_download

""" 
models-id = "TheBloke/Llama-2-7b-Chat-GGUF"
model-basename = "llama-2-7b-chat.Q5_K_M.gguf"

"""

def download_model(destination_folder : str, model_id : str, model_basename : str):
    local_path = os.path.abspath(destination_folder)
    try:
        res = hf_hub_download(
            repo_id = model_id,
            filename = model_basename,
            local_dir = local_path,
            local_dir_use_symlinks=True,
        )
        logging.info(f"model : {model_id} : {model_basename} at {res}")
        logging.info(f"model: {model_id} : {model_basename} downloaded successfully")
    except:
        logging.INFO("Error in downloading the model")



if __name__ == "__main__":
    model_id = "TheBloke/Llama-2-7b-Chat-GGUF"
    model_basename = "llama-2-7b-chat.Q5_K_M.gguf"
    destination_folder = "models"
    download_model(destination_folder, model_id, model_basename)
    logging.info("Now you can run the gpt.py")