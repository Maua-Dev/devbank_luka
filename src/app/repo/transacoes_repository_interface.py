from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import tipotransacao

from ..entities.transacoes import transacao


class ITransacaoRepository(ABC):
    
    
    @abstractmethod
    def get_all_transactions(self) -> List[transacao]:
        '''
        Returns all the transactions in the database 
        '''
        pass
    
    @abstractmethod
    def get_transaction(self, transaction_id: int) -> Optional[transacao]:
        '''
        Returns the transaction with the given id.
        If the transaction does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def post_transaction(self, transaction: transacao, transaction_id: int) -> transacao:
        '''
        Creates a new transaction in the database
        '''
        pass
    
    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> transacao:
        '''
        Deletes the transaction with the given id.
        If the transaction does not exist, returns None
        '''
        
    @abstractmethod
    def update_transaction(self, transaction_id:int, type:tipotransacao=None, value:float=None, current_balance:float=None, timestamp:float=None) -> transacao:
        '''
        Updates the transaction with the given id.
        If the transaction does not exist, returns None.
        I put the update transaction just for precaution, I'm not sure if it is needed for this project.
        '''
        pass
    
    