# Created by vidit.singh at 09-06-2022
import datetime as dt
import calendar
from src.utils import datasets

orders_dataset = datasets.get('orders')
order_item_dataset = datasets.get('order_items')


#  Find out which day has maximum revenue.

# pre-requisites
# 1. date,order_id,
# 2. order_sub_total
# 3. Join the orders_dataset & order_item_dataset on order_id
# 4. strip the day from the date on matching join. put in map and aggregate
# 5. filter in closed and completed order.

def get_completed_and_closed_orders(status):
    closed_completed_orderId_date = filter(lambda order: order.split(',')[3] in status, orders_dataset)
    order_list = map(get_order_id_date, closed_completed_orderId_date)
    return get_order_dict(list(order_list))


def get_order_id_date(order):
    day = calendar.day_name[dt.datetime.strptime(order.split(',')[1].split(' ')[0], '%Y-%m-%d').weekday()]
    return {int(order.split(',')[0]): day}


def get_order_dict(order_list):
    order_dict = {}
    for o in iter(order_list):
        dd = list(o.items())[0]
        order_dict[dd[0]] = dd[1]

    return order_dict


def get_revenue_by_days(status):
    order_dict = get_completed_and_closed_orders(status)
    order_revenue = {}
    for oi in order_item_dataset:
        order_items = oi.split(',')
        order_item_order_id = int(order_items[1])

        if order_item_order_id in order_dict:
            order_day = order_dict[order_item_order_id]
            if order_day in order_revenue:
                order_revenue[order_day] = round(order_revenue[order_day] + float(order_items[4]), 2)
            else:
                order_revenue[order_day] = float(order_items[4])
    return order_revenue


daily_revenue = get_revenue_by_days('COMPLETE,CLOSED')
print(sorted(daily_revenue.items(), key=lambda order: order[1]))
