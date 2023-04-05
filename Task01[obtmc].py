# Atividade da Disciplina de Compiladores - Task1 - Olivia Tavares (obtmc)
fileIn = open('Calc1.stk', 'r');

data = fileIn.readlines();
fileIn.close();
data = [i.strip() for i in data]; # eliminando os '/n' copiados do arquivo de entrada
size = len(data);
result = [];

for i in range(0,size):
    if   data[i] == '*':
        result[0] = result[0] * result[1];
        result.pop();
        #print(result[0]);
    elif data[i] == '/':
        result[0] = result[0] / result[1];
        result.pop();
        #print(result[0]);
    elif data[i] == '+':
        result[0] = result[0] + result[1];
        result.pop();
        #print(result[0]);
    elif data[i] == '-':
        result[0] = result[0] - result[1];
        result.pop();
        #print(result[0]);
    else: 
        result.append(float(data[i])); # se "data[i]" não é um operador é um número
        #print(result);

print (result[0]);
fileOut = open('Saida.txt', 'w');
fileOut.write(str(result[0]));

