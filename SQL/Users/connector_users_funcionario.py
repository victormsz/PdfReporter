import mysql.connector

cnx = mysql.connector.connect(user = 'root',
                              password='2024%rootsql#',
                              host='127.0.0.1',
                              database='mydb'
                              )

cursor = cnx.cursor()

def create_funcionario(cursor): 
    idfuncionario = input("entre com o id do funcionario: ")
    nome = input("entre com o nome do funcionario: ")
    email = input("entre com o email do funcionario: ")
    senha = input("entre com a senha do funcionario: ")
    cursor.execute("INSERT into mydb.funcionario(idfuncionario, nome, email, senha) values(%s , %s, %s, %s);", (idfuncionario, nome, email, senha))
    cnx.commit()
    
def get_funcionario_byname( cursor ):

    #placeholder for the name of the employee, será input no futuro
    funcionario = input("entre com o nome do funcionario: ")


    cursor.execute("SELECT * FROM mydb.funcionario WHERE nome = %s ", (funcionario))
    result = cursor.fetchall()
    return result

def get_funcionario_byid( cursor ):

    #placeholder for the name of the employee, será input no futuro
    funcionario = input("entre com o id do funcionario: ")


    cursor.execute("SELECT * FROM mydb.funcionario WHERE idfuncionario = %s ", (funcionario))
    result = cursor.fetchall()
    return result

def get_funcionario_byemail( cursor ):
    
        #placeholder for the name of the employee, será input no futuro
        funcionario = input("entre com o email do funcionario: ")
    
    
        cursor.execute("SELECT * FROM mydb.funcionario WHERE email = %s ", (funcionario))
        result = cursor.fetchall()
        return result


for x in cursor:
    print(x)
