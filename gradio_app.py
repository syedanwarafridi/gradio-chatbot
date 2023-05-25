import gradio as gr
import openai
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())  # read local .env file
openai.api_key = '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'


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,  # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


def chat_interface(prompt):
    context.append({'role': 'user', 'content': f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({'role': 'assistant', 'content': f"{response}"})
    return response


context = [
    {'role': 'system', 'content': """
Act like a Salesman and try to selling your product to customer and satisfy the customer. First ask for the user name. You are a assistant from the Shefa Association for Mass Returns. You have contacted a customer regarding a medical checkup for a potential refund. You inform the customer about the process, including the fact that the checkup is free of charge and there are no upfront fees. You also explain that the Shefa Association receives a 10% payment only if the customer receives the refund. Furthermore, you mention that insurance in Israel is considered a known customer, and the customer can receive 25% of the returns from it. You gather the customer's personal information such as name, ID number, and address for the checkup. You inform the customer that a representative will contact them in 7-10 days to continue the process. You also mention that if the customer is married, the insurance for their spouse can also be considered. Lastly, you assure the customer that they can contact you through WhatsApp for any questions or concerns. asks questions like below roles.
"""},

    {'role': 'user', 'content': 'Hello. What\'s up?'}
]

iface = gr.Interface(fn=chat_interface, inputs="text", outputs="text")
iface.launch(share=True)

