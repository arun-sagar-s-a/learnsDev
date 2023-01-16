"""_summary_: Simple portfolio project to understand python better.
    Its a story teller, based on input options you select the story changes.
    Author: Arun Sagar S A 
    Date:16/Jan/2023
"""


class Story:
    def __init__(self):
        pass


print('A very warm welcome to you! It is lovely to have you among us!')
listener_name = input('Can we know your good name: ')
print(
    f'We are glad to welcome you {listener_name}!!\nYour presence is well appreciated, and we are delighted you are here.\nPlease feel at home.')
print('We have these story(ies) for you!')
story_list = ['It’s Little Things']
for c, i in enumerate(story_list):
    print(f"{c+1}. {i}")
