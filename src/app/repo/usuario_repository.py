import requests
from ..entities.usuario import usuario

def get_user():
    response = requests.get("https://r2tcz6zsokynb72jb6o4ffd5nm0ryfyz.lambda-url.us-west-2.on.aws", name, agency, account, current_balance)
print(response)
#mostra o código de status da requisição get.
print(response.json())
#imprime o valor armazenado na response.

#CHAMAR A FUNÇÃO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!