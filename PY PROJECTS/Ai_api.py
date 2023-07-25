import openai
import os

openai.api_key ='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'

promt=input("ENTER THE QUERRY >> ")
output = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "HELLO WORLD "}]
,prompt=promt

                                      )

# while True:
#     model_engine ="text-davinci-003"
#   
#     if "exit" in promt or "quit" in promt:
#         print("BYE BYEEEEE >> ")
#         break

#     completion= openai.ChatCompletion.create(
#     model="gpt-3.5-turbo", 
#     prompt=promt,              
#     messages=[{"role": "user", "content": "Hello world"}])
    # completion =openai.Completion.create(
    #     engine=model_engine,
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1, stop=None,
    #     temperature=0.5)
    
    # responce=completion.choices[0].text
print(output)