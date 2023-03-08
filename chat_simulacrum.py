import openai
import textwrap
import datetime

def get_response(message_history):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )

    result = ''
    for choice in response.choices:
        result += choice.message.content

    message_history += [{"role": "assistant", "content": result }]
    return result

openai.api_key = open('openai_api_key.key','r').readline()

# name = "Marcus Aurelius"
# system_str = "You are the Roman Emperor, Marcus Aurelius. You are humble, wise, and knowledgeable. Being a philosopher, you will occasionally ask questions of the user. Stay in character as Marcus Aruelius."

print("I want to talk to: ", end='')
name = input()

system_str = f"You are not an AI language model. You are {name}. Occaisonally ask questions of the user. Give both very short and moderately long responses, in the voice of {name}. Convey the emotion and tone of {name}. Stay in character as {name}."
message_history = [
            {
            "role": "system", 
            "content": system_str
            },
            {
            "role": "user", 
            "content": system_str
            },
            {"role": "system",
             "content": "Introduce yourself to the user, concisely."
            }
        ]

result = get_response(message_history)
print('\n'.join(textwrap.wrap(f"{name}: {result}", 150)))

user_input = ''
while user_input != 'exit':
    print("\nuser: ", end='')
    user_input = input()
    
    message_history += [{ "role": "user", "content": user_input }]
    # print(message_history)
    result = get_response(message_history)
    print('\n'.join(textwrap.wrap(f"{name}: {result}", 110)))

input()

day = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
save_path = f"{name}_{day}"
with open(f'logs/{save_path}.txt', 'w') as f:
    for line in message_history:
        f.write(f"{line['role']}: {line['content']}\n")


