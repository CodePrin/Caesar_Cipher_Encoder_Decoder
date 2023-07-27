#Caesar Cipher

print("\n\n***************** Welcome to Caesar Cipher encoding ****************\n")
progress=True

while progress:
  alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  choice=input("Type 'encode' to encrypt your message and 'decode' to decrypt your message.\n")
  shift=int(input("Type the shift number, which means the total text count:   "))

  def caesar(alphabet, choice, shift):
    text=input(f"Type your message that you want to {choice}:   ")
    cipher_text=""
    
    if choice=="decode":
      shift*=-1
    if choice=="encode":
      shift*=1
  
    for letter in text:
      original_position=alphabet.index(letter)
      new_position=original_position+shift
      new_letter=alphabet[new_position]
      cipher_text+=new_letter
    print(f"Your {choice}d text is:\n{cipher_text}")

  caesar(alphabet, choice, shift)
  ask=input(f"Type 'yes' if you want to continue and 'no' if you want to stop it.").lower()
  if ask=='yes':
    print("\n\n*************************Program continued*************************\n\n")
  elif ask=='no':
    print("\n\n*************************Program stopped*************************\n\n")
    progress=False

    