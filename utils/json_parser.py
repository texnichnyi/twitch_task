import json
import os

from utils.path_helper import get_project_root


def capabilities_parser(platform) -> dict:
    """
      Helper method for read capability
    """
    with open(os.path.join(get_project_root(), "platform_capabilities", f"{platform}.json")) as capabilities_file:
        capabilities = json.load(capabilities_file)
        return capabilities
