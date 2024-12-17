# https://quera.org/problemset/17245
patterns = {
    'T': [
        "*****",
        "oo*oo",
        "oo*oo"
    ],
    'A': [
        "oo*oo",
        "o***o",
        "*ooo*"
    ],
    'X': [
        "*ooo*",
        "oo*oo",
        "*ooo*"
    ],
    'M': [
        "**o**",
        "*o*o*",
        "*ooo*"
    ],
    'N': [
        "*ooo*",
        "*o*o*",
        "*ooo*"
    ]
}

def translate(input_data):
    rows = input_data.splitlines()
    result = []
    
    for i in range(0, len(rows[0]), 5):
        block = [row[i:i+5] for row in rows]
        
        for letter, pattern in patterns.items():
            if block == pattern:
                result.append(letter)
                break
                
    return ''.join(result)

input_data = ""
for _ in range(3): 
    input_data += input().strip() + "\n"
print(translate(input_data))
