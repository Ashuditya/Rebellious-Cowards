#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class sr_determine_rois():
 
  def __init__(self):

    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/usb_cam/image_rect",Image,self.callback)
    self.cv_image = None
  def callback(self,data):
    try:
			self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		except CvBridgeError as e:
			print(e)
		
		self.lower_red = np.array([169,58,15], dtype=np.uint8)
		self.higher_red = np.array([179,255,255], dtype=np.uint8)
		self.lower_green = np.array([59,62,14], dtype=np.uint8)
		self.higher_green = np.array([75,255,255], dtype=np.uint8)
		self.lower_blue = np.array([105,123,82], dtype=np.uint8)
		self.higher_blue = np.array([118,255,255], dtype=np.uint8)
		self.hsv_frame = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2HSV)
		self.red = cv2.inRange(self.hsv_frame, self.lower_red, self.higher_red)
		self.red = cv2.medianBlur(self.red, 31)
		self.green = cv2.inRange(self.hsv_frame, self.lower_green, self.higher_green)
		self.green = cv2.medianBlur(self.green, 15)
		self.blue = cv2.inRange(self.hsv_frame, self.lower_blue, self.higher_blue)
		self.blue = cv2.medianBlur(self.blue, 15)
		self._ = cv2.bitwise_or(self.red, self.green)
		self.mask = cv2.bitwise_or(self._, self.blue)
		self.median = cv2.medianBlur(self.mask,15)


    cv2.imshow("Image window", self.cv_image)
    cv2.waitKey(3)
 
 
def main(args):
  ic = sr_determine_rois()
  rospy.init_node('sr_determine_rois', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
