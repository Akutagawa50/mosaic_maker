#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

mosaic_img = None
bridge = CvBridge()

def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def make_mosaic(message):
    global mosaic_img
    # $ find / 2>/dev/null | grep haarcascade_frontalface_default.xml 
    cascade_path = "/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
    
    # Face detection
    img = bridge.imgmsg_to_cv2(message, "bgr8")
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cascade = cv2.CascadeClassifier(cascade_path)
    facedetect = cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeghbors=2, minSize=(30, 30))
    if len(facedetect) > 0:
        # make mosaic
        for x, y, w, h in facedetect:
            mosaic_img = img[y:y + height, x:x + width] = mosaic(img[y:y + height, x:x + width], 0.1)


if __name__=='__main__':
    rospy.init_node('mosaic')
    sub = rospy.Subscriber('cv_camera/image_raw', Image, make_mosaic)
    pub = rospy.Publisher('mosaic_face', Image, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        ros_img = bridge.cv2_to_imgmsg(mosaic_img, "bgr8")
        pub.publish(mosaic_img)
        rate.sleep()
