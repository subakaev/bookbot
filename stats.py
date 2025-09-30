def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_characters_dict(text):
  dict = {}

  text = text.lower()

  for char in text:
    if char in dict:
      dict[char] += 1
    else:
      dict[char] = 1

  return dict

def sort_on(item):
  return item["num"]

def sort_characters_dict(characters_dict):
  items = []

  for key, value in characters_dict.items():
    items.append({ "char": key, "num": value })

  items.sort(key=sort_on, reverse=True)

  return items