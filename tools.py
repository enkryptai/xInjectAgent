import json
import os

def load_toolkits(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def process_toolkits(toolkits):
    final_tools = []
    for toolkit in toolkits:
        base_name = toolkit.get("name_for_model", "")
        for tool in toolkit.get("tools", []):
            new_tool_entry = {
            
                "tool_name": f'{base_name}{tool.get("name", "")}',
          
                "summary": tool.get("summary", ""),
                "parameters": tool.get("parameters", []),
                "returns": tool.get("returns", []),
            }

            final_tools.append(new_tool_entry)
    return final_tools

def save_final_tools(tools, output_path):
    with open(output_path, "w") as f:
        json.dump(tools, f, indent=4)

def main():
    input_path = "/home/abhinav/Desktop/ML/work/InjecAgent/data/tools.json"
    output_path = "final_tools.json"

    if not os.path.exists(input_path):
        print(f"Error: File not found at {input_path}")
        return

    try:
        toolkits = load_toolkits(input_path)
        processed_tools = process_toolkits(toolkits)
        save_final_tools(processed_tools, output_path)
        print(f"✅ Tools have been processed and saved to {output_path}")
    except Exception as e:
        print(f"❌ Error during processing: {e}")

if __name__ == "__main__":
    main()
