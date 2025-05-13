import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class test_historico:
    def test_history(self):
        history = historico("deposito", 500.0, 1000.0, 2025051123.4537)
        assert history.type == "deposito"
        assert history.value == 500.0
        assert history.current_balance == 1000.0
        assert history.timestamp == 2025051123.4537

    def test_historico_is_None(self)
    with pytest.raises(ParamNotValidated):
        historico(type="", value=500.0, current_balance=1000.0 , timestamp=2025051123.4537)

    def test_historico_is_not_deposito_nor_saque(self)
    with pytest.raises(ParamNotValidated):
        historico(type="abc", value=500.0, current_balance=1000.0 , timestamp=2025051123.4537)

    def test_historico_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        historico(type=10, value=500.0, current_balance=1000.0 , timestamp=2025051123.4537)



    def test_value_is_None(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value="", current_balance=1000.0 , timestamp=2025051123.4537)

    def test_value_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value="abc", current_balance=1000.0 , timestamp=2025051123.4537)

    def test_value_is_zero_or_less(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value=-10.0, current_balance=1000.0 , timestamp=2025051123.4537)

    

    def test_current_balance_is_None(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value=500.0, current_balance="" , timestamp=2025051123.4537)

    def test_current_balance_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value=500.0, current_balance="abc" , timestamp=2025051123.4537)

    def test_current_balance_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
       historico(type="deposito", value=500.0, current_balance=-10.0 , timestamp=2025051123.4537)

    

    def test_timestamp_is_None(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value=500.0, current_balance=1000.0 , timestamp="")
    
    def test_timestamp_is_not_float(self)
    with pytest.raises(ParamNotValidated):
       historico(type="deposito", value=500.0, current_balance=1000.0 , timestamp="abc")

    def test_timestamp_is_zero(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value=500.0, current_balance=1000.0 , timestamp=0000000000.0000)
    
    def test_timestamp_length_is_under_fourteen(self)
    with pytest.raises(ParamNotValidated):
        historico(type="deposito", value=500.0, current_balance=1000.0 , timestamp=2025051123.453)