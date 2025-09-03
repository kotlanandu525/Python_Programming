num=input("enter a numbeer")
def evaluate(x):
    if(x in "aeiouAEIOU"):
        return "VOWEL"
    else:
        return "CONSONENT"
print(evaluate(num))