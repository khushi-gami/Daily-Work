

def vowles_count(value):
    total_vowels = 0
    vowels = "aeiouAEIOU"
    for i in value:
        if i in vowels:
            total_vowels += 1
            print(i)
    return total_vowels
            
    
    