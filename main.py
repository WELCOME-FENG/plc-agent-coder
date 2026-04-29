import os
from dotenv import load_dotenv
from crewai import Crew, Process
from src.agents import PLCAgents
from src.tasks import PLCTasks

# 加载环境变量
load_dotenv()

def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("致命错误：请在 .env 文件中配置 OPENAI_API_KEY")

    # 业务输入：模拟真实的现场需求
    raw_specification = """
    项目：全自动锁付循环控制系统。
    包含核心环节：送料检测、防呆拦截、扭矩与深度模拟、数据自动统计(FB3)。
    架构要求：主程序(OB1)必须只做调用，不得包含具体逻辑，控制逻辑必须下放至独立的FB块中，符合IEC标准。
    """

    agents = PLCAgents()
    tasks = PLCTasks()

    # 实例化 Agents
    architect = agents.architect_agent()
    coder = agents.coder_agent()
    validator = agents.validator_agent()

    # 实例化 Tasks
    task_arch = tasks.architecture_task(architect, raw_specification)
    task_code = tasks.coding_task(coder)
    task_valid = tasks.validation_task(validator)

    # 构建 Crew 工作流
    plc_crew = Crew(
        agents=[architect, coder, validator],
        tasks=[task_arch, task_code, task_valid],
        process=Process.sequential 
    )

    print("=> 正在启动工业多Agent协同系统...")
    result = plc_crew.kickoff()
    
    print("\n" + "="*50)
    print("系统交付物与最终审计报告：")
    print("="*50)
    print(result)

if __name__ == "__main__":
    main()
