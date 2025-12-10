email = input("Emailingizni kiriting, email .com bilan tugashligi kerak")

result = email[0] != "@" and email.endswith(".com")

print(result)