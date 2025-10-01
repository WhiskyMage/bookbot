
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
                
            
      

