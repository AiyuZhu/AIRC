from transitions import Machine, State
import uuid
import random


class RobotConstructionActionNode(object):
    success = False
    attempts = 0

    def __init__(self):
        self.id = uuid.uuid4()

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

    def count_attempts(self): self.attempts += 1

    def stats(self): print('It took you %i attempts to success!' % self.attempts)


robotAction = RobotConstructionActionNode()

# Same states as above, but now we give StateA an exit callback
states = [
    State(name='need construction'),
    State(name='need positioning for picking up'),
    State(name='need pick up'),
]

transitions = [
    {'trigger': 'move_to_component', 'source': 'need construction', 'dest': 'need positioning for picking up',
     'prepare': ['execute_move_action'], 'conditions': 'execution_success'},
    {'trigger': 'position_pickup', 'source': 'need positioning for picking up', 'dest': 'need pick up',
     'prepare': ['execute_positioning_action'], 'conditions': 'execution_success'}
]

machine = Machine(robotAction, states=states, transitions=transitions, initial='need construction')
# machine.add_transition('move_to_component', 'need construction', 'need positioning for picking up',
#                        conditions='execute_move_action')
# machine.add_transition('position_pickup', 'need positioning for picking up', 'need pick up',
#                        conditions='execute_positioning_action')

# Callbacks can also be added after initialization using
# the dynamically added on_enter_ and on_exit_ methods.
# Note that the initial call to add the callback is made
# on the Machine and not on the model.
# machine.on_exit_need_construction('position_pickup_point')


if __name__ == '__main__':
    # Test out the callbacks...
    # print(robotAction.move_to_component())
    robotAction.move_to_component()
    # robotAction.position_pickup()

    # robotAction.position_pickup()
    # print(robotAction.state)
    # machine.set_state('need construction')
