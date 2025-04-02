"""
Aplicação para rodar a predição a de uma Resnet-18
"""
import pandas as pd
import torch
from datasets import load_dataset
from transformers import AutoImageProcessor, AutoModelForImageClassification

if __name__ == '__main__':
    image_processor = AutoImageProcessor.from_pretrained(
        "microsoft/resnet-18")
    model = AutoModelForImageClassification.from_pretrained(
        "microsoft/resnet-18")
    dataset = load_dataset("microsoft/cats_vs_dogs")

    N_SAMPLES = 10

    # Selecionando algumas amostras
    dados_teste = dataset["train"][:N_SAMPLES]["image"]

    with torch.no_grad():
        inputs = image_processor(dados_teste, return_tensors="pt")
        outputs = model(**inputs)

    # Extraindo as predições
    preds = torch.argmax(outputs.logits, dim=1)
    print(preds)
