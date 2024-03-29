import app.database.Database as db
from app.model.context.HireMeContext import HireMeContext
from app.model.selectiveprocess import SelectiveProcess
from app.model.selectiveprocess.SelectiveProcessStep import SelectiveProcessStep


def create_selective_process(selective_process: SelectiveProcess, context: HireMeContext):
    sql = """
        INSERT INTO ProcessoSeletivo (Titulo, Id_Empresa, Id_Usuario)
            VALUES(?, ?, ?)
    """

    param = (selective_process.title, context.company_id, context.user_id)

    return db.execute_insert(sql, param)


def create_selective_process_steps(step: SelectiveProcessStep):
    sql = """
    INSERT INTO EtapasProcessoSeletivo (Titulo_Etapa, Descricao_Etapa, Tipo_Etapa, Id_Questionario, Id_Processo_Seletivo, Ordem)
        VALUES(?, ?, ?, ?, ?, ?)
    """

    param = (step.step_title, step.step_description, step.step_type, step.questionnaire_id, step.selective_process_id, step.order)

    return db.execute_insert(sql, param)


def delete_seletive_process(selective_process_id):
    sql = """
        DELETE FROM ProcessoSeletivo WHERE Id = ?
    """

    param = (selective_process_id)

    db.execute_delete(sql, param)


def delete_selective_process_steps(selective_process_id):
    sql = """
        DELETE FROM EtapasProcessoSeletivo WHERE Id_Processo_Seletivo = ?
    """

    param = (selective_process_id)

    db.execute_delete(sql, param)


def list_selective_process_common_sql():
    return """
            SELECT  Id,
                    Titulo
            FROM ProcessoSeletivo
            WHERE Id_Empresa = ?
            AND Id_Usuario = ?
        """


def list_selective_process(context):
    sql = list_selective_process_common_sql()

    param = (context.company_id, context.user_id)

    return db.execute_query_fetchall(sql, param)


def list_selective_process_by_id(context, selective_process_id):
    sql = list_selective_process_common_sql()

    sql += " AND Id = ?"

    param = (context.company_id, context.user_id, selective_process_id)

    return db.execute_query_fetchall(sql, param)


def list_selective_process_step(selective_process_id):
    sql = """
        SELECT  Id,
                Titulo_Etapa,
                Descricao_Etapa,
                Tipo_Etapa,
                Id_Questionario,
                Id_Processo_Seletivo,
                Ordem
        FROM    EtapasProcessoSeletivo
        WHERE   Id_Processo_Seletivo = ?
        ORDER BY Ordem
    """

    param = (selective_process_id)

    return db.execute_query_fetchall(sql, param)


def selective_process_editable(selective_process_id):
    sql = """
        SELECT 1
        FROM Vaga 
        WHERE Id_Processo_Seletivo = ?
    """

    param = (selective_process_id,)

    return db.execute_query_fetchall(sql, param)


def get_selective_process_by_job_id(person_id, job_id):
    sql = """
        SELECT  EtapasProcessoSeletivo.Titulo_Etapa,
                EtapasProcessoSeletivo.Descricao_Etapa,
                EtapasProcessoSeletivo.Tipo_Etapa,
                EtapasProcessoSeletivo.Id_Questionario,
                EtapasProcessoSeletivo.Ordem,
                ProcessoSeletivoAprovacao.Status,
                ProcessoSeletivoAprovacao.Id
        FROM    EtapasProcessoSeletivo
        LEFT JOIN ProcessoSeletivoAprovacao
        ON ProcessoSeletivoAprovacao.Id_Etapa = EtapasProcessoSeletivo.Id
        AND ProcessoSeletivoAprovacao.Id_Vaga = ?
        AND ProcessoSeletivoAprovacao.Id_Pessoa = ?
        WHERE EtapasProcessoSeletivo.Id_Processo_Seletivo = (
            SELECT  Vaga.Id_Processo_Seletivo
            FROM    Vaga
            WHERE   Vaga.Id = ?
        )
        ORDER BY EtapasProcessoSeletivo.Ordem
    """

    param = (job_id, person_id, job_id)

    return db.execute_query_fetchall(sql, param)


def get_candidates(job_id):
    sql = """
        SELECT  Pessoa.Id,
                Pessoa.Nome,
                VagasAplicadas.Data_Aplicacao,
                ProcessoSeletivoAprovacao.[Status],
                MAX(ProcessoSeletivoAprovacao.Data_Aprovacao)
        FROM    VagasAplicadas
        INNER JOIN Pessoa
        ON Pessoa.Id = VagasAplicadas.Id_Pessoa
        LEFT JOIN ProcessoSeletivoAprovacao
        ON ProcessoSeletivoAprovacao.Id_Vaga = ?
        AND ProcessoSeletivoAprovacao.Id_Pessoa = Pessoa.Id
        AND ProcessoSeletivoAprovacao.Id IN (
            SELECT MAX(id) 
            FROM   ProcessoSeletivoAprovacao
            GROUP BY Id_Vaga, Id_Pessoa, Id_Processo_Seletivo
        )
        WHERE VagasAplicadas.Id_Vaga = ?
        GROUP BY Pessoa.Id, Pessoa.Nome, VagasAplicadas.Data_Aplicacao, ProcessoSeletivoAprovacao.[Status]
        ORDER BY Nome
    """

    param = (job_id, job_id)

    return db.execute_query_fetchall(sql, param)
