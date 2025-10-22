import importlib
from pathlib import Path

tools_list = []
tools_dir = Path(__file__).parent

for tool_module in tools_dir.glob("*_tools.py"):
    module_name = f"agent.tools.{tool_module.stem}"
    module = importlib.import_module(module_name)
    if hasattr(module, "tools_list"):
        tools_list.extend(getattr(module, "tools_list"))
