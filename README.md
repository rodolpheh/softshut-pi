# softshut-pi

Softshut-pi is a systemd service for Raspberry pi based systems using Linux and systemd. It allows you to add a switch on GPIO4 of the Raspberry Pi in order to trigger a software shutdown.
It was originally made for Pi Supply but can work for any system (it's just a push button between GPIO and GND). The difference with the Pi Supply
service that was delivered with the board is that, with Python and RPi.GPIO, we can use interrupt instead of polling thus reducing CPU usage.

## How to use ?

Start by cloning and installing the scripts :

```
git clone https://github.com/rodolpheh/softshut-pi.git  
sudo make install
```

Then you can start the service or enable it on start :

```
sudo systemctl start softshut
sudo systemctl enable softshut
```
Then just press the button and you should see your raspberry gracefully shutting down.
