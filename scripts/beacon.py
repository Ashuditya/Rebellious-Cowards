#!/usr/bin/env python
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

def emptyFunction():
    pass


class sr_determine_colors():
 
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
		self.cap = None
		self.r = 0
		self.b = 0
		self.g = 0


  	def load_rois(self, file_path = os.path.join( os.path.dirname(__file__) , 'rect_info.pkl')):
  		try:
			with open(file_path , 'rb') as input:
  				self.rect_list = pickle.load(input)
  		except IOError, ValueError:
  			print("File doesn't exist or is corrupted")
  
  	def callback(self,data):
        self.cap = self.bridge.imgmsg_to_cv2(data, "bgr8")
        windowsname = "FuckYouuuuuuuuuuuuuuuuuuuuu"
        cv2.namedWindow(windowsname)
        cv2.createTrackbar("hr", windowsname,0,179,emptyFunction)
        cv2.createTrackbar("sr", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("vr", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("Hr", windowsname,0,179,emptyFunction)
        cv2.createTrackbar("Sr", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("Vr", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("hb", windowsname,0,179,emptyFunction)
        cv2.createTrackbar("sb", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("vb", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("Hb", windowsname,0,179,emptyFunction)
        cv2.createTrackbar("Sb", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("Vb", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("hg", windowsname,0,179,emptyFunction)
        cv2.createTrackbar("sg", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("vg", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("Hg", windowsname,0,179,emptyFunction)
        cv2.createTrackbar("Sg", windowsname,0,255,emptyFunction)
        cv2.createTrackbar("Vg", windowsname,0,255,emptyFunction)
        while(1):
            
            hr = cv2.getTrackbarPos("hr", windowsname)
            sr = cv2.getTrackbarPos("sr", windowsname)
            vr = cv2.getTrackbarPos("vr", windowsname)
            Hr = cv2.getTrackbarPos("Hr", windowsname)
            Sr = cv2.getTrackbarPos("Sr", windowsname)
            Vr = cv2.getTrackbarPos("Vr", windowsname)
            hb = cv2.getTrackbarPos("hb", windowsname)
            sb = cv2.getTrackbarPos("sb", windowsname)
            vb = cv2.getTrackbarPos("vb", windowsname)
            Hb = cv2.getTrackbarPos("Hb", windowsname)
            Sb = cv2.getTrackbarPos("Sb", windowsname)
            Vb = cv2.getTrackbarPos("Vb", windowsname)
            hg = cv2.getTrackbarPos("hg", windowsname)
            sg = cv2.getTrackbarPos("sg", windowsname)
            vg = cv2.getTrackbarPos("vg", windowsname)
            Hg = cv2.getTrackbarPos("Hg", windowsname)
            Sg = cv2.getTrackbarPos("Sg", windowsname)
            Vg = cv2.getTrackbarPos("Vg", windowsname)

            _, frame = self.cap.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            lower_green = np.array([hg,sg,vg], dtype=np.uint8)
            upper_green = np.array([Hg,Sg,Vg], dtype=np.uint8)

            lower_red = np.array([hr,sr,vr], dtype=np.uint8)
            upper_red = np.array([Hr,Sr,Vr], dtype=np.uint8)

            lower_blue = np.array([hb,sb,vb], dtype=np.uint8)
            upper_blue = np.array([Hb,Sb,Vb], dtype=np.uint8)

            red = cv2.inRange(hsv_frame, lower_red, upper_red)
            green = cv2.inRange(hsv_frame, lower_green, upper_green)
            blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)
            
            mask1 = cv2.bitwise_or(red, blue)
            mask2 = cv2.bitwise_or(mask1, green)
            median = cv2.medianBlur(mask2, 15)

            cv2.imshow("median boi", median)
            cv2.imshow("frame", frame)
            if cv2.waitKey(5)==27:
                self.cap.release()
                cv2.destroyAllWindows()
                break
        
def main(args):
	rospy.init_node('sr_determine_colors', anonymous=False)
	rate = rospy.Rate(30)
	s = sr_determine_colors()
	s.load_rois()
	try:
		rospy.spin()
	except KeyboardInterrupt:
		print("Shutting down")
	cv2.destroyAllWindows()
if __name__ == '__main__':

    main(sys.argv)