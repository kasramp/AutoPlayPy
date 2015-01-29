# AutoPlayPy
##Description
The purpose of AutoPlayPy is to automate playing process of Youtube, DailyMotion, LiveStream, Twitch, and Ustream via [LiveStreamer](https://github.com/chrippa/livestreamer).
AutoPlayPy is written in Python 2.7 and it is not tried on Python 3.x. AutoPlayPy is simply traces clipboard content and if any string with the aforementioned stream names found in a clipboard the script automatically launches LiveStreamer and passes the string as input parameter. Therefore, the video will start playing.

##Dependencies
In order to utilize the script LiveStreamer should be installed. For installing it,
### Ubuntu
	```bash
	$ sudo apt-get install python-pip
	$ sudo pip install livestreamer
	```
### CentOS
	```bash
	$ sudo yum install python-pip 
	$ sudo pip instll livestreamer
	```
To AutoPlayPy the following module(s) should be installed:
	* Tkinter
For installing the above module(s),
### Ubuntu
	```bash
	$ sudo apt-get install python-tk
	```
### CentOS
	```bash
	$ sudo yum install 
	```
##How to use
You can run the script with typing
	```bash
	$ python autoPlayPy.py
	```
	Or
	```bash
	$ chmod a+x autPlayPy.py
	$ ./autPlayPy.py
	```
The script accepts the following parameter(s)  
	+ --popup [true/false]  

'true' : shows popup message and ask to terminate current stream if any is playing and start playing the new stream copied to clipboard.  

'false' : automatically terminates the current stream if any is playing and start playing the new stream.  


##Contact
    - kasra@madadipouya.com  
    - kasra_mp@live.com  

	
	

