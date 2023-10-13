import rclpy
import cv2
from rclpy.node import Node
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class Video_get(Node):
    def __init__(self):
        super().__init__('video_subscriber')   ## node name
        self.subsrcriber=self.create_subscription(Image,'camera/image_raw',self.process_data,10)
        ## set for writing and saving the video file
        self.out=cv2.VideoWriter('/home/kanja-koduki/zypher_ws/src/prius_sdc_pkg/videorecord.avi',cv2.VideoWriter_fourcc('M','J','P','G'),30,(1280,720))
        self.bridge=CvBridge()   # converts ros images to opencv data        


    def process_data(self, data):
        frame=self.bridge.imgmsg_to_cv2(data,'bgr8')   # converting the image from the published data to the cv2 format
        self.out.write(frame) # writing the frames to a video
        cv2.imshow("Output",frame)
        cv2.waitKey(1)   # will wait till the image is interpreted


def main():
    rclpy.init()
    image_subsciber=Video_get()
    rclpy.spin(image_subsciber)
    rclpy.shutdown()

if __name__ == "__main__":
    main()