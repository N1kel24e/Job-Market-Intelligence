from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

def init_db():
    db_url = URL.create(
        drivername="postgresql+psycopg",
        username="jmi_user",
        password="jmi_pass",
        host="127.0.0.1",
        port=5432,
        database="job_market"
    )

    engine = create_engine(
        db_url,
        echo=False,
        connect_args={"sslmode": "disable"}
    )

    with open("db/schema.sql") as f:
        content = f.read()
    with engine.connect() as conn:
        conn.execute(text(content))
        conn.commit()

if __name__ == "__main__":
    init_db()