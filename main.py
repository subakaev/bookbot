import sys

from stats import get_num_words, get_num_characters_dict,sort_characters_dict

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    return f.read()

def main():
  args = sys.argv

  if len(args) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  print("============ BOOKBOT ============")

  path_to_file = args[1]
  text = get_book_text(path_to_file)

  print(f"Analyzing book found at {path_to_file}...")

  num_words = get_num_words(text)

  num_characters_dict = get_num_characters_dict(text)

  characters = sort_characters_dict(num_characters_dict)

  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")

  for item in characters:
    if item["char"].isalpha():
      print(f"{item['char']}: {item['num']}")

  print("============= END ===============")

main()