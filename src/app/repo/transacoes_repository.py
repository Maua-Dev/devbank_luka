import requests
from ..entities.transacoes import transacao
from ..enums.item_type_enum import tipotransacao

def get_history():
    response1 = requests.get("https://r2tcz6zsokynb72jb6o4ffd5nm0ryfyz.lambda-url.us-west-2.on.aws/history", type, value, current_balance, timestamp)
print(response1)
#mostra o código de status da requisição get.
print(response1.json())
#imprime o valor armazenado na response1.

informacoes = '{"type":tipotransacao, "value":value, "current_balance":current_balance, "timestamp":timestamp}'
def post_transaction():
    response2 = requests.post("https://r2tcz6zsokynb72jb6o4ffd5nm0ryfyz.lambda-url.us-west-2.on.aws/history", informacoes)
print(response2)
#mostra o código de status da requisição post.
print(response2.json())
#imprime o valor armazenado na response2.

#CHAMAR AS FUNÇÕES!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Excluir deposito e saque já que agora tem o file transacoes????????????