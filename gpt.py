import openai
import os

openai.api_key=os.environ.get("gpt_key")

messages=[]
def gpttype(role="system",content="You are a kind helpful assistant"):
    messages.append(
        {"role":role,"content":content}
        )
def askgpt(message,product):
    gpttype()
    if message:
        messages.append(
            {"role":"user","content":f"{message} . Have this tweet a relation with this product {product}? Answer with yes or no"}
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply=chat.choices[0].message.content
        messages.append(
            {"role":"assistant","content":reply}
        )
        return reply[0:3] #we need just the Yes or No response



 
    

#print(askgpt("Want to be a Data Analyst in 100 Days? \n\nDay 1-15:\nMaths & Statistics \n\nDay 16-35:\nExcel\n\nDay 36-46:\nSQL\n\nDay 47-60:\nPython/Data Cleaning\n\nDay 61-75:\nData Analysis and Cleaning\n\nDay 76 - 85:\nPresenting Data Models\n\nDay 86-100:\nDeploying Models","excel"))

#print(askgpt("When I tell young people about the Japanese American internment, they're not going to grow up to be Japanese.When I tell kids I'm married to Brad, they don't suddenly ooze rainbows and turn gay.The're just learning about the world and others in it.See how that works?","excel"))