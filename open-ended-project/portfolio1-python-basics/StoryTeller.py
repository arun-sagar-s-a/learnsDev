"""_summary_: Simple portfolio project to understand python better.
    Its a story teller, based on input options you select the story changes.
    Author: Arun Sagar S A 
    Date:16/Jan/2023
"""
import time


class Story:
    def __init__(self, title, moral, brief):
        self.title = title
        self.moral = moral
        self.brief = brief


# inital greeting message....!
print('A very warm welcome to you! It is lovely to have you among us!')
listener_name = input('Can we know your good name: ')
time.sleep(1)
print("## ## ## ## ## ## ## ## ## ## ## ## ## ##")
print(
    f'We are glad to welcome you {listener_name}!!\nYour presence is well appreciated, and we are delighted you are here.\nPlease feel at home.')
print("## ## ## ## ## ## ## ## ## ## ## ## ## ##")
print('We have these story(ies) for you!')
time.sleep(1)
# list of story and moral in order, but seperate list
story_list = ['It’s Little Things']
story_moral = ['It’s the little things that make a huge impact in our lives. Sometimes we ignore the small things that are already in front of us because we lose sight of what is important. A small act of kindness, actions that seem insignificant for most people could mean the world to another person!']
# display intial list of story
time.sleep(1)
print("Please select one from the list.")
"""
Current plan:
1. user selects story - done.
2. class is created for story with name and moral - done.
"""
usr_input = 0
while True:
    for c, i in enumerate(story_list):
        print(f"{c+1}. {i}")

    try:
        usr_input = int(input("Option number: "))
        if usr_input > 0 and usr_input <= len(story_list):
            print(f"This is the story you chose: {story_list[usr_input-1]}")
            break
        else:
            print("Please enter valid number.")
    except ValueError:
        print("Please enter a valid input.")

story = Story(story_list[usr_input-1], story_moral[usr_input-2], brief="")
print(story.moral)
