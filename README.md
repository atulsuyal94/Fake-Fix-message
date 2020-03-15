# Fake-Fix-message

FIX is an open source protocol widely used to trade all asset types in the global financial systems.

We have produced a fake simplified FIX 4.2 message which the candidate is to use as a basis to produce a dataset of fake FIX messages.

 

Step 1 – Write a python 2.7 script capable of generating fake FIX messages, the candidate needs to use the below description and online FIX 4.2 documentation. The script should be able to take 1 argument to specify the amount of fake FIX messages to generate. They need to be aggregated in a file to be used for step 2.

 

Step 2 – Write a python 2.7 script capable of reading the generated FIX messages and produce various statistics on the trading habits of each clients.

The type of stats could be the message amount per clients, list of all the traded products(symbols), most popular order type(40), average ordered quantity per product. Please feel free to be creative and generate other stats. Produce at least 5 stats.

 

Step 3 – The two scripts need to be pushed to https://github.com and the link sent to our team for review.

 

EX 1: Simplified FIX 4.2 new order message example:

8=FIX.4.2|35=D|55=SYMBOL_1|54=1|38=100|40=2|59=0|167=FUT|1=CLIENT_1|44=199.99

 

EX 2: Simplified rules:

8=FIX.4.2 (always this value)

35=D (always a new order message ‘D’)

55=SYMBOL_N (Symbol meaning the product name: N is a number) Note that in real life this could be a stock like GOOGLE

54=[1-2] side (buy or sell the given symbol/product)

38=N (quantity of the symbol/product that you want to buy or sell)

40=[1-5] (only order types 1-5 per the FIX 4.2 spec: http://btobits.com/fixopaedia/fixdic42/tag_40_OrdType_.html)

59=[0-6] (all time in force orders per FIX 4.2 spec: https://www.onixs.biz/fix-dictionary/4.2/tagNum_59.html)

167=(FUT|OPT|CS) (Futures, Options and Common stocks)

1=CLIENT_N (random client id)

44=Any price (price at which you will sell or buy the given product)



usage :

1. download / clone the repo
2. run the fix generator : python Fix_Generate.py num-of-fix-msg-to-generate output-filename
3. To see the stats : python Fix_Parser.py output-filename
