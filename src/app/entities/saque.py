from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

class saque:
    valor_do_saque: float
    current_balance: float
    timestamp: float

    def __init__(self, valor_do_saque: float=None, current_balance: float=1000.0, timestamp: float=None)
    validation_valor_do_saque = self.validate_valor_do_saque(valor_do_saque)
    if validation_valor_do_saque[0] is False:
        raise ParamNotValidated("valor_do_saque", validation_valor_do_saque[1])
    self.valor_do_saque = valor_do_saque

    validation_current_balance = self.validate_current_balance(current_balance)
    if validation_current_balance[0] is False:
        raise ParamNotValidated("current_balance", validation_current_balance[1])
    self.current_balance = current_balance

    validation_timestamp = self.validate_timestamp(timestamp)
    if validation_timestamp[0] is False:
        raise ParamNotValidated("timestamp", validation_timestamp[1])
    self.timestamp = timestamp


    @staticmethod
    def validate_valor_do_saque(valor_do_saque: float) -> Tuple[bool, str]
        if valor_do_saque is None:
            return (False, "Withdraw value is required")
        if type(valor_do_saque) != float:
            return (False, "Withdraw must be a float number")
        if valor_do_saque < 0:
            return (False, "Can not withdraw a value under zero")
        if valor_do_saque > current_balance:
            return (False, "Insufficient balance for transaction")
        return (True, "")

    @app.post("/withdraw")
    async def read_root(response: Response)
        if valor_do_saque > current_balance:
            return response.status_code = status.HTTP_403_Forbidden

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
        if current_balance is None:
            return (False, "Current balance is required")
        if type(current_balance) != float:
            return (False, "Current balance must be a float number")
        if current_balance < 0:
            return (False, "Current balance can not be negative")
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]
        if timestamp is None:
            return (False, "timestamp is required")
        if type(timestamp) != float:
            return (False, "timestamp must be a float number")
        if timestamp <= 0:
            return (False, "timestamp must be above zero")
        if len(timestamp) < 14:
            return (False, "timestamp must have at least fourteen digits")
        return (True, "")

    def to_dict(self):
        return {
            "valor_do_saque": self.valor_do_saque,
            "current_balance": self.current_balance,
            "timestamp": self.timestamp
        }
        #retorna um dicionário com as chaves e seus respectivos valores depois de serem validados pelos métodos acima.

    def __eq__(self.other)
        return self.valor_do_saque == other.valor_do_saque, self.current_balance == other.current_balance, self.timestamp == other.timestamp
        #verifica se o objeto em questão possui a mesma classe do objeto instanciado (self), ou seja, a classe "saque".

    def __repr__(self):
        return (f"saque({valor_do_saque = self.valor_do_saque}, "
                f"{current_balance = self.current_balance}, "
                f"{timestamp = self.timestamp}")")