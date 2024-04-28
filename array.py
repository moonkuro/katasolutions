#Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
#You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. 
#Be careful, there shouldn't be a space at the beginning or the end of the sentence!

#test.assert_equals(smash(["hello", "world"]), "hello world")
#test.assert_equals(smash(["hello", "amazing", "world"]), "hello amazing world")
#test.assert_equals(smash(["this", "is", "a", "really", "long", "sentence"]), "this is a really long sentence")

def smash(words):
    resultado = ""
    for i, palavra in enumerate(words):
        if i == 0:
            resultado += palavra
        else:
            resultado += " " + palavra
    return resultado

print(smash)
    
smash(["luvas","gay","aspas"])
