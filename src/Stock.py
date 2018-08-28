from datetime import datetime as dt
from pprint import pprint
class Stock:
    def __init__(self, t, pos=None, ins=None):
        '''
        Params:
            - The Robinhood Object of the logged in user
            - The Positions dictionary returned from
              Robinhood.securities_owned()['results'][index] (if security is owned)
            - The instrument URL of the stock (not needed if security is owned)
        '''
        print("Making another stock")
        self.trader = t
        self.position = pos
        self.instrument = None
        self.fundamentals = None
        self.quote = None
        self.popularity = None

        if pos:
            ins = pos['instrument']
        self.instrument = t.instrument(ins)
        self.fundamentals = t.fundamentals(url=self.instrument['fundamentals'])
        self.quote = self.trader.quote_data(self.symbol())
        self.popularity = self.trader.get_popularity(self.symbol())







    def updateAllProperties(self):
        if self.position:
            # TODO: (A) Figure out how to update the position
            pass

        self.instrument = self.trader.instrument(self.instrumentURL())
        self.fundamentals = self.trader.fundamentals(self.fundamentalsURL())
        self.quote = self.trader.quote_data(self.symbol())
        self.popularity = self.trader.get_popularity(self.symbol())








    def printInfo(self, printOriginals=False):
        ''' This function is mostly for testing purposes to make sure all getters are working. '''
        print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")
        if printOriginals:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            pprint(self.position)
            pprint(self.instrument)
            pprint(self.fundamentals)
            pprint(self.quote)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("accountURL: {}".format(self.accountURL()))
        print("averageBuyPrice: {}".format(self.averageBuyPrice()))
        print("createdAt: {}".format(self.createdAt()))
        print("intradayAverageBuyPrice: {}".format(self.intradayAverageBuyPrice()))
        print("intradayQuantity: {}".format(self.intradayQuantity()))
        print("pendingAverageBuyPrice: {}".format(self.pendingAverageBuyPrice()))
        print("quantityOwned: {}".format(self.quantityOwned()))
        print("sharesHeldForBuys: {}".format(self.sharesHeldForBuys()))
        print("sharesHeldForOptionsCollateral: {}".format(self.sharesHeldForOptionsCollateral()))
        print("sharesHeldForOptionsEvents: {}".format(self.sharesHeldForOptionsEvents()))
        print("sharesHeldForSells: {}".format(self.sharesHeldForSells()))
        print("sharesHeldForStockGrants: {}".format(self.sharesHeldForStockGrants()))
        print("sharesPendingFromOptionsEvents: {}".format(self.sharesPendingFromOptionsEvents()))
        print("securityUpdatedAt: {}".format(self.securityUpdatedAt()))
        print("bloombergUnique: {}".format(self.bloombergUnique()))
        print("country: {}".format(self.country()))
        print("dayTradeRatio: {}".format(self.dayTradeRatio()))
        print("fundamentalsURL: {}".format(self.fundamentalsURL()))
        print("ID: {}".format(self.ID()))
        print("listDate: {}".format(self.listDate()))
        print("maintenanceRatio: {}".format(self.maintenanceRatio()))
        print("marginInitialRatio: {}".format(self.marginInitialRatio()))
        print("marketURL: {}".format(self.marketURL()))
        print("minTickSize: {}".format(self.minTickSize()))
        print("name: {}".format(self.name()))
        print("quoteURL: {}".format(self.quoteURL()))
        print("RHSTradability: {}".format(self.RHSTradability()))
        print("simpleName: {}".format(self.simpleName()))
        print("splitsURL: {}".format(self.splitsURL()))
        print("state: {}".format(self.state()))
        print("symbol: {}".format(self.symbol()))
        print("tradability: {}".format(self.tradability()))
        print("tradableChainID: {}".format(self.tradableChainID()))
        print("tradable: {}".format(self.tradable()))
        print("type: {}".format(self.type()))
        print("averageVolume: {}".format(self.averageVolume()))
        print("averageVolume2Weeks: {}".format(self.averageVolume2Weeks()))
        print("CEO: {}".format(self.CEO()))
        print("description: {}".format(self.description()))
        print("dividendYield: {}".format(self.dividendYield()))
        print("headquartersCity: {}".format(self.headquartersCity()))
        print("headquartersState: {}".format(self.headquartersState()))
        print("high: {}".format(self.high()))
        print("high52Weeks: {}".format(self.high52Weeks()))
        print("instrumentURL: {}".format(self.instrumentURL()))
        print("low: {}".format(self.low()))
        print("low52Weeks: {}".format(self.low52Weeks()))
        print("marketCap: {}".format(self.marketCap()))
        print("numberOfEmployees: {}".format(self.numberOfEmployees()))
        print("open: {}".format(self.open()))
        print("PERatio: {}".format(self.PERatio()))
        print("sector: {}".format(self.sector()))
        print("sharesOutstanding: {}".format(self.sharesOutstanding()))
        print("volume: {}".format(self.volume()))
        print("yearFounded: {}".format(self.yearFounded()))
        print("adjustedPreviousClose: {}".format(self.adjustedPreviousClose()))
        print("askPrice: {}".format(self.askPrice()))
        print("askSize: {}".format(self.askSize()))
        print("bidPrice: {}".format(self.bidPrice()))
        print("bidSize: {}".format(self.bidSize()))
        print("hasTraded: {}".format(self.hasTraded()))
        print("lastExtendedHoursTradePrice: {}".format(self.lastExtendedHoursTradePrice()))
        print("lastTradePrice: {}".format(self.lastTradePrice()))
        print("lastTradePriceSource: {}".format(self.lastTradePriceSource()))
        print("previousClose: {}".format(self.previousClose()))
        print("previousCloseDate: {}".format(self.previousCloseDate()))
        print("tradingHalted: {}".format(self.tradingHalted()))
        print("quoteUpdatedAt: {}".format(self.quoteUpdatedAt()))
        print("percentChange: {}".format(self.percentChange()))
        print("+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+")


    def getAllInfo(self):
        allDict = {}
        for d in (self.position, self.instrument, self.fundamentals, self.quote):
            try:
                allDict.update(d)
            except:
                pass
        allDict['popularity'] = self.popularity
        return allDict

    ###########################################################################
    ###########################  Positions Getters  ###########################
    ###########################################################################
    def accountURL(self):
        try:
            return self.position['account']
        except:
            return

    def averageBuyPrice(self):
        try:
            return float(self.position['average_buy_price'])
        except:
            return

    def createdAt(self):
        try:
            dateTimeStr = self.position['created_at']
            dateTime = dt.strptime(dateTimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
            return dateTime
        except:
            return

    def intradayAverageBuyPrice(self):
        try:
            return float(self.position['intraday_average_buy_price'])
        except:
            return

    def intradayQuantity(self):
        try:
            return float(self.position['intraday_quantity'])
        except:
            return

    def pendingAverageBuyPrice(self):
        try:
            return float(self.position['pending_average_buy_price'])
        except:
            return

    def quantityOwned(self):
        try:
            return float(self.position['quantity'])
        except:
            return

    def sharesHeldForBuys(self):
        try:
            return float(self.position['shares_held_for_buys'])
        except:
            return

    def sharesHeldForOptionsCollateral(self):
        try:
            return float(self.position['shares_held_for_options_collateral'])
        except:
            return

    def sharesHeldForOptionsEvents(self):
        try:
            return float(self.position['shares_held_for_options_events'])
        except:
            return

    def sharesHeldForSells(self):
        try:
            return float(self.position['shares_held_for_sells'])
        except:
            return

    def sharesHeldForStockGrants(self):
        try:
            return float(self.position['shares_held_for_stock_grants'])
        except:
            return

    def sharesPendingFromOptionsEvents(self):
        try:
            return float(self.position['shares_pending_from_options_events'])
        except:
            return

    def securityUpdatedAt(self):
        try:
            dateTimeStr = self.position['updated_at']
            dateTime = dt.strptime(dateTimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
            return dateTime
        except:
            return

    ###########################################################################
    ###########################  Instrument Getters  ##########################
    ###########################################################################
    def bloombergUnique(self):
        try:
            return self.instrument['bloomberg_unique']
        except:
            return

    def country(self):
        try:
            return self.instrument['country']
        except:
            return

    def dayTradeRatio(self):
        try:
            return float(self.instrument['day_trade_ratio'])
        except:
            return

    def fundamentalsURL(self):
        try:
            return self.instrument['fundamentals']
        except:
            return

    def ID(self):
        try:
            return self.instrument['id']
        except:
            return

    def listDate(self):
        try:
            dateTimeStr = self.instrument['list_date']
            dateTime = dt.strptime(dateTimeStr, '%Y-%m-%d')
            return dateTime
        except:
            return

    def maintenanceRatio(self):
        try:
            return float(self.instrument['maintenance_ratio'])
        except:
            return

    def marginInitialRatio(self):
        try:
            return float(self.instrument['margin_initial_ratio'])
        except:
            return

    def marketURL(self):
        try:
            return self.instrument['market']
        except:
            return

    def minTickSize(self):
        try:
            return float(self.instrument['min_tick_size'])
        except:
            return

    def name(self):
        try:
            return self.instrument['name']
        except:
            return

    def quoteURL(self):
        try:
            return self.instrument['quote']
        except:
            return

    def RHSTradability(self):
        try:
            return self.instrument['rhs_tradability']
        except:
            return

    def simpleName(self):
        try:
            return self.instrument['simple_name']
        except:
            return

    def splitsURL(self):
        try:
            return self.instrument['splits']
        except:
            return

    def state(self):
        try:
            return self.instrument['state']
        except:
            return

    def symbol(self):
        try:
            return self.instrument['symbol']
        except:
            return

    def tradability(self):
        try:
            return self.instrument['tradability']
        except:
            return

    def tradableChainID(self):
        try:
            return self.instrument['tradable_chain_id']
        except:
            return

    def tradable(self):
        try:
            return bool(self.instrument['tradeable'])
        except:
            return

    def type(self):
        try:
            return self.instrument['type']
        except:
            return
    ###########################################################################
    ##########################  Fundamentals Getters  #########################
    ###########################################################################
    def averageVolume(self):
        try:
            return float(self.fundamentals['average_volume'])
        except:
            return

    def averageVolume2Weeks(self):
        try:
            return float(self.fundamentals['average_volume_2_weeks'])
        except:
            return

    def CEO(self):
        try:
            return self.fundamentals['ceo']
        except:
            return

    def description(self):
        try:
            return self.fundamentals['description']
        except:
            return

    def dividendYield(self):
        try:
            return float(self.fundamentals['dividend_yield'])
        except:
            return

    def headquartersCity(self):
        try:
            return self.fundamentals['headquarters_city']
        except:
            return

    def headquartersState(self):
        try:
            return self.fundamentals['headquarters_state']
        except:
            return

    def high(self):
        try:
            return float(self.fundamentals['high'])
        except:
            return

    def high52Weeks(self):
        try:
            return float(self.fundamentals['high_52_weeks'])
        except:
            return

    def instrumentURL(self):
        try:
            return self.fundamentals['instrument']
        except:
            return

    def low(self):
        try:
            return float(self.fundamentals['low'])
        except:
            return

    def low52Weeks(self):
        try:
            return float(self.fundamentals['low_52_weeks'])
        except:
            return

    def marketCap(self):
        try:
            return float(self.fundamentals['market_cap'])
        except:
            return

    def numberOfEmployees(self):
        try:
            return int(self.fundamentals['num_employees'])
        except:
            return

    def open(self):
        try:
            return float(self.fundamentals['open'])
        except:
            return

    def PERatio(self):
        try:
            return float(self.fundamentals['pe_ratio'])
        except:
            return

    def sector(self):
        try:
            return self.fundamentals['sector']
        except:
            return

    def sharesOutstanding(self):
        try:
            return float(self.fundamentals['shares_outstanding'])
        except:
            return

    def volume(self):
        try:
            return float(self.fundamentals['volume'])
        except:
            return

    def yearFounded(self):
        try:
            dateTimeStr = str(self.fundamentals['year_founded'])
            dateTime = dt.strptime(dateTimeStr, '%Y')
            return dateTime
        except:
            return
    ###########################################################################
    #############################  Quote Getters  #############################
    ###########################################################################
    def adjustedPreviousClose(self):
        try:
            return float(self.quote['adjusted_previous_close'])
        except:
            return

    def askPrice(self):
        try:
            return float(self.quote['ask_price'])
        except:
            return

    def askSize(self):
        try:
            return float(self.quote['ask_size'])
        except:
            return

    def bidPrice(self):
        try:
            return float(self.quote['bid_price'])
        except:
            return

    def bidSize(self):
        try:
            return float(self.quote['bid_size'])
        except:
            return

    def hasTraded(self):
        try:
            return float(self.quote['has_traded'])
        except:
            return

    def lastExtendedHoursTradePrice(self):
        try:
            return float(self.quote['last_extended_hours_trade_price'])
        except:
            return

    def lastTradePrice(self):
        try:
            return float(self.quote['last_trade_price'])
        except:
            return

    def lastTradePriceSource(self):
        try:
            return float(self.quote['last_trade_price_source'])
        except:
            return

    def previousClose(self):
        try:
            return float(self.quote['previous_close'])
        except:
            return

    def previousCloseDate(self):
        try:
            dateTimeStr = self.instrument['previous_close_date']
            dateTime = dt.strptime(dateTimeStr, '%Y-%m-%d')
            return dateTime
        except:
            return

    def tradingHalted(self):
        try:
            return bool(self.quote['trading_halted'])
        except:
            return

    def quoteUpdatedAt(self):
        try:
            dateTimeStr = self.position['updated_at']
            dateTime = dt.strptime(dateTimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
            return dateTime
        except:
            return

    def popularity(self):
        try:
            return int(self.popularity)
        except:
            return

    ###########################################################################
    #############################  Market Getters  ############################
    ###########################################################################
    # TODO: (C) modify Robinhood API to get information about the market that this stock

    ###########################################################################
    ##########################  Analysis Information  #########################
    ###########################################################################
    def percentChange(self):
        lastPrice = self.lastTradePrice()
        previousClose = self.previousClose()
        diff = lastPrice - previousClose
        return (diff/previousClose) * 100


