#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自定义识别模块
"""

import cv2
import numpy as np


def color_based_recognition(context, image, roi, custom_param):
    """基于颜色的识别"""
    if isinstance(image, bytes):
        nparr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = image
    
    if roi and len(roi) == 4:
        x, y, w, h = roi
        img = img[y:y+h, x:x+w]
    
    lower = custom_param.get("lower", [0, 0, 0])
    upper = custom_param.get("upper", [255, 255, 255])
    
    lower = np.array(lower)
    upper = np.array(upper)
    mask = cv2.inRange(img, lower, upper)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    results = []
    min_area = custom_param.get("min_area", 100)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area >= min_area:
            x, y, w, h = cv2.boundingRect(contour)
            results.append([x, y, w, h])
    
    return results


def template_with_rotation(context, image, roi, custom_param):
    """带旋转的模板匹配"""
    if isinstance(image, bytes):
        nparr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = image
    
    template_path = custom_param.get("template_path")
    if not template_path:
        return []
    
    template = cv2.imread(template_path)
    if template is None:
        return []
    
    angles = custom_param.get("angles", [0, 90, 180, 270])
    threshold = custom_param.get("threshold", 0.7)
    
    results = []
    
    for angle in angles:
        if angle != 0:
            h, w = template.shape[:2]
            center = (w // 2, h // 2)
            matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated = cv2.warpAffine(template, matrix, (w, h))
        else:
            rotated = template
        
        result = cv2.matchTemplate(img, rotated, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= threshold)
        
        for pt in zip(*locations[::-1]):
            h, w = rotated.shape[:2]
            results.append([int(pt[0]), int(pt[1]), w, h])
    
    return results


# 注册所有识别器
def register_recognitions(resource):
    """注册所有自定义识别器"""
    recognitions = {
        "color_based": color_based_recognition,
        "template_with_rotation": template_with_rotation,
    }
    
    for name, recognition in recognitions.items():
        resource.register_custom_recognition(name, recognition)
    
    print(f"已注册 {len(recognitions)} 个自定义识别器")