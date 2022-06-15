# Created by vidit.singh at 14-06-2022

from src.utils.posgress import Posgress

connection = Posgress.connect('localhost', 5432, 'itversity_hr_db', 'itversity_hr_user', 'password')

cursor = connection.cursor()
query = ("""
    INSERT INTO users 
        (user_first_name, user_last_name, user_email_id)
    VALUES 
        ('Scott', 'Tiger', 'scott@tiger.com')
""")
#cursor.execute(query)

# Inserting Multiple records.
query1 = ("""
    INSERT INTO users 
        (user_first_name, user_last_name, user_email_id, user_password, user_role, is_active)
    VALUES 
        (%s, %s, %s, %s, %s, %s)
""")

users = [
    ('Gordan', 'Bradock', 'gbradock0@barnesandnoble.com', 'h9LAz7p7ub', 'U', True),
    ('Tobe', 'Lyness', 'tlyness1@paginegialle.it', 'oEofndp', 'U', True),
    ('Addie', 'Mesias', 'amesias2@twitpic.com', 'ih7Y69u56', 'U', True)
]

cursor.executemany(query1, users)
connection.commit()

cursor.close()
connection.close()