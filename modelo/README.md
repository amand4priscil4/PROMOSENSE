# Modelo Treinado

O modelo BERTimbau fine-tuned para análise de sentimento está disponível no Hugging Face:

🤗 **[Amand4priscil4/promosense-modelo](https://huggingface.co/Amand4priscil4/promosense-modelo)**

## Como baixar

```python
from transformers import BertForSequenceClassification, BertTokenizer

model = BertForSequenceClassification.from_pretrained('Amand4priscil4/promosense-modelo')
tokenizer = BertTokenizer.from_pretrained('neuralmind/bert-base-portuguese-cased')
```

## Informações

- **Base:** neuralmind/bert-base-portuguese-cased (BERTimbau)
- **Tarefa:** Classificação de sentimento (positivo, neutro, negativo)
- **Dados de treino:** 28.196 avaliações da Olist
- **Accuracy:** 86%
- **F1:** 0.851