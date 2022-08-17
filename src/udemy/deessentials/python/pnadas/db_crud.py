# Created by vidit.singh at 18-06-2022
import sys
from src.utils.posgress import Posgress
from src.udemy.deessentials.python.pnadas.reader import get_json_reader
from src.udemy.deessentials.python.pnadas.writer import write_sql


def main():
    # get json reader df in chunks
    conn = Posgress.get_sql_alchemy_connection('itversity_retail_user_batch', 'password', 'localhost', 5432,
                                               'itversity_retail_db_batch_processing')
    tables = sys.argv[1].split(',')  # table names will be passed as program argument as comma separated
    for table in tables:
        df = get_json_reader(table, 3000)
        write_sql(df, conn, table)


if __name__ == '__main__':
    main()

# print('Reading from Database ::: ')
# query = 'SELECT order_date,order_status,count(1) FROM orders GROUP BY order_date,order_status ORDER BY order_date,' \
#        'order_status LIMIT 10 '
# data = pd.read_sql(query, conn)
# print(data)
