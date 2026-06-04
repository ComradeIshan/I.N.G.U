message  = input(">")         #this is pretty cool tbh
words = message.split(' ')
emojis = {
    ":)": "😄",
    ":(": "😔"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "  #Two words is written because When we supply A value that is not matching in the tuple created above The output will be the same word that the user has written The first word is used to get the value and convert it to emoji and the 2nd word has the use that I specified before Which will return the same word in the output .
print(output)
