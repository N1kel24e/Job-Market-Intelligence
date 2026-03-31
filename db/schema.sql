CREATE TABLE vacancies
(
    id          SERIAL PRIMARY KEY,
    external_id int,
    vac_source  varchar(255),
    job_name    varchar(255),
    min_sal     int,
    max_sal     int,
    currency    varchar(255),
    grade       varchar(255),
    stack       text[],
    requirements text[],
    parsed_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (external_id, vac_source)
)