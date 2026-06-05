import hashlib
from database import conn, cursor

def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def register(username, password):

    try:

        hashed_password = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users
            (username, password)
            VALUES (?,?)
            """,
            (username, hashed_password)
        )

        conn.commit()

        return True

    except:

        return False


def login(username, password):

    hashed_password = hash_password(password)

    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=?
        AND password=?
        """,
        (username, hashed_password)
    )

    user = cursor.fetchone()

    return user