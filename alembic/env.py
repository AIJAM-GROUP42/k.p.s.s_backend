from logging.config import fileConfig
import os
import sys
from sqlalchemy import engine_from_config, pool
from alembic import context

# Proje yolunu ekle
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# .env dosyasını yükle
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")

# Ayarları çek
from config.settings import settings
from models.base import Base
from models import user, lesson, quiz_result
#veya from models import User, QuizResult, Lesson  # modellerin hepsi burada tanıtılsın


config = context.config
fileConfig(config.config_file_name)

# Alembic'e bağlantı URL'sini ver
config.set_main_option("sqlalchemy.url", settings.DATABASE_URL)

target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()