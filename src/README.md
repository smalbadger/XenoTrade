# :alien: Source Directory :alien:

# In-Depth Description of System Architecture

# To-Do's
* Create a XenoWidget abstract class that all custom widgets will inherit from. This class should:
	* have an 'update' method to fetch data from the user object and spread it to internal widget components appropriately. This should also probably repaint the widget.
* Concurrently fetch as much data as I can from the Robinhood servers. This will require quite a bit of experimentation and research. There also needs to be a simple and clean way to keep track of the threads and manage them (ThreadManager class maybe???).
* record everything that happens during execution in a log. This will make debugging waaaaayyyyy easier hopefully.
