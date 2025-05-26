
from enum import Enum
import os

from .errors.environment_errors import EnvironmentNotFound

from .repo.item_repository_interface import IItemRepository
from .repo.usuario_repository_interface import IUsuarioRepository
from .repo.transacoes_repository_interface import ITransacaoRepository


class STAGE(Enum):
    DOTENV = "DOTENV"
    DEV = "DEV"
    PROD = "PROD"
    TEST = "TEST"


class Environments:
    """
    Defines the environment variables for the application. You should not instantiate this class directly. Please use Environments.get_envs() method instead.

    Usage:

    """
    stage: STAGE

    def _configure_local(self):
        from dotenv import load_dotenv
        load_dotenv()
        os.environ["STAGE"] = os.environ.get("STAGE") or STAGE.TEST.value

    def load_envs(self):
        if "STAGE" not in os.environ or os.environ["STAGE"] == STAGE.DOTENV.value:
            self._configure_local()

        self.stage = STAGE[os.environ.get("STAGE")]

    @staticmethod
    def get_item_repo() -> IItemRepository:
        if Environments.get_envs().stage == STAGE.TEST:
            from .repo.item_repository_mock import ItemRepositoryMock
            return ItemRepositoryMock
        # use "elif" conditional to add other stages
        else:
            raise EnvironmentNotFound("STAGE")
    
    @staticmethod
    def get_user_repo() -> IUsuarioRepository:
        if Enviroments.get_envs().stage == STAGE.TEST:
            from .repo.usuario_repository_mock import IUsuarioRepositoryMock
            return UsuarioRepositoryMock
        else:
            raise EnviromentNotFound("STAGE")
        
    @staticmethod
    def get_transaction_repo() -> ITransacaoRepository:
        if Enviroments.get_envs().stage == STAGE.TEST:
            from .repo.transacoes_repository_mock import ITransacaoRepositoryMock
            return TransacaoRepositoryMock
        else:
            raise EnviromentNotFound("STAGE")

    @staticmethod
    def post_transaction_repo() ->ITransacaoRepository:
        if Enviroments.post_envs().stage == STAGE.TEST:
            post()
        else:
            raise EnviromentNotFound("STAGE")

    @staticmethod
    def get_envs() -> "Environments":
        """
        Returns the Environments object. This method should be used to get the Environments object instead of instantiating it directly.
        :return: Environments (stage={self.stage})

        """
        envs = Environments()
        envs.load_envs()
        return envs

    @staticmethod
    def post_envs() -> "Enviroments":
        envs = Enviroments.post()
        envs.load_envs()

    def __repr__(self):
        return self.__dict__