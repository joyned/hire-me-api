from app.model.context.HireMeContext import HireMeContext
from app.model.email.EmailMessage import EmailMessage
from app.repository.selectiveprocessapproval import ApprovalSelectiveProcessRepository
from app.service.email import EmailService


def approve(request, approved_step_id):
    context = HireMeContext()
    context.build(request)

    next_step_id = get_next_step_by_current_step(approved_step_id)

    ApprovalSelectiveProcessRepository.change_status_to_approved(approved_step_id)

    if next_step_id is not None and next_step_id[0] is not None:
        ApprovalSelectiveProcessRepository.insert_new_step(next_step_id[0], approved_step_id)

    send_approval_email(approved_step_id)


def get_next_step_by_current_step(approved_step_id):
    return ApprovalSelectiveProcessRepository.get_next_step_by_current_step(approved_step_id)


def has_more_steps(approved_step_id):
    return not get_next_step_by_current_step(approved_step_id) is None


def reject(approved_step_id):
    ApprovalSelectiveProcessRepository.reject(approved_step_id)
    send_reproval_email(approved_step_id)


def can_approve(approved_step_id):
    return ApprovalSelectiveProcessRepository.can_approve(approved_step_id) is not None


def send_approval_email(approved_step_id):
    info_to_email = ApprovalSelectiveProcessRepository.get_info_to_email(approved_step_id)
    email_body = """
        <h1>Parabéns!!!</h1>
       <p>Você acabou de ser aprovado no passo <b>{0}</b> da vaga <b>{1}</b>.</p>
       <p>Acesse nosso sistema e veja os próximos passos para o processo seletivo dessa vaga.</p>
       <br>
       <br>
       <br>
       <p>Atenciosamente,</p>
       <b>Equipe HireMe</b>
    """.format(info_to_email[0], info_to_email[1])

    send_email(email_body, info_to_email[2], info_to_email[1])


def send_reproval_email(approved_step_id):
    info_to_email = ApprovalSelectiveProcessRepository.get_info_to_email(approved_step_id)
    email_body = """
        <b>Temos uma triste noticia. :(</b>
		<p>Infelizmente, você foi reprovado no passo <b>Questionário</b> da vaga <b>Programador Jr</b>.</p>
		<p>Não desista, acesso nosso sistema e veja outras oportunidades.</p>
		<br>
		<br>
		<p>Atenciosamente,</p>
		<b>Equipe HireMe</b>
        """.format(info_to_email[0], info_to_email[1])

    send_email(email_body, info_to_email[2], info_to_email[1])


def send_email(email_body, to, job_name):
    email_message = EmailMessage()

    email_message.to = to
    email_message.body = email_body
    email_message.subject = job_name + ' - Processo seletivo'
    email_message.from_email = 'noreply@hireme.com'

    EmailService.send_email(email_message)
