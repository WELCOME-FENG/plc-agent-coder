from crewai import Task

class PLCTasks:
    def architecture_task(self, agent, raw_spec):
        return Task(
            description=f'''分析以下业务需求并输出状态机架构及I/O分配表：
            {raw_spec}
            要求：必须明确划分 0-90 的状态流转路径，包含初始化、自动运行和故障停机。''',
            expected_output='JSON格式的状态机流转图和系统变量映射表。',
            agent=agent
        )

    def coding_task(self, agent):
        return Task(
            description='基于架构输出，编写具体的结构化文本(ST)代码。你需要生成FB1(轴联动控制)、FB2(品质判定)和FB4(报警管理)的核心逻辑。',
            expected_output='包含具体FB定义的纯ST语言代码文本，必须带有详尽的中文工业注释。',
            agent=agent
        )

    def validation_task(self, agent):
        return Task(
            description='对生成的FB逻辑进行安全审计。重点检查：当处于正常运行状态时，若发生突发急停或防呆拦截触发，系统是否具备强大的阻断能力并准确跳转至State 90？',
            expected_output='逻辑漏洞审计报告。若安全则输出"PASS"，若有漏洞需提供精确到行的修改建议及原理解释。',
            agent=agent
        )
