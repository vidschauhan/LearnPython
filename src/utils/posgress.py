# Created by vidit.singh at 24-05-2022
import psycopg2


class Posgress:

    @staticmethod
    def connect(*args):
        return psycopg2.connect(host=args[0],
                                port=args[1],
                                database=args[2],
                                user=args[3],
                                password=args[4])
