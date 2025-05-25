from typing import Tuple
from ..errors.entity_errors import ParamNotValidated

class usuario:
    name: str
    agency: str
    account: str
    current_balance: float

    def __init__(self, name: str=None, agency: str=None, account: str=None, current_balance: float=None)
    validation_name = self.validate_name(name)
        if validation_name[0] is False:
            raise ParamNotValidated("name", validation_name[1])
    self.name = name

    validation_agency = self.validate_agency(agency)
        if validation_agency[0] is False:
            raise ParamNotValidated("agency", validation_agency[1])
    self.agency = agency

    validation_account = self.validate_account(account)
        if validation_account[0] is False:
            raise ParamNotValidated("account", validation_account[1])
    self.account = account

    validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
    self.current_balance = current_balance

    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
        if name is None:
            return (False, "Name is required")
        if type(name) != str:
            return (False, "Name must be a string")
        if len(name) < 12:
            return (False, "Username must have at least twelve digits")
        return (True, "")

    @staticmethod
    def validate_agency(agency: str) -> Tuple[bool, str]:
        if agency is None:
            return (False, "Agency is required")
        if type(agency) != str:
            return (False, "Agency must be a string")
        if len(agency) != 4:
            return (False, "Agency number must have only four digits")
        return (True, "")

    @staticmethod
    def validate_account(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Account number is required")
        if type(account) != str:
            return (False, "Account number must be a string")
        if len(account) < 7:
            return (False, "Account number must have at least 7 digits")
        return (True, "")

    @staticmethod
    def validate_current_balance(account: str) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Account number is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float number")
        if current_balance < 0:
            return (False, "Current balance can not be negative")
        return (True, "")

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
        #retorna um dicionário com as chaves e seus respectivos valores depois das validações pelos métodos acima.
    
    def __eq__(self.other)
        return self.name == other.name, self.agency == other.agency, self.account == other.account, self.current_balance == other.current_balance
        #verifica/compara se o objeto instanciado possui a mesma classe que o objeto moldado na classe, ou seja, se "other" também é "usuário".
    
    def __repr__(self):
        return (f"usuario({name = self.name}, "
                f"{agency = self.agency}, "
                f"{account = self.account}, "
                f"{current_balance = self.current_balance}")")
        #serve para fazer uma representação inequívoca do objeto no formato string, trazendo detalhes do objeto para o desenvolvedor.
        #é diferente do __str__ que foca na representação do objeto no formato string para o usuário.
        #!estudar mais!