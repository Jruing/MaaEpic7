#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第七史诗自动化助手 - MaaFramework 版本
基于 MaaPracticeBoilerplate 模板
"""

import os
import sys
from pathlib import Path

# 添加 MaaFramework 路径
try:
    from MaaFramework import (
        MaaTasker,
        MaaResource,
        MaaController,
        MaaAdbController,
        MaaCustomRecognition,
        MaaCustomAction,
    )
except ImportError:
    print("错误: 未安装 MaaFramework")
    print("请运行: pip install MaaFw")
    sys.exit(1)


class EpicSevenAgent:
    """第七史诗自动化助手"""
    
    def __init__(self, resource_path: str = None):
        """初始化"""
        # 资源路径
        if resource_path is None:
            self.resource_path = Path(__file__).parent.parent / "assets" / "resource"
        else:
            self.resource_path = Path(resource_path)
        
        # 组件
        self.tasker = None
        self.resource = None
        self.controller = None
        
        print(f"资源路径: {self.resource_path}")
    
    def init_adb_controller(self, adb_path: str, address: str):
        """初始化 ADB 控制器"""
        print(f"正在连接设备: {address}")
        
        self.controller = MaaAdbController(
            adb_path=adb_path,
            address=address,
            screencap_methods=0,
            input_methods=0,
            config={},
            agent_path=None
        )
        
        self.controller.post_connection()
        self.controller.wait()
        
        if self.controller.connected:
            print("设备连接成功")
            return True
        else:
            print("设备连接失败")
            return False
    
    def load_resource(self):
        """加载资源"""
        print("正在加载资源...")
        
        self.resource = MaaResource()
        resource_id = self.resource.post_bundle(str(self.resource_path))
        self.resource.wait(resource_id)
        
        if self.resource.loaded:
            print("资源加载成功")
            return True
        else:
            print("资源加载失败")
            return False
    
    def init_tasker(self):
        """初始化任务器"""
        if not self.resource or not self.controller:
            print("错误: 请先初始化资源和控制器")
            return False
        
        self.tasker = MaaTasker()
        self.tasker.bind(self.resource, self.controller)
        
        print("任务器初始化成功")
        return True
    
    def register_custom_actions(self):
        """注册自定义动作"""
        # 导入自定义动作
        from my_action import register_actions
        register_actions(self.resource)
        print("自定义动作注册成功")
    
    def run_task(self, entry: str = "Main"):
        """运行任务"""
        if not self.tasker:
            print("错误: 请先初始化任务器")
            return False
        
        print(f"开始执行任务: {entry}")
        task_id = self.tasker.post_task(entry)
        self.tasker.wait(task_id)
        
        print("任务执行完成")
        return True
    
    def destroy(self):
        """销毁资源"""
        if self.tasker:
            self.tasker.destroy()
        if self.resource:
            self.resource.destroy()
        if self.controller:
            self.controller.destroy()
        print("资源已释放")


def main():
    """主函数"""
    print("=" * 50)
    print("第七史诗自动化助手")
    print("=" * 50)
    
    agent = EpicSevenAgent()
    
    config = {
        "adb_path": "adb",  # 或完整路径
        "address": "127.0.0.1:5555"
    }
    
    try:
        if not agent.init_adb_controller(config["adb_path"], config["address"]):
            return
        
        if not agent.load_resource():
            return
        
        if not agent.init_tasker():
            return
        
        agent.register_custom_actions()
        agent.run_task("Main")
        
    except KeyboardInterrupt:
        print("\n用户中断")
    finally:
        agent.destroy()


if __name__ == "__main__":
    main()