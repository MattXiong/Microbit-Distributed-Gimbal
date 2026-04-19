# Microbit-Distributed-Gimbal
A distributed 3-node bionic robot system with 2-DOF gimbal and emotional OLED display.
# 🤖 Bionic Companion Robot / 分布式仿生交互机器人

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Platform: Micro:bit](https://img.shields.io/badge/Platform-Micro%3Abit-green.svg)](https://microbit.org/)

🌍 Read this in: [English](#english) | [中文](#中文)

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

### 📂 Repository Structure
Bionic-Microbit-Robot/
├── src/
│   ├── node_a_actuator.py    # Gimbal servo control & Silent PWM
│   ├── node_b_sensor.py      # 3D tracking & Expo mixing curve
│   └── node_c_display.py     # OLED morphing engine
├── docs/
│   └── hardware_layout.md    # BOM & Wiring guide
└── README.md                 # You are here

### 🚀 Quick Start
1. Flash the code from the src/ directory to your three respective Micro:bits.

2. Ensure all nodes are set to the same radio channel (group=22).

3. Power on the system. Hold the Node B sensor level and press Button B for a quick one-click zero-point calibration.

4. Tilt the sensor to interact!

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

### 📂 目录结构
Bionic-Microbit-Robot/
├── src/
│   ├── node_a_actuator.py    # 云台端：Silent PWM 与运动平滑算法
│   ├── node_b_sensor.py      # 传感器端：3D 向量计算与 Expo 混控
│   └── node_c_display.py     # 视觉端：6 参数形态学渲染引擎
├── docs/
│   └── hardware_layout.md    # 硬件清单与接线逻辑
└── README.md                 # 当前说明文档

### 🚀 快速开始
将 src/ 文件夹下的代码分别烧录至三个 Micro:bit 节点。

1. 确保代码中的无线电频道一致 (group=22)。

2. 系统通电后，水平握住传感器 Node B，按下 Button B 进行一键零点校准。

3. 倾斜传感器，开始与你的机器人互动！

### 👨‍💻 开发者
* **熊珅黎 (XIONG Shenli)** - 独立开发者
* *负责内容:* 硬件架构搭建、全套平滑滤波算法开发、OLED 仿生渲染引擎设计。

---
*If you find this project interesting, feel free to give it a ⭐ Star!*
