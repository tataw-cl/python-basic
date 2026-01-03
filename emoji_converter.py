emojiDict = {":)": "😊",
             ":(": "😞",
             ":D": "😃",
             ";)": "😉",
             ":P": "😛",
             ":'(": "😢",
             ":O": "😮",
             ":/": "😕",
             ":|": "😐",
             "<3": "❤️",
             ":*": "😘",
             "XD": "😆",
             "B)": "😎",
             "-_-": "😑",
             "^_^": "😊",
             ">:(": "😠",
             ":3": "😺",
             ":$": "😳",
             ":^)": "🙂"
             }
message = input("> ").split()
for word in range(len(message)):
    if message[word] in emojiDict:
        message[word] = emojiDict[message[word]]
res = ""
res += " ".join(message)
print(res)