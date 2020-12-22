import os
from pathlib import Path

from dotenv import load_dotenv


class MetaEnv(type):
    prefix = "MMDB_"

    @property
    def DEBUG(cls):
        default = "true"
        return cls._get("DEBUG", default, prefix=True) in cls.truevals

    @property
    def SECRET_KEY(cls):
        default = "mmdb" if cls.DEBUG else ""
        return cls._get("SECRET_KEY", default, prefix=True)

    @property
    def ALLOWED_HOSTS(cls):
        default = "*"
        return [
            host
            for host in cls._get("ALLOWED_HOSTS", default, prefix=True).split(",")
            if host
        ]

    @property
    def MMDB_PORT(cls):
        default = "8002"
        return cls._get("MMDB_PORT", default)

    @property
    def MMDB_TOKEN_TTL(cls):
        default = 1000 * 60 * 15  # 15 minute lifespan by default
        return int(cls._get("MMDB_TOKEN_TTL", default))

    @property
    def MMDB_VERSION_NUMBER(cls):
        default = "Not Specified"  # 15 minute lifespan by default
        return cls._get("MMDB_VERSION_NUMBER", default)

    @property
    def SQL_DATABASE(cls):
        default = "mmdb" if cls.DEBUG else ""
        return cls._get("SQL_DATABASE", default)

    @property
    def SQL_HOST(cls):
        default = "127.0.0.1" if cls.DEBUG else ""
        sql_host = cls._get("SQL_HOST", default)
        # Force TCP connection rather than UNIX socket
        if sql_host == "localhost":
            return "127.0.0.1"
        return sql_host

    @property
    def SQL_PORT(cls):
        default = "3306"
        return cls._get("SQL_PORT", default)

    @property
    def SQL_USER(cls):
        default = "root" if cls.DEBUG else ""
        return cls._get("SQL_USER", default)

    @property
    def SQL_PASSWORD(cls):
        default = ""
        return cls._get("SQL_PASSWORD", default)


class env(metaclass=MetaEnv):
    truevals = ("true", "True", "yes", "y", "1", "on", "ok", True)

    def load():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        base_env = os.path.join(base_dir, ".env")
        load_dotenv(dotenv_path=Path(base_env))
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mmdb.settings")

    load()

    @classmethod
    def _get(cls, key, default, prefix=False):
        value = os.getenv(cls.prefix + key)
        global_value = os.getenv(key)
        if value and prefix:
            return value
        elif not global_value:
            return default
        return global_value
