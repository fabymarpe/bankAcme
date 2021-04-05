from managers.WorkFlowStepManager import WorkFlowStepManager


class WorkFlowStepController:

    def get_workflow_step(self, workflow_id, step_id):

        filters = {"workflow_id": workflow_id, 'id': step_id}
        return WorkFlowStepManager().get(filters)
