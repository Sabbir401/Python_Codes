str=input("Enter a String: ")
upper=0
lower=0

for i in str:
   if i.isupper():
      upper=upper+1
   elif i.islower():
      lower=lower+1

print(f"UPPER CASE {upper}")
print(f"LOWER CASE {lower}")