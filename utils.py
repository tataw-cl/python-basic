#Function to get max in a list using a linear search
def find_max(data):
    Max = data[0]
    for num in data:
        if num > Max:
            Max = num
    
    return Max


#Emoji converter function
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


#Human and Person class definition
class Human:
    def __init__(self, gender):
        self.gender = gender
        
    def breathe(self):
        print(f"{self.gender} Humans breathe")
    def soul(self):
        print(f"{self.gender} Humans have a soul")
    
class Person(Human):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} is Talking...')
    
    def walk(self):
        print(f'{self.name} is Walking...') 
