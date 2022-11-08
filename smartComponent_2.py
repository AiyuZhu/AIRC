import uuid
from operator import methodcaller
from transitions import Machine
from robotConstructionActions import robotConstructionActionNode as rcan


class SmartComponentStates(object):
    def __init__(self, states):
        self.id = uuid.uuid4()
        self.success = False
        self.state_machine = Machine(model=self, states=states, initial=states[0]['name'],
                                     ignore_invalid_triggers=True)
        self.state_machine.add_ordered_transitions()

    def is_execution_success(self, execute_result):
        if execute_result == 'executed':
            self.success = True
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

    transitions = [
        'move_to_component',
        'positioning_for_pickup',
        'pickup',
        'transfer',
        'positioning_for_assembly',
        'assembly',
    ]

    smartComponent = SmartComponentStates(states_test)

    while smartComponent.state != 'constructed':
        for i in transitions:
            while smartComponent.success is False:
                comp_state = rcan.RobotConstructionActionNode(i)
                comp_state.start_execution()
                comp_state.finish_execution()
                smartComponent.is_execution_success(comp_state.state)
            smartComponent.next_state()
            smartComponent.reset_success()
            print(smartComponent.state)
            print('\n')



