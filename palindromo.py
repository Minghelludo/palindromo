

def is_palindrome(seq, size):
    if size==1:
        return True
    sup = size-1
    size = int(size/2)
    for i in range(size):
        if seq[i] != seq[sup]:
            print(i)
            return False
        sup = sup-1
    return True

string = "arara"
size = len(string)

check = is_palindrome(string,size)
print(check)