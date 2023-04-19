# Atividade da Disciplina de Compiladores - Task1 - Olivia Tavares (obtmc)

from Token import Token
from TokenType import TokenType


# Função que processa a expressão
def result_(data):
    result = [];
    size = len(data);

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

    return result[0];

def scanning(data_scan):
    size = len(data);
    tokens = [];
    j = 0;
    str = '';

    for i in range(0,size):
        if   data_scan[i] == '*':
            tokens.append(Token(TokenType.STAR, "*"));
            print(tokens[j]);
            j +=1;          

        elif data_scan[i] == '/':
            tokens.append(Token(TokenType.SLASH, "/"));
            print(tokens[j]);
            j +=1; 

        elif data_scan[i] == '+':
            tokens.append(Token(TokenType.PLUS, "+"));
            print(tokens[j]);
            j +=1; 

        elif data_scan[i] == '-':
            tokens.append(Token(TokenType.MINUS, "-"));
            print(tokens[j]);
            j +=1; 
            
            print(data_scan[i].isdigit())

        elif data[i].isdigit():# se "data[i]" não é um operador será um número
            #num.append(data[i]);
            str = data_scan[i];
            print(data_scan[i]);
            i +=1;  
            while data_scan[i].isdigit():# Ainda existe número após o ponto
                #num.append(data[i]);
                print(data_scan);
                str = str + data_scan[i];
                print(data_scan[i]);
                i +=1;
                #print(data[i]);

            if data[i] == ".":
                str = str + data_scan[i];
                print(data_scan[i]);
                i +=1;
                while data_scan[i].isdigit():# Ainda existe número após o ponto
                    #num.append(data[i]);
                    str = str + data_scan[i];
                    print(data_scan[i]);
                    i +=1;
                    
                i -=1;
                tokens.append(Token(TokenType.NUM, "str"));
                print(tokens[j]);
                #i +=1;

            else:
                i +=1;
        else:
            print("\"" + data_scan[i] + "\"" + " não é um token possível.");
        
        print(data_scan[i]);

# INÍCIO DO PROGRAMA

# Abrindo e lendo arquivo de entrada
fileIn = open('Calc1.stk', 'r');
data = fileIn.readlines();
fileIn.close();

# Tratando entrada
# eliminando os '/n' copiados do arquivo de entrada
data = [i.strip() for i in data]; 

# Tokenização
scanning(data);

# Resolvendo a expressão
result = result_(data);

# Expondo resultado
print ('\nSaída: ', result, '\n');
fileOut = open('Saida.txt', 'w');
fileOut.write(str(result));
fileOut.close();

