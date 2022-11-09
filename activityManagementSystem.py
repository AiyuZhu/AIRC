import uuid
from robotConstructionActions import robotConstructionActionNode as rcan
import smartComponent_2 as sc


class ActivityManagementSystem(object):
    def __init__(self, smart_component):
        self.id = uuid.uuid4()
        self.smart_component = smart_component

    def auto_construction(self):
        while self.smart_component.current_state != 'constructed':
            for activity in self.smart_component.activities:
                while self.smart_component.component_stateMachine.success is False:
                    activity_state = rcan.RobotConstructionActionNode(self.smart_component.guid,
                                                                      activity,
                                                                      self.smart_component.activities)
                    self.smart_component.component_stateMachine.is_execution_success(
                        activity_state.execute_robot_simulation())
                self.smart_component.component_stateMachine.next_state()
                self.smart_component.current_state = self.smart_component.component_stateMachine.state
                self.smart_component.component_stateMachine.reset_success()
                print('\n')

    def return_component_state(self):
        return self.smart_component.current_state


if __name__ == '__main__':
    states_test = [
        {'name': 'need construction'},
        {'name': 'need positioning for picking up'},
        {'name': 'need pick up'},
        {'name': 'need transfer to target'},
        {'name': 'need positioning for assembling'},
        {'name': 'need assembly'},
        {'name': 'constructed'},
    ]

    activities = {'move_to_component': [1, 2, 3],
                  'positioning_for_pickup': [2, 3, 4],
                  'pickup': [3, 4, 5],
                  'transfer': [4, 5, 6],
                  'positioning_for_assembly': [5, 6, 7],
                  'assembly': [7, 8, 9]}

    robot_namespaces = {'move_to_component': 'mobile_base',
                        'positioning_for_pickup': 'manipulator',
                        'pickup': 'gripper',
                        'transfer': 'mobile_base',
                        'positioning_for_assembly': 'manipulator',
                        'assembly': 'gripper'}

    comp_1 = sc.SmartComponent('267VPu8ab9991QBA3MI1qr', states_test, activities)
    activity_1 = ActivityManagementSystem(comp_1)
    activity_1.auto_construction()
    print(activity_1.return_component_state())
