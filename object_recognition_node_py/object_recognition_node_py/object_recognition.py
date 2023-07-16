#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@作者: 王仰旭
@说明: 使用OpenCV进行图像识别并显示识别结果的节点代码, 无发布消息
"""

import rclpy
from rclpy.node import Node
import cv2
import numpy as np                                  # Python数值计算库

lower_red = np.array([0, 90, 128])
upper_red = np.array([180, 255, 255])

def object_detect(image):
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)            # 图像从BGR颜色模型转换为HSV模型
    mask_red = cv2.inRange(hsv_img, lower_red, upper_red)       # 图像二值化
    cv2.imshow("mask_red", mask_red)
    contours, hierarchy = cv2.findContours(mask_red, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)  # 图像中轮廓检测

    for cnt in contours:                # 去除轮廓面积太小的噪声
        if cnt.shape[0] < 150:
            continue
        
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.drawContours(image, [cnt], -1, (0, 0, 255), 2)
        cv2.circle(image, (int(x+w/2), int(y+h/2)), 5, (0, 255, 0), -1)

    cv2.imshow("object", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = Node("object_recognition_node")

    node.get_logger().info("Start Imread...")
    # 因编译后可执行文件在install中，不与图片同文件夹，只能用绝对路径，或把照片复制过去
    image = cv2.imread("/home/wang/my_ws/src/object_recognition_node_py/object_recognition_node_py/apple.jpg")
    object_detect(image)

    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

