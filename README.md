# TokenGet

TokenGet is a tool to intercept Samsung Pay tokens using a credit card reader and a raspberry zero.

TokenGet device:
Raspberry Zero, Lipo 3.7 V, PowerBoost 1000, Credit Card reader one head, USB adapters, USB WIFI dongle , Mini OTG USB,
Cell phone armband

However, the script does not need any special hardware to be executed.


You must edit the email from hotmail and the password of the account.
To run the *.py after raspberry zero boots up automatically, you have to add a line of code at the end of /etc/profile file: 

sudo nano /etc/profile

go to the end and add:

sudo python ~/TokenGet.py

depending where you saved your TokenGet.py file.

Any questions, contact me at salvador_m_g@msn.com
Twitter: @Netxing
