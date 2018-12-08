'''
Class:      RobinhoodReader
Author(s):  Sam Badger
Date:       December 8, 2018
Type:       FINAL
Description:
            This is the Reader portion of the Robinhood API.
            
            It is used to get information from Robinhood such as prices, stocks
            owned, price history, etc.
            
            You cannot use this API to place trades or issue any commands that
            will somehow change your account.
'''

from Robinhood import Robinhood

class RobinhoodReader():
    def __init__(self):
        self.api = Robinhood()
        
        
    ##################
    # Authentication #
    ##################
    def login(self, username, password, mfa_code=None):
        return self.api.login(username, password, mfa_code=mfa_code)
        
    def logout(self):
        return self.api.logout()
        
    ##########################
    # User-specific requests #
    ##########################
    def investment_profile(self):
        return self.api.investment_profile()
    
    def get_account(self):
        return self.api.get_account()
        
    def portfolios(self):
        return self.api.portfolios()
        
    def adjusted_equity_previous_close(self):
        return self.api.adjusted_equity_previous_close()
        
    def equity(self):
        return self.api.equity()
        
    def equity_previous_close(self):
        return self.api.equity_previous_close()
        
    def excess_margin(self):
        return self.api.excess_margin()
        
    def extended_hours_equity(self):
        return self.api.extended_hours_equity()
        
        
    ##############################
    # Non user-specific requests #
    ##############################
    def instruments(self, ticker):
        return self.api.instruments(ticker)
        
    def instrument(self, id):
        return self.api.instrument(id)
        
    def quote_data(self, stock=''):
        return self.api.quote_data(stock)
        
    def quotes_data(self, stocks):
        return self.api.quotes_data(stocks)
        
    def get_quote_list(self, stock='', key=''):
        return self.api.get_quote_list(stock, key)
        
    def get_quote(self, stock=''):
        return self.api.get_quote(stock)
        
    def get_news(self, stock):
        return self.api.get_news(stock)
        
    def print_quote(self, stock=''):
        return self.api.print_quote(stock)
        
    def print_quotes(self, stocks):
        return self.api.print_quotes(stocks)
        
    def ask_price(self, stock=''):
        return self.api.ask_price(stock)
        
    def ask_size(self, stock=''):
        return self.api.ask_price(stock)
        
    def bid_price(self, stock='':
        return self.api.bid_price(stock)
        
    def bid_size(self, stock=''):
        return self.api.bid_price(stock)
        
    def last_trade_price(self, stock=''):
        return self.api.last_trade_price(stock)
        
    def previous_close(self, stock=''):
        return self.api.previous_close(stock='')
        
    def previous_close_date(self, stock=''):
        return self.api.previous_close_date(stock)
        
    def adjusted_previous_close(self, stock=''):
        return self.api.adjusted_previous_close(stock)
        
    def symbol(self, stock=''):
        return self.api.symbol(stock)
        
    def last_updated_at(self, stock):
        return self.api.last_updated_at(stock)
           
    def get_url(self, url):
        return self.api.get_url(url)
        
    def popularity(self, stock=''):
        return self.api.get_popularity(stock)
        
    def get_tickers_by_tag(self, tag=None):
        return self.api.get_tickers_by_tag(tag)
        
    def get_options(self, stock, expiration_dates, option_type):
        return self.api.get_options(stock, expiration_dates, option_type)
        
    def get_option_market_data(self, optionid):
        return self.api.get_option_market_data(optionid)
        
    def get_fundamentals(self, stock='', url=''):
        return self.api.get_fundamentals(self, stock, url)
        
    def fundamentals(self, stock='', url=''):
        return self.api.fundamentals(stock, url)
        
    def get_ticker_from_fundamentals_url(self, url):
        return self.api.get_ticker_from_fundamentals_url(url)
        
    
        
     
    
    def __str__(self):
        return "Reader portion of the Robinhood API"
        
