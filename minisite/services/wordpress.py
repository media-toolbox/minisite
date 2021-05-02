from fastapi_sqlalchemy import db
from passlib.hash import phpass
from sqlalchemy import text

from minisite.core.config import config

WP_USERS_TABLE = config.get("MS_WP_USERS_TABLE")


def verify_password(username: str, password: str):

    statement = text(
        f"SELECT user_pass FROM {WP_USERS_TABLE} "
        f"WHERE user_login=:username OR user_email=:username"
    )
    result = db.session.execute(statement, {"username": username})
    hash = next(result)["user_pass"]

    verify_hash(password, hash)


def verify_hash(password, hash):
    if phpass.verify(password, hash):
        return True
    else:
        return False
