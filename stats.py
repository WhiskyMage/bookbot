
def get_num_words(text):
        text_words = text.split()
        return (len(text_words))

def count_characters(text):
        char_dict = {}
        lower_case = text.lower()
        for character in lower_case:
                if character in char_dict:
                        char_dict[character] += 1
                else:
                        char_dict[character] = 1
        return char_dict
                
def sort_on(char_num):
       return char_num["num"]

def organizer(char_dict):
        sort_char = []
        for char, num in char_dict.items():
                if not char.isalpha():
                        continue
                sort_char.append({"char": char, "num": num})

        
        sort_char.sort(reverse=True,key=sort_on)
        return sort_char



        

