from transitions import Machine
import uuid


class RobotConstructionActionNode(object):
    states = ['need construction', 'need positioning for picking up', 'need pick-up', 'need transfer to target',
              'need positioning for assembling', 'need assembly']

    def __init__(self):
        self.id = uuid.uuid4()
        self.machine = Machine(model=self, states=RobotConstructionActionNode.states, initial='need construction')
        self.machine.add_transition(trigger='move_to_component',
                                    source='need construction',
                                    dest='need positioning for picking up')
        self.machine.add_transition(trigger='position pick-up point',
                                    source='need positioning for picking up',
                                    dest='need pick-up')
        self.machine.add_transition(trigger='pick up',
                                    source='need pick-up',
                                    dest='need transfer to target')
        self.machine.add_transition(trigger='move to target',
                                    source='need transfer to target',
                                    dest='need positioning for assembling')
        self.machine.add_transition(trigger='positioning assembly point',
                                    source='need positioning for assembling',
                                    dest='need assembly')
        self.machine.add_transition(trigger='assemble',
                                    source='need assembly',
                                    dest='constructed')


if __name__ == '__main__':
    test_comp = RobotConstructionActionNode()
    test_comp.move_to_component()
    print(test_comp.state)
