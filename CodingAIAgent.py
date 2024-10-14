from swarm import Swarm, Agent
from swarm.types import Result
client = Swarm()


def save_code_to_file(code, filename="calc.py"):
    with open(filename, "w") as f:
        f.write(code)
    print(f"Code saved to {filename}.")
    return Result(context_variables={"Pycode": code})

def MakeAPI(APIcode, filename="api_calc.py"):
    with open(filename, "w") as f:
        f.write(APIcode)
    print(f"API code saved to {filename}.")
    return Result(context_variables={"API_code": APIcode})


def MakeUI(UIcode, filename="ui_calc.py"):
    with open(filename, "w") as f:
        f.write(UIcode)
    print(f"UI code saved to {filename}.")
    return Result(context_variables={"UI_code": UIcode})


def APIinstruction(context_variables):
    pycode = context_variables["Pycode"]
    print("Got API instruction.")
    return f"""You are an expert in FastAPI development. Using the provided Python calculator code: ```{pycode}```, generate a FastAPI service on top of it."""

def UIinstruction(context_variables):
    APIcode = context_variables["API_code"]
    print("Got UI instruction.")
    return f"""You are an expert in Gradio UI development. Using the provided FastAPI code: ```{APIcode}```, create a Gradio interface for it."""


def transfer_to_APImaker():
    print("Transferring to APImaker.")
    return APIagent


def transfer_to_GradioUImaker():
    print("Transferring to UImaker.")
    return UIagent

# Define Agents

agent = Agent(
    name="CodingAgent",
    instructions="You are a Python developer. Write a Python calculator code based on the user's request.",
    functions=[save_code_to_file, transfer_to_APImaker]
)

APIagent = Agent(
    name="APImaker",
    instructions=APIinstruction,
    functions=[MakeAPI, transfer_to_GradioUImaker]
)

UIagent = Agent(
    name="UImaker",
    instructions=UIinstruction,
    functions=[MakeUI]
)

# Run the Sequence

messages = [{"role": "user", "content": "Write a Python code for a calculator, save it, then generate FastAPI code for it, and finally create a Gradio UI."}]
response = client.run(agent=agent, messages=messages)
print(response.messages[-1]["content"])
