#the function checks for index of consonant values in strings and outputs the value of the consonant with highest ASCII value

def output_max_value(letter):
    def calculate_consonants(strings):
        return sum(ord(l) - ord('a') + 1 for l in strings) 
    
    consonants = [] #empty list where the whole string is appended
    current_letter = "" #empty string in which each letter in a string appended 
   

    for char in letter: #iteration of single letter in a string
        if char not in "aeiou": #checks whether the letter is a vowel
            current_letter += char # adds the consonant to the current_letter variable
        else:  #checks for the vowels
            if current_letter:
                consonants.append(calculate_consonants(current_letter))
               
                current_letter = "" #appends empty string to the consonants lists when the program runs into a vowel in the string

    if current_letter:
        consonants.append(calculate_consonants(current_letter)) #appends the consonants to the consonants list

    return max(consonants) if consonants else 0 #checks for the max value of the index of the consonants 

print(output_max_value("zodiacs"))
print(output_max_value("strength"))
            
