import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class test_deposito:
    def test_deposit(self):
        deposit = deposito(500.0, 1000.0, 2025051123.4537)
        assert deposit.valor_do_deposito == 500.0
        assert deposit.current_balance == 1000.0
        assert deposit.timestamp == 2025051123.4537

    def test_valor_do_deposito_is_None(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito="", current_balance=1000.0 , timestamp=2025051123.4537)
    
    def test_valor_do_deposito_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito= "abc", current_balance=1000.0 , timestamp=2025051123.4537)

    def test_valor_do_deposito_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=-10.0, current_balance=1000.0 , timestamp=2025051123.4537)

    def test_valor_do_deposito_is_two_times_current_balance(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=2000.0, current_balance=1000.0 , timestamp=2025051123.4537)



    def test_current_balance_is_None(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance="" , timestamp=2025051123.4537)

    def test_current_balance_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance="abc" , timestamp=2025051123.4537)

    def test_current_balance_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance=-10.0 , timestamp=2025051123.4537)

    

    def test_timestamp_is_None(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance=1000.0 , timestamp="")
    
    def test_timestamp_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance=1000.0 , timestamp="abc")

    def test_timestamp_is_zero(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance=1000.0 , timestamp=0000000000.0000)
    
    def test_timestamp_length_is_under_fourteen(self)
    with pytest.raises(ParamNotValidated):
        deposito(valor_do_deposito=500.0, current_balance=1000.0 , timestamp=2025051123.453)