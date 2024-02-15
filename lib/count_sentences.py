#!/usr/bin/env python3
import ipdb

class MyString:
  def __init__(self, value=None):
    self._value = value
    

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if isinstance(new_value, str):
        self._value = new_value
    else:
        print("The value must be a string.")  

  def is_sentence(self):
      if self._value[-1] == ("."):
        return True
      else:
        return False  

  def is_question(self):
    if self._value[-1] ==("?"):
      return True
    else:
      return False

  def is_exclamation(self):
    if self._value[-1] ==("!"):
      return True
    else:
      return False
  
  def count_sentences(self):
    sentence_ending =[".", "!", "?"]
    sentence_count = 0

    for char in self._value:
      if char in sentence_ending:
        sentence_count +=1
    return sentence_count  

    



