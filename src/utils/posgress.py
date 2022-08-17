# Created by vidit.singh at 24-05-2022
import psycopg2


class Posgress:

    @staticmethod
    def connect(*args):
        connection = None
        try:
            connection = psycopg2.connect(host=args[0],
                                          port=args[1],
                                          database=args[2],
                                          user=args[3],
                                          password=args[4])
        except Exception as e:
            raise e
        return connection

    @staticmethod
    def get_sql_alchemy_connection(username, password, host, port, database):
        return f'postgresql://{username}:{password}@{host}:{port}/{database}'
