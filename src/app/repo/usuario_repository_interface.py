from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..entities.usuario import usuario


class IUsuarioRepository(ABC):
    
    
    @abstractmethod
    def get_all_users(self) -> List[usuario]:
        '''
        Returns all the users in the database 
        '''
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> Optional[usuario]:
        '''
        Returns the user with the given id.
        If the user does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def post_user(self, user: usuario, user_id: int) -> usuario:
        '''
        Creates a new user in the database
        '''
        pass
    
    @abstractmethod
    def delete_user(self, user_id: int) -> usuario:
        '''
        Deletes the user with the given id.
        If the user does not exist, returns None
        '''
        
    @abstractmethod
    def update_user(self, user_id:int, name:str=None, agency:str=None, account=str=None, current_balance=float=None) -> usuario:
        '''
        Updates the user with the given id.
        If the user does not exist, returns None
        '''
        pass
    
    