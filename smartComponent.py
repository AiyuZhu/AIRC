from transitions import Machine
import uuid
import random
from ActionNode_callback_test_1 import RobotConstructionActionNode


class SmartComponentStates(object):
    def __init__(self, states, transitions):
        self.id = uuid.uuid4()
        self.success = False
        self.state_machine = Machine(model=self, states=states, transitions=transitions, initial=states[0]['name'],
                                     ignore_invalid_triggers=True)

    def execute_move_action(self):
        print("Moving to target")
        self.success = random.random() < 0.5

    def execute_positioning_action(self):
        print("Doing positioning")
        self.success = random.random() < 0.5

    def execute_pickup_action(self):
        print("Doing pick up work")
        self.success = random.random() < 0.5

    def execute_assemble_action(self):
        print("Doing assembling work")
        self.success = random.random() < 0.5

    def execution_success(self):
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
         'prepare': ['execute_move_action'], 'conditions': 'execution_success'},
        {'trigger': 'start_positioning_for_pickup', 'source': 'need positioning for picking up', 'dest': 'need pick up',
         'prepare': ['execute_positioning_action'], 'conditions': 'execution_success'},
        {'trigger': 'start_pickup', 'source': 'need pick up', 'dest': 'need transfer to target',
         'prepare': ['execute_pickup_action'], 'conditions': 'execution_success'},
        {'trigger': 'start_transfer', 'source': 'need transfer to target', 'dest': 'need positioning for assembling',
         'prepare': ['execute_move_action'], 'conditions': 'execution_success'},
        {'trigger': 'start_positioning_for_assembly', 'source': 'need positioning for assembling',
         'dest': 'need assembly',
         'prepare': ['execute_positioning_action'], 'conditions': 'execution_success'},
        {'trigger': 'start_assembly', 'source': 'need assembly', 'dest': 'constructed',
         'prepare': ['execute_assemble_action'], 'conditions': 'execution_success'},
    ]

    smartComponent = SmartComponentStates(states_test, transitions_test)
    while smartComponent.success is False:
        smartComponent.start_work()
    smartComponent.reset_success()
    # print(smartComponent.state)
    while smartComponent.success is False:
        smartComponent.start_positioning_for_pickup()
