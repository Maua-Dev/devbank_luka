import pytest
from src.app.entities.usuario import usuario
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
        usuario(name=None, agency="0000", account="00000-0", current_balance=1000.0)

    def test_name_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        usuario(name=10, agency="0000", account="00000-0", current_balance=1000.0)

    def test_name_length_is_under_twelve(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soll", agency="0000", account="00000-0", current_balance=1000.0)
    #verifica se o nome do usuário condiz com as regras impostas.



    def test_agency_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency=None, account="00000-0", current_balance=1000.0)

    def test_agency_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency=10, account="00000-0", current_balance=1000.0)

    def test_agency_length_is_under_four(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="000", account="00000-0", current_balance=1000.0)
    #verifica se a agência segue os padrões estabelecidos.



    def test_account_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account=None, current_balance=1000.0)

    def test_account_is_not_string(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account=10, current_balance=1000.0)

    def test_account_is_not_string2(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account=10.0, current_balance=1000.0)
    
    def test_account_length_is_under_seven(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-", current_balance=1000.0)
    #verifica se a conta obedece aos parâmetros exigidos.



    def test_current_balance_is_None(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance=None)

    def test_current_balance_is_not_float(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance="abc")

    def test_current_balance_is_not_float2(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance=10)

    def test_current_balance_is_under_zero(self)
    with pytest.raises(ParamNotValidated):
        usuario(name="Vitor Soller", agency="0000", account="00000-0", current_balance=-10)
    #verifica se o valor atual na conta está dentro dos parâmetros impostos.
    

    def test_usuario_to_dict(self)
    with pytest.raises(ParamNotValidated):
        a = usuario(name = "Vitor Soller", agency = "0000", account = "00000-0", current_balance = 1000.0)
        try a.to_dict() = {
            name = "Vitor Soller",
            agency = "0000",
            account = "00000-0",
            current_balance = 1000.0
        }
    #verifica se os dados podem ser dispostos como dicionário.
    #?poderia fazer try to_dict(a) ao invés de try a.to_dict()?
