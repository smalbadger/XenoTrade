# :alien: XenoTrade :alien:
A trading and analysis platform like you've never seen before!

### About
XenoTrade is an experimental trading application that utilizes Robinhood's existing infrastructure. As such, each user will have to create a Robinhood account before being able to use this application. The approval process can take quite a bit of time, so I recommend you [create an account](https://signup.robinhood.com/) now. Robinhood was chosen because they offer completely commision-free trading and it is relatively simple to pull the information needed from their servers.

So why would we make essentially a wrapper application around Robinhood's existing framework if they already have a clean and simple website and mobile application? The answer: **Freedom**. By storing data locally, we have should be able to analyze markets, individual stocks, cryptocurrencies, options, etc, however we want. Furthermore, we will have the ability to place trades as if we were using their app directly. XenoTrade makes it very simple to design modularized custom 'widgets' to perform any analysis desired.

Once XenoTrade is stable and well developed, the next goal is to incorporate a trading bot dock where the user could select bots to run either in simulation or in real life. Each bot would have a standardized architecture, but different decision making algorithms making simple to run each of the bots concurrently in the same window in the form of widgets.

### System Requirements
| What    | Version | Where To Get? |
| ------- | ------- | ------------- |
| Robinhood Account | - | [sign up](https://signup.robinhood.com/) |
| Python  | >=3.4   | [download](https://www.python.org/downloads/) *make sure to install pip or pip3 as well |
| Robinhood API | >=1.0.1 | [clone](https://github.com/smalbadger/Robinhood) |
| numpy | latest | sudo pip3 install numpy |
| matplotlib | latest | sudo pip3 install matplotlib |
| PySide2 | latest | sudo pip3 install PySide2 |
NOTE: If you're having problems with multiple Qt binaries, anaconda may be the cause if you have it.

### Installing Robinhood API
1. Open a terminal 
	* I'm assuming you're using a UNIX-based system
1. Navigate to the directory you want the source code to be in (doesn't matter too much though because we'll install it in a few steps)
1. type `git clone https://github.com/smalbadger/Robinhood.git`
1. Navigate into the newly created Robinhood directory
1. type `sudo pip3 install .`
	* Note that if you change a source file from the Robinhood repository, you'll have to retype this for the changes to take effect in the installation directory. 

### Getting Started
1. Go create a Robinhood account [here](https://signup.robinhood.com/).
1. Start XenoTrade by running XenoTrade.py with python3
1. Create an account on XenoTrade by clicking "new user"
1. Enter your Robinhood account information in the fields shown. 
	* Don't worry, the password isn't stored anywhere and you'll only need to do this once.
1. You're in! now you can see some account info.
	* If you look in the "users" directory, you should see your username. This is where personal preferences, downloaded data, etc will be stored on your computer.
