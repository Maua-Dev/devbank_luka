from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum

class deposito:
    valor_do_deposito: float
    current_balance: float
    timestamp: float

    def __init__(self, valor_do_deposito: float=None, current_balance: float=1000.0, timestamp: float=None)
        validation_valor_do_deposito = self.validate_valor_do_deposito(valor_do_deposito)
        if validation_valor_do_deposito[0] is False:
            raise ParamNotValidated("valor_do_deposito", validation_valor_do_deposito[1])
        self.valor_do_deposito = valor_do_deposito
    
        validation_current_balance = self.validate_current_balance(current_balance)
        if validation_current_balance[0] is False:
            raise ParamNotValidated("current_balance", validation_current_balance[1])
        self.current_balance = current_balance

        validation_timestamp = self.validate_timestamp(timestamp)
        if validation_timestamp[0] is False:
            raise ParamNotValidated("timestamp", validation_timestamp[1])
        self.timestamp = timestamp

    @staticmethod
    def validate_valor_do_deposito(valor_do_deposito: float) -> Tuple[bool, str]
        if valor_do_deposito is None:
            return (False, "Deposit value is required")
        if type(valor_do_deposito) != float:
            return (False, "Deposit must be a float number")
        if valor_do_deposito < 0:
            return (False, "Can not deposit a value under zero")
        if valor_do_deposito = 2*current_balance:
            return (False, "Suspicious deposit")
        return (True, "")

    @app.post("/deposit")
    async def read_root(response: Response):
        if valor_do_deposito = 2*current_balance:
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