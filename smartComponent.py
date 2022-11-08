import time

from transitions import Machine
import uuid
from robotConstructionActions import robotConstructionActionNode as rca


class SmartComponentStates(object):
    def __init__(self, states, transitions):
        self.id = uuid.uuid4()
        self.success = False
        self.state_machine = Machine(model=self, states=states, transitions=transitions, initial=states[0]['name'],
                                     ignore_invalid_triggers=True)

    def execute_moving_action(self):
        oneNode = rca.RobotConstructionActionNode('move_action')
        oneNode.start_execution()
        oneNode.finish_execution()
        if oneNode.state == 'executed':
            self.success = True

    def execute_positioning_action(self):
        oneNode = rca.RobotConstructionActionNode('positioning_action')
        oneNode.start_execution()
        oneNode.finish_execution()
        if oneNode.state == 'executed':
            self.success = True

    def execute_pickup_action(self):
        oneNode = rca.RobotConstructionActionNode('pickup_action')
        oneNode.start_execution()
        oneNode.finish_execution()
        if oneNode.state == 'executed':
            self.success = True

    def execute_assembly_action(self):
        oneNode = rca.RobotConstructionActionNode('assembly_action')
        oneNode.start_execution()
        oneNode.finish_execution()
        if oneNode.state == 'executed':
            self.success = True

    def is_execution_success(self):
        print('The execute result is', self.success)
        return self.success

    def reset_success(self):
        self.success = False


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

    transitions_test = [
        {'trigger': 'start_work', 'source': 'need construction', 'dest': 'need positioning for picking up',
         'prepare': ['execute_moving_action'], 'conditions': 'is_execution_success'},
        {'trigger': 'start_positioning_for_pickup', 'source': 'need positioning for picking up', 'dest': 'need pick up',
         'prepare': ['execute_positioning_action'], 'conditions': 'is_execution_success'},
        {'trigger': 'start_pickup', 'source': 'need pick up', 'dest': 'need transfer to target',
         'prepare': ['execute_pickup_action'], 'conditions': 'is_execution_success'},
        {'trigger': 'start_transfer', 'source': 'need transfer to target', 'dest': 'need positioning for assembling',
         'prepare': ['execute_moving_action'], 'conditions': 'is_execution_success'},
        {'trigger': 'start_positioning_for_assembly', 'source': 'need positioning for assembling',
         'dest': 'need assembly',
         'prepare': ['execute_positioning_action'], 'conditions': 'is_execution_success'},
        {'trigger': 'start_assembly', 'source': 'need assembly', 'dest': 'constructed',
         'prepare': ['execute_assembly_action'], 'conditions': 'is_execution_success'},
    ]

    smartComponent = SmartComponentStates(states_test, transitions_test)

    while smartComponent.state != 'constructed':
        print(smartComponent.state)
        print('\n')

        while smartComponent.success is False:
            smartComponent.start_work()
        smartComponent.reset_success()
        print('\n')

        while smartComponent.success is False:
            smartComponent.start_positioning_for_pickup()
        smartComponent.reset_success()
        print('\n')

        while smartComponent.success is False:
            smartComponent.start_pickup()
        smartComponent.reset_success()
        print('\n')

        while smartComponent.success is False:
            smartComponent.start_transfer()
        smartComponent.reset_success()
        print('\n')

        while smartComponent.success is False:
            smartComponent.start_positioning_for_assembly()
        smartComponent.reset_success()
        print('\n')

        while smartComponent.success is False:
            smartComponent.start_assembly()
        smartComponent.reset_success()
        print('\n')

        print(smartComponent.state)
