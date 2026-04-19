# Microbit-Distributed-Gimbal
A distributed 3-node bionic robot system with 2-DOF gimbal and emotional OLED display.
# 🤖 Bionic Companion Robot / 分布式仿生交互机器人

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Micro:bit](https://img.shields.io/badge/Platform-Micro%3Abit-green.svg)](https://microbit.org/)

🌍 Read this in: [English](#english) | [中文](#中文)

<p align="center">
  <img src="demo.gif" alt="Bionic Robot Demonstration" width="600px">
</p>

---

<h2 id="english">🇬🇧 English</h2>

A low-cost, high-performance distributed bionic interactive robot powered by three BBC Micro:bits. I independently designed this full-stack system to translate human hand gestures into real-time, perfectly synchronized mechanical movements and dynamic facial expressions.

> **"Curing cheap hardware with smart algorithms."** — The core philosophy of this solo project is to use mathematical optimization (Expo curves, Low-Pass Filters, Lerp animations) to make budget MG90S servos perform with industrial-grade smoothness.

### 🌟 Key Features
* **Algorithm-Driven Stabilization:** Implements RC-grade **Expo mixing curves** and **First-Order Low-Pass Filters (LPF)** to completely eliminate hardware jitter.
* **Zero-Latency 3D Tracking:** Uses `math.atan2` for full 360-degree spatial gravity vector calculation, avoiding gimbal lock and value inversion.
* **Bionic OLED Morphing Engine:** A custom 6-parameter rendering engine replaces static images. Features organic smooth transitions (Lerp), random bionic Saccades (eye twitches), and rapid blinking logic.
* **One-Click Calibration:** Instant zero-point baseline setup with a single button press.

### 🛠 Hardware Architecture
A distributed 3-node architecture ensuring zero-latency processing via high-frequency Radio sync:
1. **Node B (The Brain):** Handheld sensor. Calculates 3D vectors and applies LPF/Expo filters.
2. **Node A (The Body):** 2-DOF Gimbal. Drives physical movement using a custom **Silent PWM** logic to prevent electrical humming.
3. **Node C (The Face):** OLED Display. Independently computes and renders morphological expressions.

## 🛒 Bill of Materials (BOM)

This project consists of three independent nodes, each with a specific power strategy to balance high-current demands and portability.

| Component | Qty | Notes |
| :--- | :---: | :--- |
| **BBC Micro:bit** | 3 | Main controllers for Node A, B, and C (V1/V2). |
| **IO Expansion Board** | 2 | For Node A (Servos) and Node C (OLED). |
| **MG90S Servo** | 2 | Metal gear servos for the 2-DOF gimbal (Node A). |
| **SSD1306 OLED Display** | 1 | 0.96" I2C interface (128x64) for Node C. |
| **USB Cable** | 1 | Power source for Node A (High current for servos). |
| **3.7V LiPo Battery** | 1 | 500mAh JST-connector battery for Node B. |
| **3V AAA Battery Box** | 1 | 2-cell battery holder for Node C. |
| **Dupont Wires** | 1 Set | Female-to-Female jumpers for I2C and servos. |

### 🔌 Wiring Guide

#### **Node A: Actuator Controller**
* **Power:** Powered via USB cable (for stable servo operation).
* **Servos:** X-axis (Pitch) to **P0**, Y-axis (Roll) to **P1** on the expansion board.

#### **Node B: Handheld Sensor**
* **Power:** 3.7V LiPo battery plugged into the Micro:bit JST port.
* **Wiring:** No external wiring required (uses built-in accelerometer).

#### **Node C: Display Node**
* **Power:** 3V (2x AAA) battery box connected to expansion board pins.
* **OLED:** **SCL** to **P19**, **SDA** to **P20**, **VCC** to **3V3**, **GND** to **GND**.

### 📂 Directory Structure

```text
Microbit-Distributed-Gimbal/
├── node_a_actuator.py     # Node A: Actuator (Silent PWM & Motion Smoothing)
├── node_b_sensor.py       # Node B: Sensor (3D Vector Calc & Expo Mixing)
├── node_c_display.py      # Node C: Display (6-Param Morphological Engine)
├── ssd1306.py             # Driver: Pure Python OLED Library
├── demo.gif               # Project demonstration animation
├── README.md              # Project documentation (You are here)
└── LICENSE                # MIT License
```

### 🚀 Quick Start

Flash the respective code files to three separate Micro:bit boards (Note: Node C also requires the `ssd1306.py` driver to be flashed together).

1. **Sync Channel:** Ensure the radio group is identical across all three codes (default is `group=22`).
2. **Zero Calibration:** After powering on, hold the Node B sensor horizontally and press **Button B** for a one-click zero calibration.
3. **Interact:** Tilt the handheld sensor and enjoy the ultra-smooth bionic interaction!

### 👨‍💻 Author
* **XIONG Shenli** (Solo Developer)
* *Role:* Full-stack development including hardware architecture, 3D tracking algorithms, and OLED rendering engine.

---

<h2 id="中文">🇨🇳 中文</h2>

这是一个基于 3 个 Micro:bit 节点开发的分布式仿生交互机器人。我独立设计了整个系统的软硬件架构，将人类的手势实时转化为极其丝滑的机械运动与生动的表情变化。

> **"用软件算法治愈廉价硬件的痛。"** —— 本项目的核心理念是：如何通过数学算法优化（指数曲线、低通滤波、线性插值），让几十块钱的廉价舵机跑出工业级的细腻质感。

### 🌟 核心技术亮点
* **极致平滑的运动算法:** 引入 RC 遥控级别的**高阶指数混控曲线 (Expo)** 与**一阶低通滤波 (LPF)**，彻底过滤人手生理抖动与硬件机械卡顿。
* **3D 向量空间追踪:** 弃用简单的角度读取，采用 `math.atan2` 进行全空间重力向量计算，告别万向节死锁与数值翻转。
* **6 参数形态学表情引擎:** 从零编写了一个 6 参数矩阵渲染引擎取代静态图片。包含插值动画过渡 (Lerp)、模拟生物的微跳视 (Saccades) 与随机眨眼逻辑，赋予机器独立意识感。
* **一键校准:** 按下单键即可瞬间建立空间零点基准。

### 🛠 硬件架构
系统分为三个独立节点，通过无线电 (Radio) 进行高频同步通讯：
1. **Node B (传感器端):** 手持感应，负责 3D 信号采集与核心滤波计算。
2. **Node A (云台执行端):** 驱动 2 自由度云台，采用 **Silent PWM** 逻辑彻底消除电机啸叫。
3. **Node C (视觉渲染端):** 搭载 0.96" OLED 屏幕，独立进行表情的矩阵变换与渲染。

## 🛒 物料清单 (BOM)

本项目由三个独立的节点组成，每个节点根据实际功耗和便携性需求采用了不同的供电方案。

| 零件名称 | 数量 | 规格/备注 |
| :--- | :---: | :--- |
| **BBC Micro:bit** | 3 | 主控板，Node A、B、C 各使用一片（V1/V2均可）。 |
| **IO 扩展板** | 2 | 用于 Node A（连接舵机）和 Node C（连接屏幕）。 |
| **MG90S 金属舵机** | 2 | 用于构建 Node A 的两自由度云台。 |
| **SSD1306 OLED 屏幕** | 1 | 0.96寸 I2C 接口，用于 Node C 的视觉渲染。 |
| **USB 数据线** | 1 | 用于 Node A 供电，确保舵机转动时电流稳定。 |
| **3.7V 锂电池** | 1 | 500mAh JST 接口，用于 Node B，实现极致便携。 |
| **3V 七号电池盒** | 1 | 两节 AAA 电池，为 Node C 屏幕端独立供电。 |
| **杜邦线** | 1 套 | 母对母跳线，用于连接 I2C 设备和舵机。 |

### 🔌 接线指南

#### **Node A: 云台执行端**
* **供电：** 使用 USB 线连接至电脑或充电宝（舵机耗电较大，建议 USB 供电）。
* **舵机：** X轴（俯仰）接扩展板 **P0**，Y轴（横滚）接扩展板 **P1**。

#### **Node B: 手持传感器端**
* **供电：** 3.7V 锂电池直接插在 Micro:bit 背面的 JST 电池接口。
* **接线：** 无需外部接线（使用主控板内置加速度计）。

#### **Node C: 视觉显示端**
* **供电：** 3V 电池盒连接至扩展板的电源引脚。
* **屏幕：** **SCL** 接 **P19**，**SDA** 接 **P20**，**VCC** 接 **3V3**，**GND** 接 **GND**。

### 📂 目录结构 (Directory Structure)

```text
Microbit-Distributed-Gimbal/
├── node_a_actuator.py     # Node A: 云台端 (Silent PWM 与运动平滑)
├── node_b_sensor.py       # Node B: 传感器端 (3D 向量计算与 Expo 混控)
├── node_c_display.py      # Node C: 视觉端 (6 参数形态学渲染引擎)
├── ssd1306.py             # 底层驱动: 纯 Python 版 OLED 驱动库
├── demo.gif               # 项目演示动图
├── README.md              # 项目说明文档与 BOM 清单
└── LICENSE                # MIT 开源协议
```

### 🚀 快速开始

将对应节点的代码分别烧录至三个 Micro:bit 主板中（注：Node C 还需要同时烧录 `ssd1306.py` 驱动文件）。

1. **统一频道：** 确保三份代码中的无线电频道保持一致（默认 `group=22`）。
2. **零点校准：** 系统通电后，水平握住传感器 Node B，按下 **Button B** 进行一键零点校准。
3. **开始互动：** 倾斜手里的传感器，体验丝滑的仿生机器人联动！

### 👨‍💻 开发者
* **熊珅黎 (XIONG Shenli)** - 独立开发者
* *负责内容:* 硬件架构搭建、全套平滑滤波算法开发、OLED 仿生渲染引擎设计。

---
*If you find this project interesting, feel free to give it a ⭐ Star!*
