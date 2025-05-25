from typing import Tuple
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import tipotransacao

class transacao:
    type: tipotransacao
    value: float
    current_balance: float 
    timestamp: float 

    def __init__(self, type: tipotransacao=None, valor: float=None, current_balance: float=None, timestamp: float=None)

    validation_type = self.validate_type(type)
    if validation_type[0] is False:
        raise ParamNotValidated("type", validation_type[1])
    self.type = type

    validation_value = self.validate_value(value)
    if validation_value[0] is False:
        raise ParamNotValidated("value", validation_value[1])
    self.value = value

    validation_current_balance = self.current_balance(current_balance)
    if validation_current_balance[0] is False:
        raise ParamNotValidated("current_balance", validation_current_balance[1])
    self.current_balance = current_balance

    validation_timestamp = self.validate_timestamp(timestamp)
    if validation_timestamp[0] is False:
        raise ParamNotValidated("timestamp", validation_timestamp[1])
    self.timestamp = timestamp


    @staticmethod
    def validate_type(type: tipotransacao) -> Tuple[bool, str]:
        if type is None:
            return (False, "Transaction must have a type")
        if type(type) is not tipotransacao:
            return (False, "Transaction type must either be a withdraw or a deposit")
        return (True, "")

    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]
        if value is None:
            return (False, "Value must exist")
        if type(value) is not float:
            return (False, "Transaction value must be a float number")
        if value < 0
            return (False, "Transaction value must be above zero")
        if value > current_balance:
            return (False, "Insufficient balance for transaction")
        return (True, "")

    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]
        if current_balance is None:
            return (False, "Current balance must exist")
        if type(current_balance) is not float:
            return (False, "Current balance must be a float number")
        if current balance < 0:
            return (False, "Current balance can not be under zero") 
        return (True, "")

    @staticmethod
    def validate_timestamp(timestamp: float) -> Tuple[bool, str]
        if timestamp is None:
            return (False, "Timestamp must exist")
        if type(timestamp) is not float:
            return (False, "Timestamp must be a float number")
        if timestamp < 0:
            return (False, "Timestamp must be a positive number")
        return (True, "")

    def to_dict(self): 
        return {
        "type": self.type,
        "value": self.value,
        "current_balance": self.current_balance,
        "timestamp": self.timestamp
    }
    #retorna um dicionário com as chaves e seus respectivos valores depois de serem validados pelos métodos acima.

    def __eq__(self.other):
        return (self.type == other.type,
        self.value == other.value,
        self.current_balance == other.current_balance,
        self.timestamp == other.timestamp)
    #verifica/compara se o objeto instanciado possui a mesma classe que o objeto moldado na classe, ou seja, se "other" também é "transacao".

    def __repr__(self):
        return (f"transacao({type = self.type}, "
                f"{value = self.value}, "
                f"{current_balance = self.current_balance}, "
                f"{timestamp = self.timestamp}")")
    #serve para fazer uma representação inequívoca do objeto no formato string, trazendo detalhamento do objeto para o desenvolvedor.
    #é diferente do __str__ que foca na representação amigável do objeto no formato string para o usuário.
    #!procurar entender melhor!