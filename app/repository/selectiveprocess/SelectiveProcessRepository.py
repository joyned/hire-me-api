import app.database.database as db
from app.model.context.HireMeContext import HireMeContext
from app.model.selectiveprocess import SelectiveProcess
from app.model.selectiveprocess.SelectiveProcessStep import SelectiveProcessStep


def create_selective_process(selective_process: SelectiveProcess, context: HireMeContext):
    sql = """
        INSERT INTO ProcessoSeletivo (Titulo, Id_Empresa, Id_Usuario)
            VALUES(%s, %d, %d)
    """

    param = (selective_process.title, context.company_id, context.user_id)

    return db.execute_insert(sql, param)


def create_selective_process_steps(step: SelectiveProcessStep):
    sql = """
    INSERT INTO EtapasProcessoSeletivo (Titulo_Etapa, Descricao_Etapa, Tipo_Etapa, Id_Questionario, Id_Processo_Seletivo)
        VALUES(%s, %s, %s, %d, %d)
    """

    param = (step.step_title, step.step_description, step.step_type, step.questionnaire_id, step.selective_process_id)

    db.execute_insert(sql, param)


def list_selective_process_common_sql():
    return """
            SELECT  Id,
                    Titulo
            FROM ProcessoSeletivo
            WHERE Id_Empresa = %d
            AND Id_Usuario = %d
        """


def list_selective_process(context):
    sql = list_selective_process_common_sql()

    param = (context.company_id, context.user_id)

    return db.execute_query_fetchall(sql, param)


def list_selective_process_by_id(context, selective_process_id):
    sql = list_selective_process_common_sql()

    sql += " AND Id = %d"

    param = (context.company_id, context.user_id, selective_process_id)

    return db.execute_query_fetchall(sql, param)


def list_selective_process_step(selective_process_id):
    sql = """
        SELECT  Id,
                Titulo_Etapa,
                Descricao_Etapa,
                Tipo_Etapa,
                Id_Questionario,
                Id_Processo_Seletivo
        FROM    EtapasProcessoSeletivo
        WHERE   Id_Processo_Seletivo = 2
    """

    param = (selective_process_id)

    return db.execute_query_fetchall(sql, param)
