import os
import openai

def gpt3(stext):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
                temperature=0.1,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0.01,
                presence_penalty=0
    )
    content = response.choices[0].text.split(".")
    print(content)
    return response.choices[0].text

query = 'What is 7X10=?'
response = gpt3(query)
print(response)