# # string concantenation (a series of interconnected things or events)
# # suppose we want to create a string that says "subscribe to _____"
# youtuber = "Ivan Benedictus" # some string variable

# # a few ways to do this:
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

name = input("Name: ")

date = input("Date: ")
month = input("Month: ")
year = input("Year: ")
verb = input("Verb: ")
company = input("Company: ")
job = input("Job: ")
number = input("Number: ")

madlib = f"Hi, my name is {name}! I was born on {date} {month} {year}. I'm currently {verb} at {company} as a {job}. \
You're probably wondering how the hell did I got here. So, let me tell you a secret that happen to me {number} years ago, \
when all of this started."

print(madlib)