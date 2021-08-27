theNaem = input(" Ples Enter Your Naem  : ")
theEmail = input("Ples Enter Your Email : ")

theUsernaem = theEmail[: theEmail.index("@")]
theWebsiet = theEmail[theEmail.index("@") + 1 :]

print(f"Hello {theNaem} Your Email Is {theEmail}")
print(f"Your Usernaem {theUsernaem} \nYour Websiet Is {theWebsiet}")