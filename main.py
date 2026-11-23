from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
client=genai.Client(api_key=api_key)


orders={
    "A001":"Shipped",
    "A002":"Delivered",
    "A003":"Processing",
    "A004":"Cancelled",
    "A005":"Out for delivery",
    "A006":"Shipped",
    "A007":"Processing"
}


def lookup_order_status(order_id: str) -> dict:
    if order_id in orders.keys():
        res=orders[order_id]
        return{
            "Order_id":order_id,
            "Status":res
        }
    else:
        return{
            "Order_id":order_id,
            "Status":"Not Found"
        }
        
            


tool_information={
    "name":"Order_Status_Check",
    "description":"Look up the current shipping status of an order by its ID",
    "parameters":{
        "type":"object",
        "properties":{
            "order_id":{
                "type":"string"
            }
        },
        "required":["order_id"]
    }
}


tool=types.Tool(
    function_declarations=[tool_information]
)

config=types.GenerateContentConfig(
    tools=[tool]
)



response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="What's the status of order A002?",
    config=config
)

print(response)

tool_calling=response.function_calls[0]
if tool_calling.name=="Order_Status_Check":
    result=lookup_order_status(
        tool_calling.args["order_id"]
    )



function_response=types.Part.from_function_response(
    name=tool_calling.name,
    response={
        "result":result
    }
)



final_response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part.from_text(text="What's the status of order A002?")
                   ]
        ),
        
        response.candidates[0].content,
        
        types.Content(
            role="user",
            parts=[function_response]
        )
    ]
)

print(final_response.text)

