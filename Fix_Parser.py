"""
This is a python 2.7 script which reads the generated FIX messages.
argument :output file name generated from generator script
output : stats of fix messages

"""
# import necessary modules
import sys
import numpy as np


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print 'python parser_script.py fixmsg_filename'
        exit(1)

    fix_message_file = sys.argv[1]

    #intitating stat dictionary to collect data values from each line of generated fake message.
    # stat_prod dictionary to keep track of product, later on used for calculating average value.
    statistics = dict()
    statistics_products = dict()

    # loop to read line by line of generated fake message
    for lines in open(fix_message_file, 'r'):
        #print line
        line = lines.strip().split('|')[2:]
        for item in line:
            item = item.split('=')
            if item[0] in statistics.keys():
                statistics[item[0]].append(item[1])
            else:
                statistics[item[0]] = [item[1]]
            if item[0]=='55':
                if item[1] in statistics_products.keys():
                    statistics_products[item[1]].append(int(line[2].split('=')[1]))
                else:
                    statistics_products[item[1]] = [int(line[2].split('=')[1])]

    # stat 1: Count of stock types
    print 'Count of stock types'
    print '# FUT:', statistics['167'].count('FUT')
    print '# OPT:', statistics['167'].count('OPT')
    print '# CS:', statistics['167'].count('CS')

    # stat 2: minimum,mean,median,maximum values for 'buy' and 'sell'.
           # Also 'average gain-difference of mean values',
           #a +ve value = profit, a -ve value = loss for the overall investment trend
    buy = []; sell = []
    for index_val, val in enumerate(statistics['54']):
        if val == '1':
            buy.append(float(statistics['44'][index_val]))
        else:
            sell.append(float(statistics['44'][index_val]))
    print '\n', 'Comparison of Buy and Sell prices'
    print 'buy:'
    print 'minimum is: ', np.min(buy)
    print 'mean is: ', np.mean(buy)
    print 'median is: ', np.median(buy)
    print 'maximum is: ', np.max(buy)

    print 'sell:'
    print 'minimum is: ', np.min(sell)
    print 'mean is: ', np.mean(sell)
    print 'median is: ', np.median(sell)
    print 'maximum is: ', np.max(sell)

    print 'avg. gain:',  np.mean(sell) - np.mean(buy)

    #stat 3 - Occurences of unique orders
    print '\n','Occurences of unique orders'

    orders ={'1':'Market', '2':'Limit','3':'Stop','4':'Stop limit','5':'Market on close'}
    popular_order = set(statistics['40'])
    max_order = ''
    max_order_value = -np.inf
    for order in popular_order:
        count_order = statistics['40'].count(order)
        print orders[order], ':', count_order
        if count_order > max_order_value:
            max_order = order
            max_order_value = count_order

    #stat 4 - Most popular order-types
    print 'Most popular order:', orders[max_order], ' occurence:', max_order_value, '\n'

    #stat 5 - Average ordered quantity per product
    print 'Average ordered quantity per product: '
    for key,val in statistics_products.items():
        print key, sum(val)/float(len(val))

    #stat 6 - Occurences of unique symbol
    print '\n', 'Occurences of unique symbols'
    uniq_symbol = set(statistics['55'])
    max_symbol = ''
    max_symbol_count = -np.inf
    for item in uniq_symbol:
        count_symbol = statistics['55'].count(item)
        print item, ':', count_symbol
        if count_symbol > max_symbol_count:
            max_symbol = item
            max_symbol_count = count_symbol

    #stat 7 - Most popular symbol:
    print 'Most popular symbol'

    print 'max_pop_sym', max_symbol, 'count:', max_symbol_count
