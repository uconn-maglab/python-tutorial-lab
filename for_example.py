#!/usr/bin/env python3

tutorial = ["Hello World", "Math", "Boolean operators", "Lists", "Iteration",
    "Control flow", "Functions", "Object-oriented programming"]

class Rachael:
    def __init__(self, tut_list):
        self.tutorial = tut_list

    def say(self, utterance):
        print(utterance)

    def introduce_topics(self):
        for section in self.tutorial:
            self.say(section + " is a really important and useful tool!")



rachael = Rachael(tutorial)
rachael.introduce_topics()
