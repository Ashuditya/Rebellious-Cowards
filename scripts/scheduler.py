#!/usr/bin/env python
'''
* Team Id : #541
* Author List : Srujan Wankhede, Ashutosh Singh
* Filename: scheduler.py
* Theme: Survey & Rescue (SR)
* Functions: 
	main functions -> main(args)
	class sr_determine_colors functions ->  __init__(), detection_callback(), serviced_callback(), decision_maker(self), on_board_check(self,msg)
* Global Variables: None
'''
from __future__ import print_function
import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from survey_and_rescue.msg import *

class sr_scheduler():
	'''
	* Function Name: __init__()
	* Input:	None
	* Output:   initializes all the parameters including sun=bscribing to /detection_info , /serviced_info, total food and medicine packages and patient on board 
	* Logic:	initializes
	*
	* Example Call: None
	'''
	def __init__(self):
		rospy.Subscriber('/detection_info',SRInfo,self.detection_callback)	
		rospy.Subscriber('/serviced_info',SRInfo,self.serviced_callback)
		self.decision_pub = rospy.Publisher('/decision_info',SRInfo,queue_size=4)
		self.stop_script = rospy.Publisher('/stop_info',String,queue_size=4 )
		self.decided_msg = SRInfo()
		self.queue_location = []
		self.queue_info = []
		self.index = 0
		self.fob = 3
		self.mob = 3
		self.pob = False
		self.service_in_progress = False
		self.early = SRInfo()
		self.late = SRInfo()
	
	'''
	* Function Name: self.detection_callback(msg)
	* Input:	msg (type SRInfo from survey_and_rescue.msg)
	* Output:   gets the number of detection by subscribing to /detection_info topic and makes decision whether the drone should service on the detected beacon or not
	* Logic:	rostopic subscription
	*
	* Example Call: None
	'''
	
	def detection_callback(self, msg):
		
		#self.late.location = self.early.location
		#self.late.info = self.early.info

		self.early.location = msg.location
		self.early.info = msg.info
		
		self.decision_maker()
	
	'''
	* Function Name: self.serviced_callback(msg)
	* Input:	msg (type SRInfo from survey_and_rescue.msg)
	* Output:   gets the status of service whether 'SUCCESS' or 'FAILURE' by subscribing to /serviced_info topic as well as makes necessary changes in self.fob ,self.mob and self.pob after succeddful service
	* Logic:	rostopic subscription
	*
	* Example Call: None
	'''
	
	def serviced_callback(self,msg):
		
		if msg.location == self.decided_msg.location :	
			if msg.info == 'SUCCESS' :
				if self.decided_msg.info == 'RESCUE':
					self.pob = True
				elif self.decided_msg.info == 'FOOD' :
					self.fob -= 1
				elif self.decided_msg.info == 'MEDICINE' :
					self.mob -= 1
			if msg.location == 'E4' and msg.info == 'SUCCESS' :
				self.pob = False
				self.fob = 3
				self.mob = 3	
				
			self.service_in_progress = False
			
			#self.decision_maker()

	'''
	* Function Name: self.decision_maker()
	* Input:	None
	* Output:   if no service is in progress then it decides what to service next to drone and publishes to topic /decision_info
	* Logic:	rostopic subscription
	*
	* Example Call: None
	'''
		
	
	def decision_maker(self):
		if not self.service_in_progress :
			
			if self.pob == True or (self.fob == 0 and self.mob == 0) :
				self.decided_msg.location = 'E4'
				self.decided_msg.info = 'BASE'
			
			elif self.on_board_check(self.early) and self.early.location != 'A6' and self.early.location != 'A2' and self.early.location != 'E2'  :
				self.decided_msg.location = self.early.location
				self.decided_msg.info = self.early.info
			elif self.fob == 0 or self.mob == 0 :
				self.decided_msg.location = 'E4'
				self.decided_msg.info = 'BASE'
			else :
				return
			
			print("fob =" ,self.fob)
			print("mob =",self.mob)
			print("pob =" ,self.pob)
		
			self.decision_pub.publish(self.decided_msg)
			print("decision is "+ self.decided_msg.location +" "+ self.decided_msg.info)
			self.service_in_progress = True
	'''
	* Function Name: on_board_check()
	* Input:	msg (type SRInfo from survey_and_rescue.msg)
	* Output:   return true when input msg can be serviced
	* Logic:	if fob is not 0 then 'FOOD' msg can be serviced similarly others
	*
	* Example Call: self.on_board_check(msg)
	'''	
	
	def on_board_check(self,msg):

		if msg.info == 'FOOD' :
			return (self.fob != 0)
		elif msg.info == 'MEDICINE' :
			return (self.mob != 0) 
		elif msg.info == 'RESCUE':
			return (not self.pob)
	
	def shutdown_hook(self):
		pass


'''
* Function Name: main()
* Input:	None
* Output:   None
* Logic:	None
*
* Example Call: main(sys.argv) 

'''

def main(args):
	
	sched = sr_scheduler()
	rospy.init_node('sr_scheduler', anonymous=False)
	rospy.on_shutdown(sched.shutdown_hook)
	rate = rospy.Rate(30)
	while not rospy.is_shutdown():
		rate.sleep()

if __name__ == '__main__':
    main(sys.argv)