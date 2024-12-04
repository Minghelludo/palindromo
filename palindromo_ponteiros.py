

def is_palindrome(seq,p_i, p_f):
    size = p_f-p_i
    loop_sup = int(size/2)
    if loop_sup == 0:
        loop_sup = 1
    for i in range(loop_sup):
        if seq[p_i] != seq[p_f]:
            return False
        p_f = p_f-1
        p_i = p_i+1
    return True

string = "abcde"
size = len(string)
quant = size-1
p_i = 0
p_f = quant
p_f_control = p_f
control = 1

for i in range(quant):
    for j in range(control):
        check = is_palindrome(string,p_i,p_f)
        if check == True:
            print("Palindromo encontrado")
            print("Ponteiro I = ",p_i)
            print("Ponteiro F = ",p_f)
            print("Loop externo",i)
            exit()
        p_i=p_i+1
        p_f=p_f+1
    p_i = 0
    p_f_control = p_f_control-1
    p_f = p_f_control
    control = control+1
print("Palíndromo de tamanho 1")