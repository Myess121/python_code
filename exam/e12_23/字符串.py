str = "abcdefg"
arr = "ss1"
ar = 2*arr + str

print(ar + 'end')

t = ['a' , 'b' , 'c','de','ff' ]
print(t[3:1])
print(t[-3:-5])


def reversewords(input):

    inputwords = input.split(" ")

    inputwords = inputwords[-1::-1]

    output = ' '.join(inputwords)

    return output

if __name__ == "__main__" :
    input = 'i like python'
    rw = reversewords(input)
    print(rw)





'''p = "1234567890"
a = 1
b = 1.0
print(r'aa\n' + 'bb\n' + 'c')
print(type(a))
print(type(type(a)))
print()

q = input("\n\n按下")
print(q)'''