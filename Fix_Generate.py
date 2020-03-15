"""
This is a python 2.7 script to generates fake FIX messages.
arguments(2) : 1st - num_fix_messages_to_generate  ; 2nd - output fix file name

"""

#importing necessary modules
import random
import sys


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print 'python python_script.py num_fake_fix_messages output_fix_filename'
        exit(1)

    num_fake_fix_msgs = int(sys.argv[1])
    output_fix_filename = sys.argv[2]

    #setting up fix_rule dictionary:
    # 54 - 1(buy) or 2(sell) the given symbol/product
    # 40 - Orde Type. 1-Market, 2-Limit, 3-Stop, 4-Stop limit, 5-Market on close
    # 59=[0-6] (all time in force orders per FIX 4.2 spec: https://www.onixs.biz/fix-dictionary/4.2/tagNum_59.html)
    # 167 - FUT-Future, OPT-Options, CS-Common Stocks


    fix_msg_rule = {'54':['1','2'],
                '40':['1','2','3','4','5'],
                '59':['0','1','2','3','4','5','6'],
                '167':['FUT', 'OPT', 'CS'],
                }

    fid = open(output_fix_filename, 'w')

    for _ in range(num_fake_fix_msgs):

	# symbol_n is the company listing
        val_symbol_n = str(random.randint(1,10))

	# select a random value for buy or sell
        val_54 = random.choice(fix_msg_rule['54'])

    # quantity of the symbol/product tp buy or sell
        val_38 = str(random.randint(1,10000))


        val_40 = random.choice(fix_msg_rule['40'])

        val_59 = random.choice(fix_msg_rule['59'])

        val_167 = random.choice(fix_msg_rule['167'])

        #client_n (random client id)
        val_client_n = str(random.randint(1,100000))

        #Any price (price at which you will sell or buy the given product)
        val_any_price = str(random.uniform(0, 10000))

        msg = '8=FIX.4.2|35=D|55=SYMBOL_'+val_symbol_n+'|54='+val_54+'|38='+val_38+'|40='+val_40
        msg += '|59='+val_59+'|167='+val_167+'|1=CLIENT_'+val_client_n+'|44='+val_any_price

        #print msg
        fid.write(msg+'\n')


    fid.close()
