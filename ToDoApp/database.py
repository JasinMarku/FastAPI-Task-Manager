from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import os
from sqlalchemy.pool import StaticPool

# Get database URL from environment variable, or use default
# For local development, you can set DATABASE_URL to use SQLite:
# export DATABASE_URL="sqlite:///./local.db"
# Or use PostgreSQL:
# export DATABASE_URL="postgresql+psycopg2://user:pass@host/db"
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL",
    # Default: Use SQLite for local development
    "sqlite:///./local.db"
)

# Determine if we're using SQLite or PostgreSQL
is_sqlite = SQLALCHEMY_DATABASE_URL.startswith("sqlite")

if is_sqlite:
    # SQLite configuration for local development
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    # PostgreSQL configuration (for Render.com or other PostgreSQL databases)
    # Try to extract SSL mode from URL or use require as default
    connect_args = {
        "sslmode": "require",
        "keepalives": 1,
        "keepalives_idle": 60,
        "keepalives_interval": 10,
        "keepalives_count": 5,
        "connect_timeout": 10
    }
    
    # If URL contains sslmode parameter, use it
    if "sslmode=" in SQLALCHEMY_DATABASE_URL:
        # Extract sslmode from URL if present
        pass  # SQLAlchemy will handle it from the URL
    
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args=connect_args,
        pool_pre_ping=True,  # Verify connections before using them
        pool_recycle=300,  # Recycle connections after 5 minutes
    )

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for models
Base = declarative_base()

# Print database type for debugging
if is_sqlite:
    print(f"Using SQLite database: {SQLALCHEMY_DATABASE_URL}")
else:
    # Mask password in URL for security
    safe_url = SQLALCHEMY_DATABASE_URL.split("@")[-1] if "@" in SQLALCHEMY_DATABASE_URL else SQLALCHEMY_DATABASE_URL
    print(f"Using PostgreSQL database: postgresql://***@{safe_url}")