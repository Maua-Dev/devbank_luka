from enum import Enum

class ItemTypeEnum(Enum):
    TOY="TOY"
    FOOD="FOOD"
    CLOTHES="CLOTHES"
    GAMES="GAMES"

class tipotransacao(Enum):
    saque = "saque"
    deposito = "deposito"