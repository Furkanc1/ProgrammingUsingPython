import yfinance as yf;
myinput = input("please entera stock symbol: ")
mystock=yf.Ticker(myinput)
information = mystock.fast_info

print(information)