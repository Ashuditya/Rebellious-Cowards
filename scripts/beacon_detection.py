#!/usr/bin/env python
'''
* Team Id : #541
* Author List : Srujan Wankhede, Ashutosh Singh
* Filename: position_hold.py
* Theme: Survey & Rescue (SR)
* Functions: 
	main functions -> check_whether_lit()
	class sr_determine_colors functions ->  __init__(), load_rois(), callback()
* Global Variables:
	None
'''
from __future__ import print_function
import numpy as np
import pickle
import roslib
import sys
import rospy
import cv2
import copy
import os
from survey_and_rescue.msg import SRinfo
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

'''
* Function Name: check_whether_lit()
* Input:	frame -> cv2 frame sequence from the live_camera feed 
 	 	 	x -> center pixel position on x-axis of region of interest
			y -> center pixel position on y-axis of region of interest
* Output:   True -> if beacon is ON in given ROI frame
		    False -> if beacon is OFF in given ROI frame
* Logic:	cv2 frame[x][y] = 255 when it is satisfied by the given colour on pixel position x, y  
*
* Example Call: check_whether_lit(red, 160, 120)
'''
def check_whether_lit(frame, x, y):
  	go = False
	for n in range(x-10,x+11):
		for m in range(y-10,y+11):
			if frame[m][n]==255:
				go = True
	if frame[y][x]==255:
		go = True
					
	return go
	
class sr_determine_colors():
	
	'''
	* Function Name: __init__()
	* Input:	None
	* Output:   initailzes the variables, parameters, publisher, subscriber for edrone class
	* Logic:	initializing for drone at beginning  
	*
	* Example Call: None
	'''
	
	def __init__(self):
		self.bridge = CvBridge()
		self.detect_pub = rospy.Publisher("/detection_info",SRinfo,queue_size=10) 
		self.image_sub = rospy.Subscriber("/usb_cam/image_rect_color",Image,self.callback)
		self.cv_image = None
		self.rect_list = None
		self.yo = SRinfo()
		self.Rescue = []
		self.Medicine = []
		self.Food = []
		self.r = 0
		self.b = 0
		self.g = 0
	
	'''
	* Function Name: load_rois( file_path, 'rect_info.pkl')
	* Input:	file_path -> path of the file to be read i.e ROI file
				rect_info.pkl -> name of file of type .pkl which store data on ROI on which colour detection is to be done
	* Output:   None
	* Logic:	the basic syntax of opening a .pkl file in python script as rb (read as binary type)  
	*
	* Example Call: self.load_rois(self, file_path, 'name.pkl' )
	'''
	
	def load_rois(self, file_path = os.path.join( os.path.dirname(__file__) , 'rect_info.pkl')):
		try:
			with open(file_path , 'rb') as input:
				self.rect_list = pickle.load(input)
		except IOError, ValueError:
				print("File doesn't exist or is corrupted")
	
	
	'''
	* Function Name: call_back(data)
	* Input:	data -> being subscribed on rostopic /usb_cam/image_rect_colour from usb camera
	* Output:   self.yo -> being published on rostopic /detection_info
	* Logic:	ye likh be  
	*
	* Example Call: self.call_back(data) -> gets called whenever something is published by /usb_cam/image_rect_colour
					self.image_sub = rospy.Subscriber("/usb_cam/image_rect_color",Image,self.callback) -> initialized
					
	'''
	
	
	def callback(self,data):
		try:
			self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")  #cv_bridge acts as a convertor from ros image type to open cv type
		except CvBridgeError as e:
			print(e)
		
		'''
		image processing is done in this scripts by hsv method
		following lines define value for masking cv frame for given colour
		'''
		
		#red colour range
		lower_red = np.array([124,83,37], dtype=np.uint8)          
		higher_red = np.array([179,255,255], dtype=np.uint8)
		
		#green colour range
		lower_green = np.array([36,67,55], dtype=np.uint8)
		higher_green = np.array([93,255,255], dtype=np.uint8)
		
		#blue colour range
		lower_blue = np.array([95,96,155], dtype=np.uint8)
		higher_blue = np.array([132,255,255], dtype=np.uint8)
		
		#converting the self.cv_image to HSV colour scale
		hsv_frame = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2HSV)
		
		red = cv2.inRange(hsv_frame, lower_red, higher_red)									#masking the colour red in HSV frame
		red = cv2.medianBlur(red, 31)														#using medianBlur to reduce noise for better accuracy
		
		green = cv2.inRange(hsv_frame, lower_green, higher_green)							#masking the colour green in HSV frame
		green = cv2.medianBlur(green, 15)													#using medianBlur to reduce noise for better accuracy
		
		blue = cv2.inRange(hsv_frame, lower_blue, higher_blue)								#masking the colour blue in HSV frame
		blue = cv2.medianBlur(blue, 15)														#using medianBlur to reduce noise for better accuracy			

		'''
		following code is for implementation of image_processing and and publishing to /detection_info only once when detected
		
		'''
		
		for i in sorted(self.rect_list.keys()):
			x, y = (int(self.rect_list[i][0][0][0])+int(self.rect_list[i][2][0][0]))//2, (int(self.rect_list[i][0][0][1])+int(self.rect_list[i][2][0][1]))//2
			if check_whether_lit(red, x, y) or check_whether_lit(green, x, y) or check_whether_lit(blue, x, y):
				if check_whether_lit(red, x, y):
					if (str(i) in self.Medicine) or (str(i) in self.Food) or (str(i) not in self.Rescue):
						if (str(i) in self.Medicine):
							self.Medicine.remove(str(i))
						if (str(i) in self.Food):
							self.Food.remove(str(i))
						if str(i) not in self.Rescue:
							self.Rescue.append(str(i))
  						print("red " +str(i))
						self.yo.location = str(i)
						self.yo.info = "RESCUE"
						self.detect_pub.publish(self.yo)
				elif check_whether_lit(blue, x, y):
					if (str(i) in self.Rescue) or (str(i) in self.Food) or (str(i) not in self.Medicine):
						if (str(i) in self.Rescue):
							self.Rescue.remove(str(i))
						if (str(i) in self.Food):
							self.Food.remove(str(i))
						if str(i) not in self.Medicine:
							self.Medicine.append(str(i))
  						print("blue " + str(i))
						self.yo.location = str(i)
						self.yo.info = "MEDICINE"
						self.detect_pub.publish(self.yo)
				elif check_whether_lit(green, x, y):
					if (str(i) in self.Rescue) or (str(i) in self.Medicine ) or (str(i) not in self.Food):
						if (str(i) in self.Rescue):
							self.Rescue.remove(str(i))
						if (str(i) in self.Medicine):
							self.Medicine.remove(str(i))
						if str(i) not in self.Food:
							self.Food.append(str(i))
						print("green " + str(i))
						self.yo.location = str(i)
						self.yo.info = "FOOD"
						self.detect_pub.publish(self.yo)
			else:
				if str(i) in self.Rescue:
					self.Rescue.remove(str(i))
				if str(i) in self.Medicine:
					self.Medicine.remove(str(i))
				if str(i) in self.Food:
					self.Food.remove(str(i))

'''
* Function Name: main()
* Input:	None
* Output:   None
* Logic:	None
*
* Example Call: main(sys.argv) 

'''

def main(args):
	rospy.init_node('sr_determine_colors', anonymous=False)
	rate = rospy.Rate(30)						# rate is 30Hz
	s = sr_determine_colors()					
	s.load_rois()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
		cv2.destroyAllWindows()
if __name__ == '__main__':
	main(sys.argv)
