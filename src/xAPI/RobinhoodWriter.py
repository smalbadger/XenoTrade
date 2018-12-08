'''
Class:      RobinhoodWriter
Author(s):  Sam Badger
Date:       December 8, 2018
Type:       FINAL
Description:
            This is the Writer portion of the Robinhood API.
            
            You can use this API to place trades or issue any commands that
            will somehow change your account.
            
            You cannot use it to get information from Robinhood such as prices, 
            stocks owned, price history, etc.
'''

from Robinhood import Robinhood

class RobinhoodReader:
    def __init__(self):
        self.api = Robinhood()
        
    ##################
    # Authentication #
    ##################
    def login(self, username, password, mfa_code=None):
        return self.api.login(username, password, mfa_code=mfa_code)
        
    def logout(self):
        return self.api.logout()
        
    ################
    # Place orders #
    ################
    def place_order(self, instrument, quantity=1, price=0.0, transaction=None, triggers='immediate', order='market', time_in_force='gfd'):
        return self.api.place_order(instrument, quantity, price, transaction, triggers, order, time_in_force)
        
    def cancel_order(self, order_id):
        return self.api.cancel_order(order_id)
        
        ##############
        # Buy orders #
        ##############
    def place_buy_order(self, instrument, quantity, bid_price=0.0):
        return self.api.place_buy_order(instrument, quantity, bid_price) 
    
    def place_market_buy_order(self, instrument_URL=None, symbol=None, time_in_force=None, Quantity=None):
        return self.api.place_market_buy_order(instrument_URL, symbol, time_in_force, quantity)
        
    def place_limit_buy_order(self, instrument_URL=None, symbol=None, time_in_force=None, price=None, quantity=None):
        return self.api.place_limit_buy_order(instrument_URL, symbol, time_in_force, price, quantity)
    
    def place_stop_loss_buy_order(self, instrument_URL=None, symbol=None, time_in_force=None, stop_price=None, quantity=None):
        return self.api.place_stop_loss_buy_order(instrument_URL, symbol, time_in_force, stop_price, quantity)
        
    def place_stop_limit_buy_order(self, instrument_URL=None, symbol=None, time_in_force=None, stop_price=None, price=None, quantity=None):
        return self.api.place_stop_limit_buy_order(instrument_URL, symbol, time_in_force, stop_price, price, quantity)
        
        ###############
        # Sell orders #
        ###############
    def place_sell_order(self, instrument, quantity, bid_price=0.0):
        return self.api.place_sell_order(instrument, quantity, bid_price)
        
    def place_market_sell_order(self, instrument_URL=None, symbol=None, time_in_force=None, quantity=None):
        return self.api.place_market_sell_order(instrument_URL, symbol, time_in_force, quantity)
        
    def place_limit_sell_order(self, instrument_URL=None, symbol=None, time_in_force=None, price=None, quantity=None):
        return self.api.place_limit_sell_order(instrument_URL, symbol, time_in_force, price, quantity)
        
    def place_stop_loss_sell_order(self, instrument_URL=None, symbol=None, time_in_force=None, stop_price=None, quantity=None):
        return self.api.place_stop_loss_sell_order(instrument_URL, symbol, time_in_force, stop_price, quantity)
        
    def place_stop_limit_sell_order(self, instrument_URL=None, symbol=None, time_in_force=None, price=None, stop_price=None, quantity=None):
        return self.api.place_stop_limit_sell_order(instrument_URL, symbol, time_in_force, price, stop_price, quantity)
    
    def submit_order(self, instrument_URL=None, symbol=None, order_type=None, time_in_force=None, trigger=None, price=None, stop_price=None, quantity=None, side=None):
        return self.api.submit_order(instrument_URL, symbol, order_type, time_in_force, trigger, price, stop_price, quantity, side)
    
    
    
    
    def __str__(self):
        return "Robinhood Writer API"
        
