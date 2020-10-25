from app.model.context.HireMeContext import HireMeContext
from app.repository.selectiveprocessapproval import ApprovalSelectiveProcessRepository


def approve(request, approved_step_id):
    context = HireMeContext()
    context.build(request)

    next_step_id = get_next_step_by_current_step(approved_step_id)

    ApprovalSelectiveProcessRepository.change_status_to_approved(approved_step_id)
    ApprovalSelectiveProcessRepository.insert_new_step(next_step_id, approved_step_id)


def get_next_step_by_current_step(approved_step_id):
    return ApprovalSelectiveProcessRepository.get_next_step_by_current_step(approved_step_id)


def has_more_steps(approved_step_id):
    return not get_next_step_by_current_step(approved_step_id) is None


def reject(approved_step_id):
    ApprovalSelectiveProcessRepository.reject(approved_step_id)
