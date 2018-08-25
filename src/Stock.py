from datetime import datetime as dt

class Stock:
	def __init__(self, t, pos=None, ins=None):
		'''
		Params: 
			- The Robinhood Object of the logged in user
			- The Positions dictionary returned from 
			  Robinhood.securities_owned()['results'][index] (if security is owned)
			- The instrument URL of the stock (not needed if security is owned)
		'''
		self.trader = t
		self.position = pos
		self.instrument = None
		self.fundamentals = None
		
		if ins:
			self.instrument = t.instrument(ins)
			self.fundamentals = t.fundamentals(url=self.instrument['fundamentals'])


	def updateAllProperties(self):
		if self.position:
			'''Figure out how to update the position'''
			pass
			
		self.instrument = self.trader.instrument(self.instrumentURL())
		self.fundamentals = self.trader.fundamentals(self.fundamentalsURL())
		
		
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
			
	def createdAt(self, typeD='str', fmt='%H:%M:%S.%.2f %b %d, %Y'):
		try:
			dateTimeStr = self.position['created_at']
			dateTime = dt.strptime(dateTimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
			
			if typeD == 'str':
				return dateTime.strftime(fmt)
			elif typeD == 'datetime':
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
			
	def updatedAt(self, typeD='str', fmt='%H:%M:%S.%.2f %b %d, %Y'):
		try:
			dateTimeStr = self.position['updated_at']
			dateTime = dt.strptime(dateTimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
			if typeD == 'str':
				return dateTime.strftime(fmt)
			elif typeD == 'datetime':
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
			
	def listDate(self, typeD='str', fmt='%b %d, %Y'):
		try:
			dateTimeStr = self.instrument['list_date']
			dateTime = dt.strptime(dateTimeStr, '%Y-%m-%d')
			if typeD == 'str':
				return dateTime.strftime(fmt)
			elif typeD == 'datetime':
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
			
	def dividentYield(self):
		try:
			return float(self.fundamentals['dividend_yield'])
		except:
			return
			
	def headquarters_city(self):
		try:
			return self.fundamentals['headquarters_city']
		except:
			return
			
	def headquarters_state(self):
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
			
	def yearFounded(self, typeD='str', fmt='%Y'):
		try:
			return self.
			dateTimeStr = self.fundamentals['yearFounded']
			dateTime = dt.strptime(dateTimeStr, '%Y')
			if typeD == 'str':
				return dateTime.strftime(fmt)
			elif typeD == 'datetime':
				return dateTime
		except:
			return
			
	###########################################################################
	#############################  Market Getters  ############################
	###########################################################################
	''' 
		TODO: 
		add to Robinhood API to get information about the market that this stock
	'''
	
