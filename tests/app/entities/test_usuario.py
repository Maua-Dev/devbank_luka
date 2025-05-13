import pytest
from src.app.entities.item import Item
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

class test_usuario:
    def test_user(self):
        user = usuario("Vitor Soller", "0000", "00000-0", 1000.0)
        assert user.name == "Vitor Soller"
        assert user.agency == "0000"
        assert user.account == "00000-0"
        assert user.current_balance == 1000.0
    
    def test_name_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="", agency="0000", account="00000-0", current_balance=1000.0)

    def test_name_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        usuario(name=10, agency="0000", account="00000-0", current_balance=1000.0)

    def test_name_length_is_under_twelve(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Solle", agency="0000", account="00000-0", current_balance=1000.0)



    def test_agency_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="", account="00000-0", current_balance=1000.0)

    def test_agency_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency=10, account="00000-0", current_balance=1000.0)

    def test_agency_length_is_under_four(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="000", account="00000-0", current_balance=1000.0)



    def test_account_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="", current_balance=1000.0)

    def test_account_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account=10, current_balance=1000.0)

    def test_account_length_is_under_seven(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-", current_balance=1000.0)



    def test_current_balance_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance="")

    def test_current_balance_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance="abc")

    def test_current_balance_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance=-10)