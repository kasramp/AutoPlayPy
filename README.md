# AutoPlayPy
##Description
The purpose of AutoPlayPy is to automate playing process of Youtube, DailyMotion, LiveStream, Twitch, and Ustream via LiveStreamer.
AutoPlayPy is written in Python. It is simply traces clipboard content and if any string with the aforementioned stream names found in a clipboard it automatically launch LiveStreamer and pass the string as input parameter. Therefore, the video will start playing.

##Dependencies
In order to utilize the script LiveStreamer should be installed. For installing it,
### Ubuntu
	```bash
	$ sudo apt-get install python-pip
	$ sudo pip install livestreamer
### CentOS
	```bash
	$ sudo yum install python-pip 
	$ sudo pip instll livestreamer

