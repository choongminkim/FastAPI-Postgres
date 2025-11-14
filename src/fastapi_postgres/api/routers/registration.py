from fastapi import APIRouter, Depends

from fastapi_postgres.schemas.registration import RegistrationInput

router = APIRouter(prefix="/registration", tags=["registration"])


class UserRepositoryInterface:
    def get_user(self, user_id: int):
        pass


class MySQLUserRepository(UserRepositoryInterface):
    def get_user(self, user_id: int):
        # MySQL 데이터베이스에서 사용자 조회
        return {"id": user_id, "name": "MySQL User"}


def get_user_service(repo: UserRepositoryInterface = Depends(MySQLUserRepository)):
    def get_user(user_id: int):
        return repo.get_user(user_id)

    return get_user


@router.get("/{user_id}")
def get_user(user_id: int, service=Depends(get_user_service)):
    return service(user_id)
