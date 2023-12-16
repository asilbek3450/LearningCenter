import psycopg2  # pip install psycopg2

# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/learning_center'
# DATABASE_URL = 'postgresql://username:password@localhost:5432/db_name'

conn = psycopg2.connect(
    database="defaultdb",
    username="doadmin",
    password="AVNS_KF6MzrKaolPLpVI9MB0",
    host="dbaas-db-7166939-do-user-13959110-0.c.db.ondigitalocean.com",
    port="25060",
    sslmode="require"
)
cursor = conn.cursor()


def create_users_table():
    # conn = psycopg2.connect(DATABASE_URL)
    # cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS registrated_users (
            id SERIAL PRIMARY KEY,
            user_id INTEGER,
            course VARCHAR(255),
            full_name VARCHAR(255),
            phone_number VARCHAR(255),
            joined TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    conn.close()
    return True


# insert data into the database
async def add_users_to_db(informations: dict):
    # conn = psycopg2.connect(DATABASE_URL)
    # cursor = conn.cursor()
    cursor.execute("INSERT INTO registrated_users (user_id, course, full_name, phone_number) VALUES (%s, %s, %s, %s)",
                   (informations['user_id'], informations['course'], informations['name'],
                    informations['phone']))
    conn.commit()
    conn.close()


# get data from the database
async def get_users_from_db():
    # conn = psycopg2.connect(DATABASE_URL)
    # cursor = conn.cursor()
    cursor.execute("SELECT * FROM registrated_users;")
    users = cursor.fetchall()
    conn.close()
    return users
