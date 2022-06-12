def reverse_words_order__order_and_swap_case(Sentences):
    mystr=" "
    for i in Sentences:
        if i.isspace():
            mystr+=" "
        else:
            if i.isupper():
                mystr+=i.lower()
            if i.islower():
                mystr+=i.upper()
    words=list(reversed(mystr.split()))
    mywords=" ".join(words)
    return mywords
out=reverse_words_order__order_and_swap_case("Hello World")
print(out)