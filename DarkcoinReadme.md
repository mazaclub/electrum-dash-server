Darkcoin Electrum Keep it Simple Instructions
=============================================

Darkcoind
-----------

* darkcoin.conf must have txindex=1 in it. After updating, you'll need to reindex.

electrum-start-server
---------------------

* Create a directory /var/electrum-start-server 
	$sudo mkdir /var/electrum-start-server
* Chown the directory to the user you'll run the electrum-start-server as. 
	$sudo chown user:user /var/electrum-start-server
* Install darkcoin_hash located in src/darkcoin_hash 
	$cd src/darkcoin_hash && sudo python setup.py install
*Install electrum-start-server
	$sudo ./configure
	$sudo python setup.py install 

electrum-start-server configuration
---------------------------------

*By default, the configuration file is located in /etc/electrum-start.conf
*By defualt, the logfile is located in /var/log/electrum-start.log 
*Check for both these files before attempting to run electrum-start-server.
	If they do not exist, create them and chown them to the user you'll be using.




 


 
