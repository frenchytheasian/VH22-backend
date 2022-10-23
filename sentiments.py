import torch
from transformers import DistilBertForSequenceClassification, pipeline, DistilBertTokenizerFast

def predict(text):
    model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
    
    model.load_state_dict(torch.load("model.pt"))

    tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

    our_predicts = pipeline(model = model, tokenizer=tokenizer, task="text-classification")
    
    return our_predicts(text)