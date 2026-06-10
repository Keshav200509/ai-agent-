import importlib
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

tools_list = []
tools_dir = Path(__file__).parent

for tool_module in tools_dir.glob("*_tools.py"):
    module_name = f"agent.tools.{tool_module.stem}"
    try:
        module = importlib.import_module(module_name)
    except Exception as exc:
        logger.error("Failed to import tool module %s: %s", module_name, exc)
        continue
    if hasattr(module, "tools_list"):
        tools_list.extend(module.tools_list)
    else:
        logger.warning(
            "Tool module %s has no 'tools_list' attribute; skipping", module_name
        )
