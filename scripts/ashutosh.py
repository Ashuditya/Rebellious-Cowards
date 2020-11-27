#!/usr/bin/env python
from __future__ import print_function
import roslib
import sys
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import pickle
import imutils
import copy
import numpy as np
import itertools
import os
class sr_determine_rois():

	def __init__(self):

		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("/usb_cam/image_rect",Image,self.image_callback)
		self.img =	 None
	
	# CV_Bridge acts as the middle layer to convert images streamed on rostopics to a format that is compatible with OpenCV
	def image_callback(self, data):
		try:
			self.img = self.bridge.imgmsg_to_cv2(data, "rgb8")
			cv2.imshow("yo",self.img)
		except CvBridgeError as e:
			print(e)


	def detect_rois(self):
		gray_img = self.img
		#gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
		_, threshold = cv2.threshold(gray_img, 90, 255, cv2.THRESH_BINARY)
		c, contours, _= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for cnt in contours:
			approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
			area = cv2.contourArea(cnt)
			if area > 5000 and len(approx) == 4:
				center_x, center_y = (int(approx[3][0][0])+int(approx[1][0][0]))//2,(int(approx[3][0][1])+int(approx[1][0][1]))//2 
				cv2.putText(gray_img, [approx], -1, (0, 255, 0), 5)
				pose.append(approx)
				i += 1
		cv2.imshow("hi",threshold)
		cv2.waitKey(100)

	def sort_rois(self):
		# Add your Code here
		pass
		

	def query_yes_no(self, question, default=None):
		valid = {"yes": True, "y": True, "ye": True,"no": False, "n": False}
		if default is None:
			prompt = " [Y/N]:\t"
		elif default == "yes":
			prompt = " [Y/N]:\t"
		elif default == "no":
			prompt = " [Y/N]:\t"
		else:
			raise ValueError("Invalid default answer: '%s'" % default)

		while True:
			sys.stdout.write(question + prompt)
			choice = raw_input().lower()
			if default is not None and choice == '':
				return valid[default]
			elif choice in valid:
				return valid[choice]
			else:
				sys.stdout.write("\nPlease respond with 'yes' or 'no' ""(or 'y' or 'n').\n")

	def save_rois(self):
		#Add your code here
		kords = dict(zip(block_names, pose))
		with open(cords_path,mode = 'wb') as file:
			pickle.dump(kords, file)
	#You may optionally implement this to display the image as it is displayed in the Figure given in the Problem Statement
	def draw_cell_names(self, img):
		#Add your code here
		pass


def main(args):
	#Sample process flow
	rospy.init_node('sr_roi_detector', anonymous=False)
	r = sr_determine_rois()
	r.detect_rois()
	r.save_rois()
	cv2.destroyAllWindows()

	#try:
	#	rospy.init_node('sr_roi_detector', anonymous=False)
	#	r =	sr_determine_rois()
	#	while True:
	#		if r.img is not None:
	#			r.detect_rois()
	#			if('''No of cells detected is not 36'''):
	#				new_thresh_flag = r.query_yes_no("36 cells were not detected, do you want to change ##Enter tweaks, this is not necessary##?")
	#				
	#				if(new_thresh_flag):
	#					#Change settings as per your desire
	#			
	#				else:
	#					continue
	#			else:
	#				satis_flag = r.query_yes_no("Are you satisfied with the currently detected ROIs?")
	#				if(satis_flag):
	#					r.sort_rois()
	#					r.save_rois()
	#					cv2.destroyAllWindows()
	#					break
	#				else:
	#					continue
	#					#Change more settings
	#	r.draw_cell_names(r.img) # Again, this is optional
	#except KeyboardInterrupt:
	#	cv2.destroyAllWindows()

if __name__ == '__main__':
	
	block_names = ['F6', 'E6', 'D6', 'C6', 'B6', 'A6', 'F5', 'E5', 'D5', 'C5', 'B5', 'A5', 'F4', 'E4', 'D4', 'C4', 'B4', 'A4', 'F3', 'E3', 'D3', 'C3', 'B3', 'A3', 'A2', 'F2', 'E2', 'D2', 'C2', 'B2', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1']
	i=0
	pose = []
	#path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "map.png")
	cords_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rect_info.pkl")

	main(sys.argv)