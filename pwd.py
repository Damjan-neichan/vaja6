print("=== PASSWORD VALIDATOR ===")
while true:
  password=input("\nEnter a password: ")
  upper=False
  lower=False
  number=False
  for char in password:
    if char>="A" and char<="Z":
      upper=True
    if char>="a" and char<="z":
      lower=True