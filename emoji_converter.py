def emoji_converter(message):
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
    res = ""
    for word in message:
        res += emojiDict.get(word, word) + " "
    return res


msg = input("> ").split()
print(emoji_converter(msg))
