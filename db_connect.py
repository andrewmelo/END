import mariadb
import sys
from config import DB_USER
from config import DB_PSSWD
from config import HOST
from config import PORT
from config import DATABASE

try:
    conn = mariadb.connect(
        user=DB_USER,
        password=DB_PSSWD,
        host=HOST,
        port=int(PORT),
        database=DATABASE
    )    
except mariadb.Error as e:
    print(f'Error connecting to MariaDB Platform: {e}')
    sys.exit(1)
    
cursor = conn.cursor(dictionary=True)
