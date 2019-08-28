import time
input("Put your Instagram accounts list here: ")
time.sleep(1.5)
print("File found!")
username = input("Put the IG Username and press ENTER: ")
time.sleep(2)
print(username, "found")
message = input("Put the message and press ENTER: ")
time.sleep(1)
times = int(input("How many messages do you want to send?"))
time.sleep(1)
print("You are gonna STRESS", times,"times", username, "with the message: ", message, ".")
input("Are you sure?")
i = 0
while True:
    if times > i:
        i = i + 1
        print(i, ">> Sent to", username, ": ", message)
        time.sleep(0.01)
    else:
        print("Done!")
        break