import app.database.Database as db


def get_next_step_by_current_step(approved_step_id):
    sql = """
        SELECT EtapasProcessoSeletivo.Id
        FROM   EtapasProcessoSeletivo
        WHERE EtapasProcessoSeletivo.Ordem = 
        (
                SELECT EtapasProcessoSeletivo.Ordem + 1
                FROM EtapasProcessoSeletivo
                JOIN ProcessoSeletivoAprovacao
                ON ProcessoSeletivoAprovacao.Id_Etapa = EtapasProcessoSeletivo.Id
                AND ProcessoSeletivoAprovacao.Id = %d
        )
        AND EtapasProcessoSeletivo.Id_Processo_Seletivo = (
            SELECT  ProcessoSeletivoAprovacao.Id_Processo_Seletivo 
            FROM    ProcessoSeletivoAprovacao 
            WHERE Id = %d
        )
    """

    param = (approved_step_id, approved_step_id)

    return db.execute_query_fetchone(sql, param)


def change_status_to_approved(approved_step_id):
    sql = """
        UPDATE ProcessoSeletivoAprovacao SET [Status] = 'A', Data_Aprovacao = GETDATE() WHERE Id = %d
    """

    param = (approved_step_id)

    db.execute_update(sql, param)


def insert_new_step(next_step_id, approved_step_id):
    sql = """
        INSERT INTO ProcessoSeletivoAprovacao (Id_Vaga, Id_Pessoa, Id_Processo_Seletivo, Id_Etapa, [Status])
        SELECT Id_Vaga, Id_Pessoa, Id_Processo_Seletivo, %d, 'P' FROM ProcessoSeletivoAprovacao WHERE Id = %d
    """

    param = (next_step_id, approved_step_id)

    db.execute_insert(sql, param)


def reject(approved_step_id):
    sql = """
            UPDATE ProcessoSeletivoAprovacao SET [Status] = 'R', Data_Aprovacao = GETDATE() WHERE Id = %d
        """

    param = (approved_step_id)

    db.execute_update(sql, param)


def can_approve(approved_step_id):
    sql = """
        SELECT  1 
        FROM    QuestionarioQuestaoRespostaCorrecao
        WHERE Id_Resposta IN (
            SELECT Id
            FROM QuestionarioQuestaoResposta
            WHERE Id_Processo_Aprovacao = %d
        )
    """
    if approved_step_id is not None:
        param = (approved_step_id)
        return db.execute_query_fetchone(sql, param)
    else:
        return False
