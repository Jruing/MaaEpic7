#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自定义动作模块
"""

import time
import random


def smart_click(context, task_name, custom_param, box):
    """智能点击 - 带随机偏移"""
    if not box:
        return False
    
    center_x = box[0] + box[2] // 2
    center_y = box[1] + box[3] // 2
    
    if custom_param.get("random_offset", False):
        center_x += random.randint(-10, 10)
        center_y += random.randint(-10, 10)
    
    context.controller.click(center_x, center_y)
    return True


def batch_click(context, task_name, custom_param, box):
    """批量点击"""
    count = custom_param.get("count", 1)
    delay = custom_param.get("delay", 500)
    
    for i in range(count):
        if box:
            x = box[0] + box[2] // 2 + random.randint(-5, 5)
            y = box[1] + box[3] // 2 + random.randint(-5, 5)
            context.controller.click(x, y)
            time.sleep(delay / 1000)
    
    return True


def swipe_with_delay(context, task_name, custom_param, box):
    """带延迟的滑动"""
    begin = custom_param.get("begin", [640, 500])
    end = custom_param.get("end", [640, 200])
    duration = custom_param.get("duration", 300)
    
    context.controller.swipe(begin[0], begin[1], end[0], end[1], duration)
    time.sleep(0.5)
    
    return True


# 邮件动作
def claim_mail_with_verify(context, task_name, custom_param, box):
    """带验证的邮件领取"""
    if not box:
        return False
    
    center_x = box[0] + box[2] // 2 + random.randint(-5, 5)
    center_y = box[1] + box[3] // 2 + random.randint(-5, 5)
    
    context.controller.click(center_x, center_y)
    time.sleep(0.5)
    
    return True


# 商店动作
def claim_free_item(context, task_name, custom_param, box):
    """领取免费商品"""
    if not box:
        return False
    
    center_x = box[0] + box[2] // 2
    center_y = box[1] + box[3] // 2
    
    context.controller.click(center_x, center_y)
    time.sleep(0.5)
    
    return True


# 圣域动作
def claim_sanctuary_reward(context, task_name, custom_param, box):
    """圣域奖励领取"""
    if not box:
        return False
    
    center_x = box[0] + box[2] // 2
    center_y = box[1] + box[3] // 2
    
    context.controller.click(center_x, center_y)
    time.sleep(0.5)
    
    return True


# 讨伐动作
def select_hunt_type(context, task_name, custom_param, box):
    """选择讨伐类型"""
    hunt_type = custom_param.get("hunt_type", "水")
    
    positions = {
        "水": [200, 300],
        "木": [400, 300],
        "火": [600, 300],
        "光": [800, 300],
        "暗": [1000, 300]
    }
    
    x, y = positions.get(hunt_type, [200, 300])
    x += random.randint(-10, 10)
    y += random.randint(-10, 10)
    
    context.controller.click(x, y)
    time.sleep(0.5)
    
    return True


# 日常动作
def claim_daily_reward(context, task_name, custom_param, box):
    """日常奖励领取"""
    if not box:
        return False
    
    center_x = box[0] + box[2] // 2
    center_y = box[1] + box[3] // 2
    
    context.controller.click(center_x, center_y)
    time.sleep(0.5)
    
    return True


# 注册所有动作
def register_actions(resource):
    """注册所有自定义动作"""
    actions = {
        "smart_click": smart_click,
        "batch_click": batch_click,
        "swipe_with_delay": swipe_with_delay,
        "claim_mail_with_verify": claim_mail_with_verify,
        "claim_free_item": claim_free_item,
        "claim_sanctuary_reward": claim_sanctuary_reward,
        "select_hunt_type": select_hunt_type,
        "claim_daily_reward": claim_daily_reward,
    }
    
    for name, action in actions.items():
        resource.register_custom_action(name, action)
    
    print(f"已注册 {len(actions)} 个自定义动作")