#!/usr/bin/python
import subprocess;
import time;
import os;
import sys;
import signal;
import tkMessageBox;
from Tkinter import Tk;
def isStream(str1):
	try:
		list = ["youtube.com","dailymotion.com","livestream.com","twitch.tv","ustream.tv"];
		for strtmp in list:
			if strtmp in str1.lower():
				return True;
	except Exception,ex:
		print ex;
		return None;
def autoPlay(str2):
	try:
		r = Tk();
		r.withdraw();
		str1 = r.clipboard_get();
		if isStream(str1) and str1 != str2:
			return str1;
		else:
			return;
	except Exception, ex:
		print ex;
		return None;
def runPlayer(strX):
	try:
		childprocess = subprocess.Popen(["livestreamer",strX,"best"]);
		return childprocess;
	except Exception,ex:
		print ex;
		return None;
def execute(showPopup):
	try:
		str2 = autoPlay("");
		str3 = autoPlay("");
		p = "";
		while(1):
			if str2 != None:
				str3 = str2;
			str2 = autoPlay(str3);
			if str2 != None:
				str4 = str2;
				print str4;	
				#p = runPlayer(str4);
				if(p == ""):
					p = runPlayer(str4);
				else:
					if(showPopup):
						if(tkMessageBox.askyesno("Next Video", "Do you want to close this video and proceed with next?")):
							p.terminate();
							p = runPlayer(str4);
					else:
							p.terminate();
							p = runPlayer(str4);
			print str2;
			time.sleep(1);
	except Exception,ex:
		print ex;
	finally:
		return;
	
def main():
	showPopup = "";
	if len(sys.argv) > 1:
		if sys.argv[1] in "--popup":
			showPopup = sys.argv[2];
			if showPopup.lower() == "true".lower():
				showPopup = bool(showPopup);
			else:
				showPopup = False;
	execute(showPopup);
	return;

if __name__ == "__main__":
	main();
