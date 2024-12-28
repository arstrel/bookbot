book = "books/frankenstein.txt"

def main():
   with open(book) as f:
      file_contents = f.read()
      total_words = len(file_contents.split())
      
      freq = {}
      for char in file_contents:
         lower_char = char.lower().strip()
         if(lower_char == ""):
            continue
         if lower_char in freq:
            freq[lower_char] += 1
         else:
            freq[lower_char] = 1
      
      print(f"--- Begin report of {book} ---")
      print (f"{total_words} words found in the document")
      for char, count in freq.items():
         print(f"The '{char}' character was found {count} times")
      print(f"--- End report ---")

    

main()
