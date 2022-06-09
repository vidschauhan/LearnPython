# Created by vidit.singh at 06-06-2022

from src.utils import datasets


def get_orders_dict(status, orders):
    orders = datasets.get(orders)
    order_dict = {}
    for order in orders:
        order_detail = order.split(',')
        if status == order_detail[3]:
            order_dict[int(order_detail[0])] = order_detail[1]
    return order_dict


# Using dictionary comp method.

def get_orders(status, orders):
    return {int(order.split(',')[0]): order.split(',')[1]  # Transformation logic
            for order in datasets.get(orders)  # For loop
            if order.split(',')[3] == status}  # filter condition.


def get_daily_revenue(status, orders, order_items):
    orders_id_date_dict = get_orders(status, orders)
    order_items_dataset = datasets.get(order_items)
    daily_revenue = {}
    for o_item in order_items_dataset:
        order_item = o_item.split(',')
        order_item_order_id = int(order_item[1])
        order_item_sub_total = float(order_item[4])

        if order_item_order_id in orders_id_date_dict:
            order_date = orders_id_date_dict[order_item_order_id]

            if order_date in daily_revenue:
                daily_revenue[order_date] = round(daily_revenue[order_date] + order_item_sub_total, 2)
            else:
                daily_revenue[order_date] = order_item_sub_total

    return daily_revenue


print((get_daily_revenue('COMPLETE', 'orders', 'order_items')))
