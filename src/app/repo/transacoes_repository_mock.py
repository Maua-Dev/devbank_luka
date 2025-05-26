from typing import Dict, Optional, List

from ..enums.item_type_enum import tipotransacao
from ..entities.transacoes import transacao
from .transacoes_repository_interface import ITransacaoRepository

class ITransacoesRepository():
    transactions = Dict[int, transacao]

    def __init__(self):
        self.transactions = {
        1 : transacao(type=tipotransacao.deposito, value=1000.0, current_balance=1000.0, timestamp=1090421749)
        2 : transacao(type=tipotransacao.saque, value=1000.0, current_balance=1000.0, timestamp=1690262764)
        }

    def get_all_transactions(self) -> List[transacao]:
        return self.transactions.values()

    def get_transaction(self, transaction_id=int) -> Optional[transacao]:
        return self.transactions.get(transaction_id, None)
    
    def post_transaction(self, transaction_id=int) -> Optional[transacao]:
        self.transactions[transaction_id] = transaction
    return transaction

    def delete_transaction(self, transaction_id=int) -> Optional[transacao]:
        self.transactions.pop(transaction_id, None) = transaction
        return transaction
    
    def update_transaction(self, transaction_id) -> Optional[transacao]:
        self.transactions.get(transaction_id, None)
        if transaction is None:
            return None
        if type is deposito:
            transaction.deposito = deposito
        if type is saque:
            transaction.saque = saque
        if value is not None:
            transaction.value = value
        if current_balance is not None:
            transaction.current_balance = current_balance
        if timestamp is not None:
            transaction.timestamp = timestamp

        self.transactions[transaction_id] = transaction
        return transaction