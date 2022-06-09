# Created by vidit.singh at 07-06-2022
from src.utils import datasets

orders_dataset = datasets.get('orders')
order_item_dataset = datasets.get('order_items')


# get number of complete orders placed by each customer.

def my_filter(order, filter1):
    return [
        (int(item.split(',')[2]), item.split(',')[3])
        for item in order
        if filter1(item)
    ]


def reduce_by_key(orders_dict):
    cust_order = {}
    for oi, values in orders_dict:
        if oi in cust_order:
            cust_order[oi] = (values, cust_order.get(oi)[1] + 1)
        else:
            cust_order[oi] = (values, 1)
    return cust_order


def get_revenue_by_customer_id(orders, status):
    order_cust_status = my_filter(datasets.get(orders), lambda order: order.split(',')[3] == status)
    return reduce_by_key(order_cust_status)


# print(get_revenue_by_customer_id('orders', 'COMPLETE'))


# Get total number of PENDING, PENDING_PAYMENT orders from month of January-2014

def filter_by_date_and_status(order, filter1):
    return [
        (item.split(',')[1], item.split(',')[3])
        for item in order
        if filter1(item)
    ]


def get_status_count_by_month_and_status(orders, status, date):
    return (date, len(filter_by_date_and_status(orders,
                                                lambda order: order.split(',')[3] in status.split(',') and
                                                              order.split(',')[1][:7].startswith(date))))


# print(get_status_count_by_month_and_status(orders_dataset, 'PENDING,PENDING_PAYMENT', '2014-01'))


# Get outstanding amount for each month considering orders with status PAYMENT_REVIEW,PAYMENT_PENDING,PENDING,PROCESSING

def filter_by_order_date(order, filter1):
    return {
        int(item.split(',')[0]): item.split(',')[1]
        for item in order
        if filter1(item)
    }


def reduce_by_date(order_status, order_item_ds):
    orders_month = {}
    for order_it in order_item_ds:
        order_item_order_id = int(order_it.split(',')[1])
        order_item_subtotal = float(order_it.split(',')[4])
        if order_item_order_id in order_status:
            order_dict_date = order_status[order_item_order_id]
            if order_dict_date in orders_month:
                orders_month[order_dict_date] = round(orders_month[order_dict_date] + order_item_subtotal, 2)
            else:
                orders_month[order_dict_date] = order_item_subtotal
    return orders_month


def get_order_outstanding_by_month_and_status(orders, order_item_ds, status):
    orders_status = filter_by_order_date(orders, lambda order: order.split(',')[3] in status.split(','))
    return reduce_by_date(orders_status, order_item_ds)


print(get_order_outstanding_by_month_and_status(orders_dataset, order_item_dataset, 'PAYMENT_REVIEW,PAYMENT_PENDING,'
                                                                                    'PENDING,PROCESSING'))
