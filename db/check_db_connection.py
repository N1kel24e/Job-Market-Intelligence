from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


def main() -> None:
    db_url = URL.create(
        drivername="postgresql+psycopg",
        username="jmi_user",
        password="jmi_pass",
        host="127.0.0.1",
        port=5432,
        database="job_market",
    )

    engine = create_engine(
        db_url,
        echo=False,
        connect_args={"sslmode": "disable"}
    )

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1")).scalar()
        print(f"DB connection OK, SELECT 1 -> {result}")


if __name__ == "__main__":
    main()