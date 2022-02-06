lottery  = "i am star"
# 'i' or 'a' or 'm' or 's' or 't' or 'a' or 'r'

print("choose correct character of the word '",lottery,"' to win the lottery")
inputs = input(" ").lower()

if inputs == "i" or inputs == "s" or inputs == "a" or inputs == "r":
    print("congratulation,you win the lottery")
else:
    print("sorry, You didn't win the lottery")
