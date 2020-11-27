#!/usr/bin/env python
from __future__ import print_function
import pickle
import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import os

class sr_determine_rois():
 
  def __init__(self):
    self.j = 1
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber("/usb_cam/image_rect",Image,self.image_callback)
    self.cv_image = None
  def image_callback(self,data):
    try:
      self.cv_image = self.bridge.imgmsg_to_cv2(data, "mono8")
    except CvBridgeError as e:
      print(e)

    
    if(self.j == 1):
      img_copy = self.cv_image
      gray_img = cv2.cvtColor(img_copy, cv2.COLOR_BAYER_BG2GRAY)
      #_, threshold = cv2.threshold(gray_img, 40, 50, cv2.THRESH_BINARY)
      threshold = cv2.adaptiveThreshold(gray_img, 200, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
        cv2.THRESH_BINARY, 11, 2)
      c, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
      i = 0
      for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
        area = cv2.contourArea(cnt)
        if area > 4000 and len(approx)==4:
          center_x, center_y = (int(approx[3][0][0])+int(approx[1][0][0]))//2, (int(approx[3][0][1])+int(approx[1][0][1]))//2
          cv2.putText(img_copy,block_names[i], (center_x, center_y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255))
          cv2.drawContours(img_copy, [approx], -1, (0, 255, 0), 5)
          pose.append(approx)
          i+=1
      kords = dict(zip(block_names, pose))
      with open(cords_path, mode='wb') as file:
        pickle.dump(kords, file)
      self.j += 1
      print("File recorded successfully")

      #cv2.imshow("Detected ROIs", threshold) #A copy is chosen because self.img will be continuously changing due to the callback function
      cv2.imshow("Detected ROIs", img_copy)
      cv2.waitKey(0)
      cv2.destroyAllWindows()
      #print("detect rois")
  
      
def main(args):
  r = sr_determine_rois()
# r.detect_rois()
# r.save_rois()
  rospy.init_node('sr_determine_rois', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
    cv2.destroyAllWindows()

if __name__ == '__main__':
    block_names = ['A6','B6','C6','D6','E6','F6','A5','B5','C5','D5','E5','F5','A4','B4','C4','D4','E4','F4','A3','B3','C3','D3','E3','F3','A2','B2','C2','D2','E2','F2','A1','B1','C1','D1','E1','F1']
    i=0

    pose = []
    #path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "map.png")
    cords_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "rect_info.pkl")
    
    main(sys.argv)