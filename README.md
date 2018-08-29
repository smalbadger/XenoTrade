# XenoTrade
A trading and analysis platform like you've never seen before!

## System Requirements
This project has a few dependencies, but fortunately most of them can be simply installed using pip (or pip3 depending of your system)
| Package | Version | Where To Get? |
| ------- | ------- | ------------- |
| Robinhood Account | - | [sign up](https://signup.robinhood.com/) |
| Python  | >=3.4   | [download](https://www.python.org/downloads/) * |
| Robinhood API | >=1.0.1 | [clone](https://github.com/smalbadger/Robinhood) |
| numpy | latest | sudo pip3 install numpy |
| matplotlib | latest | sudo pip3 install matplotlib |

Notes:
 * make sure to install pip (or pip3) along with python3
 
### Installing Robinhood API
1. Open a terminal 
	* I'm assuming you're using a UNIX-based system
1. Navigate to the directory you want the source code to be in (doesn't matter too much though because we'll install it in a few steps)
1. type `git clone https://github.com/smalbadger/Robinhood.git`
1. Navigate into the newly created Robinhood directory
1. type `sudo pip3 install .`
	* Note that if you change a source file from the Robinhood repository, you'll have to retype this for the changes to take effect in the installation directory. 


