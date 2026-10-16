from deep_translator import GoogleTranslator
import requests

texto = input("Texto em inglês: ")

traducao = GoogleTranslator(
    source='en',
    target='pt'
).translate(texto)

print("Tradução:", traducao)