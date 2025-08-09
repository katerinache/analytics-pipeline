import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

@dataclass
class ClickHouseCfg:
    host: str = os.getenv("CH_HOST", "localhost")
    port: int = int(os.getenv("CH_PORT", "9000"))
    user: str = os.getenv("CH_USER", "default")
    password: str = os.getenv("CH_PASSWORD", "")
    database: str = os.getenv("CH_DATABASE", "default")
    secure: bool = os.getenv("CH_SECURE", "false").lower() == "true"

@dataclass
class PostgresCfg:
    dsn: str = os.getenv("PG_DSN", "postgresql+psycopg://user:pass@localhost:5432/analytics")

@dataclass
class OpenAICfg:
    api_key: str = os.getenv("OPENAI_API_KEY", "")
    chat_model: str = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o-mini")
    emb_model: str = os.getenv("OPENAI_EMB_MODEL", "text-embedding-3-small")

CH = ClickHouseCfg()
PG = PostgresCfg()
OA = OpenAICfg()

