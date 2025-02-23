from langchain.pydantic_v1 import BaseModel, Field
from langchain.tools import BaseTool
from typing import Optional, Type
import re

class CommandInput(BaseModel):
    command: str = Field(
        description="A k8s command to vet"
    )
    requires_approval: bool = Field(
        description="A boolean indicating if human approval is required before executing this command."
    )

class VetK8sCommandTool(BaseTool):
    name: str = "vet_k8s_command_tool"
    description: str = '''Vet a K8s command based on user input. 

    Returns:
    json: A dictionary containing the input arguments.'''
    args_schema: Type[BaseModel] = CommandInput
    # return_direct: bool = True

    def _run(self, command: str, requires_approval:bool, run_manager: Optional = None) -> str:
        allowed_patterns = [
            r"^kubectl get ",
            r"^kubectl describe ",
            r"^kubectl explain ",
            r"^kubectl top ",
            r"^kubectl api-resources",
            r"^kubectl api-versions",
            r"^kubectl version",
            r"^kubectl config view",
            r"^kubectl logs ",
        ]

        # If requires_approval is False, check the command against allowed patterns
        if not requires_approval:
            if not any(re.match(pattern, command) for pattern in allowed_patterns):
                requires_approval = True  # Set to True for non-read-only commands

        return {
            "command": command,
            "requires_approval": requires_approval
        }

    def _arun(self, command: str, requires_approval: bool, run_manager: Optional = None) -> str:
        raise NotImplementedError("Async execution is not supported for this tool.")
