# plc-agent-coder
# AutoPLC-Agent: Multi-Agent Driven Industrial Control Logic Generation System

## 📌 项目概述 (Project Overview)
AutoPLC-Agent 是一个针对工业自动化控制系统（基于 IEC 61131-3 标准）的智能体驱动代码生成与审计框架。

本项目聚焦于复杂的**全自动锁付循环控制系统**，旨在通过多智能体协作（Multi-Agent Collaboration）与大语言模型的长链推理（Chain of Thought），彻底解决传统 PLC 编程中状态机极易死锁、防呆拦截遗漏以及过度依赖人工经验的行业痛点。

## 🎯 核心业务痛点与解决逻辑
在标准的工业产线开发中，底层控制逻辑的编写是一项耗时且极易出错的工程：
1. **状态机耦合严重**：从 `State 0` (初始化) 到 `State 90` (故障停机) 的状态流转，常因异常处理不当导致系统崩溃。
2. **测试周期漫长**：传统的物理联调成本极高，缺乏在代码生成阶段的“沙箱级”逻辑阻断推演。

**解决逻辑**：
引入 CrewAI 编排的多个专家级 Agent。剥离人类工程师的重复性编码工作，仅由系统进行高维度的需求解析，自动生成标准化的功能块（FB），并强制执行 OB1（主循环）仅做调用的极简架构，实现真正的模块化与防呆拦截闭环。

## ⚙️ 多智能体架构设计 (Multi-Agent Architecture)

系统由三个核心智能体协同闭环，形成高密度的 Token 消耗与深度推理链路：

- **🏗️ 架构 Agent (Architect Agent)**
  - **职责**：解析非结构化的业务需求，提取 I/O 拓扑。
  - **输出**：建立全局状态机流转图谱，定义严格的变量映射表。
- **💻 编码 Agent (Coder Agent)**
  - **职责**：将状态机图谱具象化为结构化文本 (ST)。
  - **输出**：生成高度解耦的独立功能块（如 `FB1_轴联动控制`, `FB2_品质判定`, `FB3_产量统计`, `FB6_送料分拣` 等）。
- **🛡️ 验证 Agent (Validator Agent)**
  - **职责**：作为系统的“安全沙箱”，执行极端的边界条件测试。
  - **推理逻辑**：通过多步长链推理，模拟如“异常送料”、“扭矩突变”等突发急停场景，确保系统能无条件切入 `State 90` 并封锁所有输出，杜绝物理撞机风险。

## 🚀 快速启动 (Quick Start)

### 1. 环境依赖
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
