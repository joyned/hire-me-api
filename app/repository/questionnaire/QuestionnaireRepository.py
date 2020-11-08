from app.database import Database as db
from app.model.context.HireMeContext import HireMeContext


def create_questionnaire(context: HireMeContext, questionnaire):
    sql = """
        INSERT INTO Questionario (Titulo_Questionario, Status, Data_Criacao, Id_Empresa, Id_Usuario)
            VALUES (?, ?, GETDATE(), ?, ?)
    """

    param = (questionnaire.title, 'T', context.company_id, context.user_id)

    questionnaire.id = db.execute_insert(sql, param)

    if not questionnaire.questionnaire_questions is None:
        for question in questionnaire.questionnaire_questions:
            question.questionnaire_id = questionnaire.id

            sql = """
                INSERT INTO QuestionarioQuestao (Id_Questionario, Titulo_Questao, Titulo_Ajuda, Tipo_Resposta, Tempo_Resposta)
                    VALUES (?, ?, ?, ?, ?)
            """

            param = (question.questionnaire_id, question.question_title, question.question_help, question.answer_type,
                     question.answer_time)

            question.id = db.execute_insert(sql, param)

            if not question.questionnaire_question_options is None:
                for option in question.questionnaire_question_options:
                    option.questionnaire_question_id = question.id

                    sql = """
                        INSERT INTO QuestionarioQuestaoOpcao (Titulo_Opcao, Id_Questionario_Questao)
                            VALUES (?, ?)
                    """

                    param = (option.option_title, option.questionnaire_question_id)

                    db.execute_insert(sql, param)
    return questionnaire.id


def delete_questionnaire(questionnaire_id):
    sql = """
        DELETE FROM Questionario WHERE Id = ?
    """

    param = (questionnaire_id)

    db.execute_delete(sql, param)


def delete_question_by_questionnaire_id(questionnaire_id):
    sql = """
        DELETE FROM QuestionarioQuestao WHERE Id_Questionario = ?
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
                WHERE Id_Questionario = ?
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
        WHERE Id_Empresa = ? 
        AND Id_Usuario = ?
    """

    param = (context.company_id, context.user_id)

    return db.execute_query_fetchall(sql, param)


def get_questionnaire_by_id(context: HireMeContext, questionnaire_id, for_view):
    sql = """
        SELECT  Titulo_Questionario,
                Id_Empresa,
                Id_Usuario
        FROM Questionario
        WHERE Id = ?
    """
    if for_view:
        sql += """
            AND Id_Empresa = ?
            AND Id_Usuario = ?
        """
        param = (questionnaire_id, context.company_id, context.user_id)
    else:
        param = (questionnaire_id)

    return db.execute_query_fetchone(sql, param)


def get_questionnaire_question_by_id(questionnaire_id, approval_id):
    sql = """
        SELECT  QuestionarioQuestao.Id,
                QuestionarioQuestao.Titulo_Questao,
                QuestionarioQuestao.Titulo_Ajuda,
                QuestionarioQuestao.Tipo_Resposta
    """

    if approval_id is not None:
        sql += """
                ,QuestionarioQuestaoResposta.Resposta
            FROM QuestionarioQuestao
            LEFT JOIN QuestionarioQuestaoResposta 
            ON QuestionarioQuestaoResposta.Id_Questao = QuestionarioQuestao.Id
            AND QuestionarioQuestaoResposta.Id_Processo_Aprovacao = ?
             WHERE QuestionarioQuestao.Id_Questionario = ?
        """
        param = (approval_id, questionnaire_id)
        return db.execute_query_fetchall(sql, param)
    else:
        sql += """
              FROM QuestionarioQuestao
              WHERE QuestionarioQuestao.Id_Questionario = ?  
        """
        param = (questionnaire_id)
        return db.execute_query_fetchall(sql, param)


def get_questionnaire_by_job_id_and_person_id(job_id, person_id):
    sql = """
        SELECT  QuestionarioQuestao.Id,
                QuestionarioQuestao.Titulo_Questao,
                QuestionarioQuestao.Titulo_Ajuda,
                QuestionarioQuestao.Tipo_Resposta,
                QuestionarioQuestaoResposta.Resposta,
                QuestionarioQuestaoResposta.Id Id_Resposta,
                QuestionarioQuestaoRespostaCorrecao.Correto
        FROM QuestionarioQuestao
        INNER JOIN QuestionarioQuestaoResposta
        ON QuestionarioQuestaoResposta.Id_Questao = QuestionarioQuestao.Id
        INNER JOIN (
            SELECT  EtapasProcessoSeletivo.Id_Questionario,
                    ProcessoSeletivoAprovacao.Id Id_Processo_Aprovacao
            FROM    EtapasProcessoSeletivo
            JOIN ProcessoSeletivoAprovacao
            ON ProcessoSeletivoAprovacao.Id_Etapa = EtapasProcessoSeletivo.Id
            AND ProcessoSeletivoAprovacao.Id_Vaga = ?
            AND ProcessoSeletivoAprovacao.Id_Pessoa = ?
        ) AS QuestionarioProcesoAprovacao
        ON QuestionarioProcesoAprovacao.Id_Questionario = QuestionarioQuestao.Id_Questionario
        AND QuestionarioQuestaoResposta.Id_Processo_Aprovacao = QuestionarioProcesoAprovacao.Id_Processo_Aprovacao
        LEFT JOIN QuestionarioQuestaoRespostaCorrecao
        ON QuestionarioQuestaoRespostaCorrecao.Id_Resposta = QuestionarioQuestaoResposta.Id
    """

    param = (job_id, person_id)

    return db.execute_query_fetchall(sql, param)


def get_questionnaire_question_options_by_id(question_id):
    sql = """
        SELECT  Id,
                Titulo_Opcao
        FROM QuestionarioQuestaoOpcao
        WHERE Id_Questionario_Questao = ?
    """

    param = (question_id)

    return db.execute_query_fetchall(sql, param)


def questionnaire_editable(questionnaire_id):
    sql = """
        SELECT 1 FROM EtapasProcessoSeletivo WHERE Id_Questionario = ?
    """

    param = (questionnaire_id,)

    return db.execute_query_fetchall(sql, param)


def answer_questionnaire(questionnaire_answer):
    sql = """
    INSERT INTO QuestionarioQuestaoResposta (Id_Processo_Aprovacao, Id_Questao, Resposta)
        VALUES (?, ?, ?)
    """

    param = (questionnaire_answer.get('process_approval_id'), questionnaire_answer.get('question_id'),
             questionnaire_answer.get('answer'))

    db.execute_insert(sql, param)


def change_status_to_pending_approval(approval_id):
    sql = """
        UPDATE ProcessoSeletivoAprovacao SET [Status] = 'G' WHERE Id = ?
    """

    param = (approval_id)

    db.execute_update(sql, param)


def check_if_can_answer_questionnaire(approval_id):
    sql = """
        SELECT 1 FROM QuestionarioQuestaoResposta WHERE Id_Processo_Aprovacao = ?
    """
    param = (approval_id)

    return db.execute_query_fetchone(sql, param)


def correct_questionnaire(question_answer):
    sql = """
        INSERT INTO QuestionarioQuestaoRespostaCorrecao (Id_Resposta, Correto)
            VALUES(?, ?)
    """

    param = (question_answer.get('answerId'), question_answer.get('correct'))

    db.execute_insert(sql, param)
