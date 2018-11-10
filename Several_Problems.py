"""
Miranda Bohm
CISC 179: Python Programming 
Monday, 10/29/2018
"""

# =============================================================================
# Exercise 2: Sum of Digits in a String
# =============================================================================

def main():
    relevant_string = input('Please enter some integers, without spaces or symbols. ')

    while relevant_string.isdigit() == False:
        relevant_string = input('Please try again. Only integers are accepted. ') 

    running_total = 0
    for digit in relevant_string:
        running_total += int(digit)
    
    print('The sum of digits is ',running_total)

main()

# =============================================================================
# Exercise 8: Sentence Capitalizer
# =============================================================================

def main():
    paragraph = input('Please enter a few sentences whose first words will be capitalized. ')   
    
    print('\n\n- - - - - - - - - - - - - -\n\n')
    capitalizer(paragraph)
        
def capitalizer(paragraph):
    for sentence in paragraph.split('.'):
        if sentence !='':
            sentence = sentence.strip()
            sentence = sentence[0].upper() + sentence[1:] + '. '
            print(sentence)

main()


# =============================================================================
# Exercise 11: Word Separator
# =============================================================================

def main():
    sentence = 'LookOutBehindYou!'
    sentence = formatter(separator(sentence))
    
def separator(sequence):
    new_space_indexes = []
    
    for index in range(0,len(sequence)): 
        if sequence[index].isupper() == True:
            new_space_indexes.append(index)
    
    # THE REASONING BEHIND ':NEW_SPACE_INDEXES[i] + i]', SEEN BELOW:
    # i is added to account for empty spaces previously added to the sentence.
    # After one space has been added (first iteration), the sentence is one
    # character longer. The next iteration will need to consider that +1 extra
    # length in its indexing. After two spaces have been added to the sentence, 
    # future indexing will need to take two extra characters into account. 
    
    for i in range(len(new_space_indexes)):
        sequence = sequence[:new_space_indexes[i] + i] + ' ' + sequence[new_space_indexes[i] + i:]
        
    return sequence
    
def formatter(sentence):
    # Accounts for lowercase words at the beginning of sentence, which 
    # theoretically shouldn't be present. 
    if sentence[0] == ' ':
        sentence = '' + sentence[1:]
    
    # Capitalize the first letter in the sentence, but lower everything else. 
    sentence = sentence[0].upper() + sentence[1:].lower()
    print(sentence)
                
    
main()








