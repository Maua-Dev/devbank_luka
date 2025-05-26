import pytest
from src.app.errors.entity_errors import ParamNotValidated

class test_transacoes:
    def test_transactions(self):
        transaction = transacao("deposito", 500.0, 1000.0, 2025051123.4537)
        assert transaction.type == "deposito"
        assert transaction.value == 500.0
        assert transaction.current_balance == 1000.0
        assert transaction.timestamp == 2025051123.4537

    def test_type_is_None(self)
    with pytest.raises(ParamNotValidated):
        transacao(type=None, value=500.0, current_balance=1000.0 , timestamp=2025051123.4537)
    
    def test_type_is_not_tipotransacao(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="seila", value=500.0, current_balance=1000.0 , timestamp=2025051123.4537)



    def test_value_is_None(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", value=None, current_balance=1000.0 , timestamp=2025051123.4537)
    
    def test_value_is_not_float1(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", value= "abc", current_balance=1000.0 , timestamp=2025051123.4537)
    
    def test_value_is_not_float2(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", value= 10, current_balance=1000.0 , timestamp=2025051123.4537)

    def test_value_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", value=-10.0, current_balance=1000.0 , timestamp=2025051123.4537)

    def test_value_is_two_times_the_current_balance(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", value=2000.0, current_balance=1000.0 , timestamp=2025051123.4537)



    def test_current_balance_is_None(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=None , timestamp=2025051123.4537)

    def test_current_balance_is_not_float1(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance="abc" , timestamp=2025051123.4537)
    
    def test_current_balance_is_not_float2(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=10 , timestamp=2025051123.4537)

    def test_current_balance_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=-10.0 , timestamp=2025051123.4537)

    

    def test_timestamp_is_None(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=1000.0 , timestamp=None)
    
    def test_timestamp_is_not_float1(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=1000.0 , timestamp="abc")

    def test_timestamp_is_not_float2(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=1000.0 , timestamp=10)

    def test_timestamp_is_zero(self)
    with pytest.raises(ParamNotValidated):
        transacao(type="deposito", valor_do_deposito=500.0, current_balance=1000.0 , timestamp=0000000000.0000)