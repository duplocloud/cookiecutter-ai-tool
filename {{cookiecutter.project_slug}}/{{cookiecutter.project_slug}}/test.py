
from duplo_custom_tool.main import VetK8sCommandTool
tool = VetK8sCommandTool()

print("\n"*2)
print("Tool args:")
print(tool.args)
print("\n"*2)

tool_input = {
    "command": "kubectl delete pod my-pod", 
    "requires_approval": False              
}

result = tool._run(**tool_input)

print("Write Command Example:")
print("Input:", tool_input)
print("Output:", result) 
print("\n")
