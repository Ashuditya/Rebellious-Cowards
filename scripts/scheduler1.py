#!/usr/bin/env python
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

	def __init__(self):
		rospy.Subscriber('/detection_info',SRInfo,self.detection_callback)
		rospy.Subscriber('/serviced_info',SRInfo,self.serviced_callback)
		self.first = True
		self.decision_pub = rospy.Publisher('/decision_info',SRInfo,queue_size=4)
		self.decided_msg = SRInfo()
		self.foodOnboard = 3
		self.medOnboard = 3
		self.patientOnboard = 0
		self.current_lit = SRInfo()
		self.early = SRInfo()
		self.mid = SRInfo()
		self.late = SRInfo()
		self.last_served = SRInfo()
		
	def detection_callback(self, msg):
		
		self.late.location = self.mid.location
		self.late.info = self.mid.info
		
		self.mid.location = self.early.location
		self.mid.info = self.early.info
		
		self.early.location = msg.location
		self.early.info = msg.info
		
		if self.identifier(self.early) :
			self.current_lit.location = self.early.location
			self.current_lit.info = self.early.info
		elif self.identifier(self.mid) :
			self.current_lit.location = self.mid.location
			self.current_lit.info = self.mid.info
		elif self.identifier(self.late) :
			self.current_lit.location = self.late.location
			self.current_lit.info = self.late.info
		
		print("current_lit" + self.current_lit.location + self.current_lit.info)
		if self.first :
			self.first = False
			self.decided_msg.location = self.current_lit.location
			self.decided_msg.info = self.current_lit.info
			self.decision_pub.publish(self.decided_msg)
			print(self.decided_msg.location + self.decided_msg.info)
			self.last_served.location = self.decided_msg.location
			self.last_served.info = self.decided_msg.info
			
			if self.current_lit.info == 'FOOD' :
				self.foodOnboard -= 1
			elif self.current_lit.info == 'MEDICNINE' :
				self.medOnboard -= 1
			elif self.current_lit.info == 'RESCUE' :
				self.patientOnboard = 1				
	
	def serviced_callback(self, msg):
		# Take appropriate action when either service SUCCESS or FAILIURE is recieved from monitor.pyc
		

		if msg.location == 'E4' and msg.info == 'SUCCESS':						#returned from BASE and replenished
			self.foodOnboard = 3
			self.medOnboard = 3
			self.patientOnboard = 0

		if (self.patientOnboard == 1 or (self.foodOnboard == 0 and self.medOnboard == 0) ) :   #if patient is on board or supplies are empty
			self.current_lit.location = 'E4'
			self.current_lit.info = 'BASE'	
		
		print("last_served "+ self.last_served.info +" "+self.last_served.location )
		print("current_lit "+ self.current_lit.info +" "+self.current_lit.location )
		
		self.decided_msg.location = self.current_lit.location
		self.decided_msg.info = self.current_lit.info
		self.decision_pub.publish(self.decided_msg)
		self.last_served.location = self.decided_msg.location
		self.last_served.info = self.decided_msg.info
		
		if self.decided_msg.info == 'FOOD' :
			self.foodOnboard -= 1
		elif self.decided_msg.info == 'MEDICNINE' :
			self.medOnboard -= 1
		elif self.decided_msg.info == 'RESCUE' :
			self.patientOnboard = 1
	


	
	def identifier(self,sent):
		if sent.info == 'RESCUE' :
			return (self.patientOnboard == 0)
		elif sent.info == 'FOOD':
			return (self.foodOnboard > 0)
		elif sent.info == 'MEDICINE':
			return (self.medOnboard > 0)
		 
	def shutdown_hook(self):
		# This function will run when the ros shutdown request is recieved.
		# For instance, when you press Ctrl+C when this is running
		pass



def main(args):
	
	sched = sr_scheduler()
	rospy.init_node('sr_scheduler', anonymous=False)
	rospy.on_shutdown(sched.shutdown_hook)
	rate = rospy.Rate(30)
	while not rospy.is_shutdown():
		rate.sleep()

if __name__ == '__main__':
    main(sys.argv)