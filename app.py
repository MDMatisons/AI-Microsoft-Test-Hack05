#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://eu-sn-openai-hack-05.openai.azure.com/"
openai.api_version = "2023-03-15-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  engine="hack01",
  messages = [{"role":"system","content":"You are a company internal customer support system whose primary goal is to help users with questions based on the documents provided to you. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to the company. Only provide answers from the provided data."}],
  temperature=0,
  max_tokens=800,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)
