import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate_word(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        user_confirmation = input('Did you mean %s instead? Please type yes or no: ' % get_close_matches(w, data.keys())[0])
        if user_confirmation == 'yes':
            return data[get_close_matches(w, data.keys())[0]]
        elif user_confirmation == 'no':
            return'This word is not valid. Please try again'
        else:
            return'I did not understand your entry'
    else:
        return'This word is not valid.  Please try again.'

word = input('Please Enter a Word: ')
output = translate_word(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


print(translate_word(word))

