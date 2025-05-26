from typing import Dict, Optional, List
from ..entities.usuario import usuario
from .usuario_repository_interface import IUsuarioRepository


class UsuarioRepositoryMock(IUsuarioRepository):
    users: Dict[int, usuario]
    
    def __init__(self):
        self.users = {
            1: usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance=1000.0),
        }
        
    def get_all_users(self) -> List[usuario]:
        return self.users.values()
    
    def get_user(self, user_id: int) -> Optional[usuario]:
        return self.users.get(user_id, None)
    
    def post_user(self, user: usuario, user_id: int) -> usuario:
        
        self.users[user_id] = user
        return user
    
    def delete_user(self, user_id: int) -> usuario:
        user = self.users.pop(user_id, None)
        return user
        
        
    def update_user(self, user_id:int, name:str=None, agency:str=None, account:str=None, current_balance:float=None) -> usuario:
        user = self.users.get(user_id, None)
        if user is None:
            return None
        
        if name is not None:
            user.name = name
        if agency is not None:
            user.agency = agency
        if account is not None:
            user.account = account
        if current_balance is not None:
            user.current_balance = current_balance
        self.users[user_id] = user
        
        return user
        
    
    