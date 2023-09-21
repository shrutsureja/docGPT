import os
from dataclasses import asdict, dataclass

from dotenv import load_dotenv
# from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from llama_cpp import Llama

template = """Question: {question}

Answer: Let's work this out in a step by step way to be sure we have the right answer."""

prompt = PromptTemplate(template=template, input_variables=["question"])

def load_model():
    try:
        # check if the model is already downloaded
        if os.path.exists(model_path):
            print("Loading model...")
            global llm
            llm = Llama(
                model_path=model_path,
                )
            return True
        else:
            raise ValueError(
                "Model not found. Please run `poetry run python download_model.py` to download the model."
            )
    except Exception as e:
        print(str(e))
        raise


if __name__ == "__main__":

    # generation_config = GenerationConfig(
    #     temperature=0.1,
    #     top_k=0,
    #     top_p=0.9,
    #     repetition_penalty=1.0,
    #     max_new_tokens=512,
    #     seed=42,
    #     reset=False,
    #     stream=True,  # streaming per word/token
    #     threads=int(os.cpu_count() / 2),  # adjust for your CPU
    #     stop=["<|im_end|>", "|<"],
    #     last_n_tokens=64,
    #     batch_size=8,
    # )

    # load model if it has already been downloaded. If not prompt the user to download it.
    load_model()

    while True:
        query = input("\nEnter a question: ")
        # query = "Question: " + query
        # if query == "Question: exit":ut
        input = """A chat between a curious human ("kunjan") and an artificial intelligence assistant ("3K"). The assistant gives helpful, detailed, and polite answers to the human's questions.my name is 3K.the problem statement name is harharmahadev.
                    kunjan: Hello, 3K.
                    3K: Hello. How may I help you today?
                    kunjan:"""
        if query == "exit":
            break
        if query.strip() == "":
            continue
        try:
            print("Thinking...")
            # call llm with formatted user prompt and generation config
            # response = llm(format_prompt(query), **apredict(generation_config))
            # llm_chain = LLMChain(prompt=prompt, llm=llm)
            llm_chain.run(input + query)
            # response = llm(query)
            # print response
            print("\n")
        except Exception as e:
            print(str(e))
            raise