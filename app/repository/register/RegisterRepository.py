from app.database import Database as db
from app.model.person.Person import Person


def register_new_user(person: Person):
    sql = """
        INSERT INTO Usuario (Email, Senha, Id_Perfil_Usuario)
        VALUES (?, ?, ?)
    """

    param = (person.user.email, person.user.password, 1)

    user_id = db.execute_insert(sql, param)

    sql = """
        INSERT INTO Pessoa (Id_Usuario, Nome, Nome_Completo, CPF, RG, Data_Nascimento, Cidade, Estado, Pais, Foto)
            VALUES (?,?,?,?,?,?,?,?,?,?)
    """

    param = (user_id, person.name, person.fullname, person.cpf, person.rg, person.birthdate, person.city, person.state,
             person.country, person.photo)

    person_id = db.execute_insert(sql, param)

    sql = """
        INSERT INTO PessoaEndereco (Id_Pessoa, Endereco, Numero, CEP, Complemento)
            VALUES (?, ?, CONVERT(NUMERIC, ?), CONVERT(NUMERIC, ?), ?)
    """

    param = (person_id, person.person_addres.address, person.person_addres.number, person.person_addres.cep,
             person.person_addres.complement)

    db.execute_insert(sql, param)

    return person_id


def check_if_email_exists(email):
    sql = """
    SELECT 1 FROM Usuario WHERE email = ?
    """

    return db.execute_query_fetchone(sql, (email))


def insert_person_professional_history(professional_history):
    sql = """    
        INSERT INTO PessoaHistoricoProfissional (Id_Pessoa, Empresa, Cargo, Descricao, Data_Entrada, Data_Saida, Trabalha_Atualmente)
            VALUES(?,?,?,?,?,?,?)
    """

    return db.execute_insert(sql, professional_history)


def insert_person_ability(person_ability):
    sql = """
        INSERT INTO PessoaHabilidades(Id_Pessoa, Habilidade)
            VALUES (?,?)
    """

    db.execute_insert(sql, person_ability)
