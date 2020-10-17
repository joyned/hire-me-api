from app.database import database as db
from app.model.context.HireMeContext import HireMeContext


def create_questionnaire(context: HireMeContext, questionnaire):
    sql = """
        INSERT INTO Questionario (Titulo_Questionario, Status, Data_Criacao, Id_Empresa, Id_Usuario)
            VALUES (%s, %s, GETDATE(), %d, %d)
    """

    param = (questionnaire.title, 'T', context.company_id, context.user_id)

    questionnaire.id = db.execute_insert(sql, param)

    if not questionnaire.questionnaire_questions is None:
        for question in questionnaire.questionnaire_questions:
            question.questionnaire_id = questionnaire.id

            sql = """
                INSERT INTO QuestionarioQuestao (Id_Questionario, Titulo_Questao, Titulo_Ajuda, Tipo_Resposta, Tempo_Resposta)
                    VALUES (%d, %s, %s, %s, %d)
            """

            param = (question.questionnaire_id, question.question_title, question.question_help, question.answer_type,
                     question.answer_time)

            question.id = db.execute_insert(sql, param)

            if not question.questionnaire_question_options is None:
                for option in question.questionnaire_question_options:
                    option.questionnaire_question_id = question.id

                    sql = """
                        INSERT INTO QuestionarioQuestaoOpcao (Titulo_Opcao, Id_Questionario_Questao)
                            VALUES (%s, %d)
                    """

                    param = (option.option_title, option.questionnaire_question_id)

                    db.execute_insert(sql, param)
    return questionnaire.id


def delete_questionnaire(questionnaire_id):
    sql = """
        DELETE FROM Questionario WHERE Id = %d
    """

    param = (questionnaire_id)

    db.execute_delete(sql, param)


def delete_question_by_questionnaire_id(questionnaire_id):
    sql = """
        DELETE FROM QuestionarioQuestao WHERE Id_Questionario = %d
    """

    param = (questionnaire_id)

    db.execute_delete(sql, param)


def delete_option_by_questionnaire_id(questionnaire_id):
    sql = """
        DELETE FROM QuestionarioQuestaoOpcao
        WHERE Id IN (
            SELECT  Id 
            FROM    QuestionarioQuestaoOpcao 
            WHERE Id_Questionario_Questao IN (
                SELECT  Id 
                FROM    QuestionarioQuestao 
                WHERE Id_Questionario = %d
            )
        )
    """

    param = (questionnaire_id)

    db.execute_delete(sql, param)


def list_questionnaires_simple(context: HireMeContext):
    sql = """
        SELECT  Id,
                Titulo_Questionario, 
                Status 
        FROM    Questionario 
        WHERE Id_Empresa = %d 
        AND Id_Usuario = %d
    """

    param = (context.company_id, context.user_id)

    return db.execute_query_fetchall(sql, param)


def get_questionnaire_by_id(context: HireMeContext, questionnaire_id):
    sql = """
        SELECT  Titulo_Questionario,
                Id_Empresa,
                Id_Usuario
        FROM Questionario
        WHERE Id = %d
        AND Id_Empresa = %d
        AND Id_Usuario = %d
    """

    param = (questionnaire_id, context.company_id, context.user_id)

    return db.execute_query_fetchone(sql, param)


def get_questionnaire_question_by_id(questionnaire_id):
    sql = """
        SELECT  Id,
                Titulo_Questao,
                Titulo_Ajuda,
                Tipo_Resposta
        FROM QuestionarioQuestao
        WHERE Id_Questionario = %d
    """

    param = (questionnaire_id)

    return db.execute_query_fetchall(sql, param)


def get_questionnaire_question_options_by_id(question_id):
    sql = """
        SELECT  Id,
                Titulo_Opcao
        FROM QuestionarioQuestaoOpcao
        WHERE Id_Questionario_Questao = %d
    """

    param = (question_id)

    return db.execute_query_fetchall(sql, param)


def questionnaire_editable(questionnaire_id):
    sql = """
        SELECT 1 FROM EtapasProcessoSeletivo WHERE Id_Questionario = %d
    """

    param = (questionnaire_id)

    return db.execute_count_lines(sql, param)
