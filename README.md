# 第七史诗自动化助手

基于 [MaaFramework](https://github.com/MaaXYZ/MaaFramework) 开发的第七史诗自动化脚本。

## 功能特性

- ✅ 日常任务领取
- ✅ 邮件领取
- ✅ 商店免费商品领取
- ✅ 圣域奖励领取
- ✅ 讨伐副本（水/木/火/光/暗）

## 项目结构

```
MaaEpic7/
├── agent/                    # Python 代理
│   ├── main.py              # 主程序入口
│   ├── my_action.py         # 自定义动作
│   └── my_reco.py           # 自定义识别
│
├── assets/                   # 资源文件
│   ├── interface.json       # 接口配置
│   └── resource/
│       ├── pipeline/        # 任务流程 JSON
│       ├── image/           # 图片素材
│       └── model/           # 模型文件
│
├── deps/                     # 依赖工具
│   └── tools/               # Schema 文件
│
└── docs/                     # 文档
```

## 环境要求

- Python 3.8+
- MaaFramework

## 安装

```bash
# 安装 MaaFramework
pip install MaaFw

# 安装依赖
pip install opencv-python numpy
```

## 使用方法

### 1. 准备图片素材

在 `assets/resource/image/` 目录下放置游戏截图裁剪的识别素材。

### 2. 配置设备

修改 `assets/interface.json` 中的 ADB 配置：

```json
{
    "controller": [
        {
            "name": "ADB",
            "type": "Adb",
            "adb_path": "adb",
            "address": "127.0.0.1:5555"
        }
    ]
}
```

### 3. 运行

```bash
cd agent
python main.py
```

## 任务列表

| 任务名称 | 入口节点 | 说明 |
|----------|----------|------|
| 日常任务 | `日常_入口` | 领取日常任务奖励 |
| 邮件领取 | `邮件_入口` | 领取邮件奖励 |
| 商店免费商品 | `商店_入口` | 领取商店免费商品 |
| 圣域奖励 | `圣域_入口` | 领取圣域建筑奖励 |
| 讨伐副本 | `讨伐_入口` | 自动讨伐副本 |
| 水龙讨伐 | `讨伐_水龙_入口` | 水属性讨伐 |
| 木妖讨伐 | `讨伐_木妖_入口` | 木属性讨伐 |
| 火魔像讨伐 | `讨伐_火魔像_入口` | 火属性讨伐 |
| 光暗讨伐 | `讨伐_光暗_入口` | 光属性讨伐 |
| 暗龙讨伐 | `讨伐_暗龙_入口` | 暗属性讨伐 |

## 讨伐属性

| 属性 | 名称 | 主要掉落 |
|------|------|----------|
| 💧 水 | 水龙 | 速度套装、暴击套装 |
| 🌿 木 | 木妖 | 命中套装、抵抗套装 |
| 🔥 火 | 火魔像 | 防御套装、生命套装 |
| ✨ 光 | 光暗 | 吸血套装、毁灭套装 |
| 🌙 暗 | 暗龙 | 复活套装、反击套装 |

## 常用模拟器 ADB 地址

| 模拟器 | 默认地址 |
|--------|----------|
| 蓝叠 | 127.0.0.1:5555 |
| 雷电 | 127.0.0.1:5555 |
| MuMu | 127.0.0.1:7555 |
| 夜神 | 127.0.0.1:62001 |

## 注意事项

1. 图片素材需要是 720p 分辨率的截图裁剪
2. 建议使用稳定的模拟器
3. 首次运行前请确保游戏已打开

## 许可证

MIT License

## 致谢

- [MaaFramework](https://github.com/MaaXYZ/MaaFramework) - 自动化框架
- [MaaPracticeBoilerplate](https://github.com/MaaXYZ/MaaPracticeBoilerplate) - 项目模板