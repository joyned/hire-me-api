import app.database.Database as db
from app.model.messages.Messages import Messages


def insert_new_message(message: Messages):
    sql = """
        INSERT INTO Mensagens (Id_De, Id_Para, Mensagem, Data_Envio, Id_Sala)
            VALUES(?,?,?,GETDATE(),?)
    """

    param = (message.from_id, message.to_id, message.message, message.room_id)

    db.execute_insert(sql, param)


def get_room_id(from_id, to_id):
    sql = """
        SELECT Id_Sala
        FROM Mensagens
        WHERE Id_De = ?
        AND Id_Para = ?
    """

    param = (from_id, to_id)

    return db.execute_query_fetchall(sql, param)


def get_messages(from_id, to_id):
    sql = """
        SELECT  Mensagens.Id,
                Mensagens.Id_De,
                De.Nome De_Nome,
                Mensagens.Id_Para,
                Para.Nome Para_Nome,
                Mensagens.Mensagem,
                Mensagens.Data_Envio,
                Mensagens.Id_Sala
        FROM Mensagens
        JOIN Pessoa De
            ON De.Id = Mensagens.Id_De
        JOIN Pessoa Para
            ON Para.Id = Mensagens.Id_Para
        WHERE 
        (Mensagens.Id_De = ?
        AND Mensagens.Id_Para = ?)
        OR
        (Mensagens.Id_De = ?
        AND Mensagens.Id_Para = ?)
        ORDER BY Mensagens.Data_Envio
    """

    param = (from_id, to_id, to_id, from_id)

    return db.execute_query_fetchall(sql, param)


def list_candidate_messages(person_id):
    sql = """
        SELECT  Pessoa.Nome,
                Mensagens.Id_Sala
        FROM Mensagens
        JOIN Pessoa
        ON Pessoa.Id = Mensagens.Id_De
        WHERE Mensagens.Id_Para = ?
        GROUP BY Mensagens.Id_Sala, Pessoa.Nome
    """

    param = (person_id,)

    return db.execute_query_fetchall(sql, param)


def get_candidate_messages_by_room_id(room_id):
    sql = """
        SELECT  Mensagens.Id,
                Mensagens.Id_De,
                De.Nome De_Nome,
                Mensagens.Id_Para,
                Para.Nome Para_Nome,
                Mensagens.Mensagem,
                Mensagens.Data_Envio,
                Mensagens.Id_Sala
        FROM Mensagens
        JOIN Pessoa De
            ON De.Id = Mensagens.Id_De
        JOIN Pessoa Para
            ON Para.Id = Mensagens.Id_Para
        WHERE Mensagens.Id_Sala = ?
        ORDER BY Mensagens.Data_Envio DESC
    """

    param = (room_id,)

    return db.execute_query_fetchall(sql, param)


def get_person_id_by_room_id(room_id, context):
    sql = """
        SELECT Id_De 
        FROM Mensagens 
        WHERE Id_Sala = ? 
        AND Id_De <> ?
        GROUP BY Id_De
    """

    param = (room_id, context.person_id)

    return db.execute_query_fetchone(sql, param)
