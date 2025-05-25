from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import ItemTypeEnum
from "./app/entities/deposito" import deposito
from "./app/entities/saque" import saque
from ..enums.item_type_enum import tipotransacao

class historico:
    type: tipotransacao
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, type: str=None, value: float=None, current_balance: float=1000.0, timestamp: float=None)
    validation_type = self.validate_type(type)
    if validation_type[0] is False:
        raise ParamNotValidated("type", validation_type[1])
    self.type = type

    validation_value = self.validation_value(value)
    if validation_value[0] is False:
        raise ParamNotValidated("value", validation_value[1])
    self.value = value

    validation_current_balance = self.validate_current_balance(current_balance)
    if validation_current_balance[0] is False:
        raise ParamNotValidated("current_balance", validation_current_balance[1])
    self.current_balance = current_balance

    validation_timestamp = self.validate_timestamp(timestamp)
    if validation_timestamp[0] is False:
        raise ParamNotValidated("timestamp", validation_timestamp[1])
    self.timestamp = timestamp

    @app.get("/deposit", "/withdraw")
    async def all_transactions(deposito, saque):
        if deposito and or saque is != None:
            return all_transactions

    @staticmethod
    def validate_type(type: str) -> Tuple[bool, str]
        if type is None:
            return (False, "Type is required")
        if type != tipotransacao:
            return (False, "Type must either be a deposit or a withdraw")
        if type(type) != str:
            return (False, "Type must be a string")
        return (True, "")


    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]
        if value is None:
            return (False, "Value is required")
        if type(value) != float:
            return  (False, "Value must be a float number")
        if value <= 0:
            return (False, "Value must be above zero")

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
