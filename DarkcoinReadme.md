Darkcoin Electrum Keep it Simple Instructions
=============================================

Darkcoind
-----------

* darkcoin.conf must have txindex=1 in it. After updating, you'll need to reindex.

electrum-dash-server
---------------------

* Create a directory /var/electrum-dash-server 
	$sudo mkdir /var/electrum-dash-server
* Chown the directory to the user you'll run the electrum-dash-server as. 
	$sudo chown user:user /var/electrum-dash-server
* Install darkcoin_hash located in src/darkcoin_hash 
	$cd src/darkcoin_hash && sudo python setup.py install
*Install electrum-dash-server
	$sudo ./configure
	$sudo python setup.py install 

electrum-dash-server configuration
---------------------------------

*By default, the configuration file is located in /etc/electrum-dash.conf
*By defualt, the logfile is located in /var/log/electrum-dash.log 
*Check for both these files before attempting to run electrum-dash-server.
	If they do not exist, create them and chown them to the user you'll be using.




 


 
