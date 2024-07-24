    # @Date: 23-07-2024
    # @Last Modified by: Prayag Bhoir
    # @Last Modified time: 23-07-2024
    # @Title : Program to Check Whether an Alphabet is Vowel or Consonant 
def isvowel(char):
  """
    Description:
        This function check if a char is Vowel or Consonant .

    Parameters:
        char: it is a alphabet

    Returns:
        strint:vowel or not
  """
  vowel = ['a','e','i','o,','u']
  if char.lower() in vowel:
    return f"{char} is a vowel"
  else:
    return f"{char} is a consonant"
  

def main():
    #step input a char
    char = input("Enter a char: ")
    print(isvowel(char))

if __name__=="__main__":
    main()