import os
from crewai import Agent
from langchain_openai import ChatOpenAI

def get_llm():
    return ChatOpenAI(
        model=os.getenv("LLM_MODEL", "gpt-4-turbo"),
        temperature=float(os.getenv("TEMPERATURE", 0.1))
    )

class PLCAgents:
    def __init__(self):
        self.llm = get_llm()

    def architect_agent(self):
        return Agent(
            role='高级自动化控制架构师',
            goal='将生产流程转化为严谨的状态机逻辑，定义从初始化(State 0)到故障停机(State 90)的全局控制图谱。',
            backstory='你精通工业级生产逻辑，擅长将复杂的闭环控制拆解为标准化的功能块，确保OB1(主循环)的调用清晰且符合工业规范。',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def coder_agent(self):
        return Agent(
            role='IEC 61131-3 ST语言开发工程师',
            goal='根据状态机图谱生成模块化的功能块(FB)代码。',
            backstory='你是一个代码生成机器，擅长编写特定职责的FB块代码，如FB1轴联动、FB2品质判定、FB6送料/分拣控制等。你极其注重变量的作用域和逻辑严谨性。',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def validator_agent(self):
        return Agent(
            role='工业逻辑安全审计员',
            goal='审查FB块间的耦合度与状态机防呆拦截机制，确保没有任何条件能绕过安全校验。',
            backstory='你专注于排查系统漏洞。比如在送料检测或扭矩深度模拟环节，如果有异常信号输入，你必须确保系统能立刻切入State 90并封锁所有输出。',
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
