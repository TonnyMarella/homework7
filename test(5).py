
#!venv/bin/python
from typing import Optional


def remove_extra_spaces (text : str) -> Optional[str]:
    """Test function for str and list type
    Function remove extra spaces in the text"""

    list_of_words = text.split()
    new_text = ' '.join(list_of_words)
    return new_text

def find_most_offen_word(text : str) -> Optional[str]:
    """Test function for dict type
     Function find of the most offen word in the text"""

    list_words = text.split()
    d = {}

    for word in list_words:
        if word not in d:
            d[word] = list_words.count(word)

    counter = 0
    counter_word = ''
    for word, k in d.items():
        if k > counter:
            counter = k
            counter_word = word
    return counter_word

def samechars (text1: str, text2: str) -> Optional[bool]:
    '''Test function for set type
    Whether 2 lines s1, s2 consist of the same characters
    '''
    set1 = set(text1)
    set2 = set(text2)
    return set1 == set2

def sorted_tuple() -> Optional[tuple]:
    tuplels = ((1,), (10, 2), (1, 2, 3),(100,))
    sorted_t = sorted(tuplels, key=lambda x: sum(x))
    return  sorted_t


if __name__ == "__main__":
    print("""Coose would you like to do: \n
          1) Function remove extra spaces in the text -- Press 1
          2) Function find of the most offen word in the text -- Press 2
          3) Whether 2 lines s1, s2 consist of the same characters  -- Press 3
          4) Sorted of tuple -- Press 4
          """)
    k=int(input('Choose: [1-4]'))
    if k == 1:
        test_string = input('Input your text: ')
        new_text = remove_extra_spaces(test_string)
        print(f'Your text after action of function: {new_text}')
    elif k == 2:
        test_string = input('Input your text: ')
        new_text=find_most_offen_word(test_string)
        print(f'Your text after action of function: {new_text}')
    elif k == 3:
        test_string1 = input('Input first text: ')
        test_string2 = input('Input second text: ')
        flags_same = samechars(test_string1,test_string2)
        print(f'Your text after action of function: {flags_same}')
    elif k == 4:
        result = sorted_tuple()
        print(f'Sorted tuple over sum of elements: {result}')
    else:
        print('You inputed Wrong number')