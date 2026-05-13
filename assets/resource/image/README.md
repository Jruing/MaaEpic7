# 图片素材说明

此目录用于存放识别用的图片素材。

## 目录结构

```
image/
├── main_menu/     # 主界面相关按钮
│   ├── home.png           # 主界面标识
│   └── battle_btn.png     # 战斗入口按钮
│
├── battle/        # 战斗相关
│   ├── start_btn.png      # 开始战斗按钮
│   ├── auto_btn_off.png   # 自动战斗关闭状态
│   ├── auto_btn_on.png    # 自动战斗开启状态
│   ├── victory.png        # 胜利标识
│   └── continue_btn.png   # 继续按钮
│
├── reward/        # 奖励相关
│   └── confirm_btn.png    # 确认领取按钮
│
├── stage/         # 关卡选择
│   └── select.png         # 关卡选择按钮
│
├── hunt/          # 讨伐副本
│   └── select.png         # 讨伐选择按钮
│
└── abyss/         # 深渊副本
    └── select.png         # 深渊选择按钮
```

## 图片要求

1. **分辨率**: 必须是 720p 截图裁剪
2. **格式**: PNG 格式（无损）
3. **内容**: 只包含目标元素，尽量去除背景干扰

## 截图方法

### 模拟器截图

1. 将模拟器分辨率设置为 720p (1280x720)
2. 使用模拟器自带截图功能
3. 用图片编辑工具裁剪目标区域

### ADB 截图

```bash
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png
```

## 注意事项

- 按钮图片应包含完整的按钮区域
- 避免包含动态内容（如数字、时间）
- 对于可能有变化的元素，考虑使用 OCR 识别
