import uuid
import copy
import smartComponent_2 as sc
import activityManagementSystem as ams


class ComponentOrientedConstructionManagementSystem(object):
    def __init__(self, component_list):
        self.id = uuid.uuid4()
        self.construction_state = 'not_start'
        self.total_component = len(component_list)
        self.fake_db = component_list
        self.no_constructed = copy.deepcopy(component_list)
        self.under_construction = []
        self.constructed = {}

    # ordered, add activities manually
    def o_start_construction(self, activities):
        # check init
        while self.construction_state != 'all_work_finished':
            self.construction_state = 'in_construction'

            # confirm construction component and generate statemachine, execute construction
            for component, current_state in self.fake_db.items():
                act = [activity for activity in activities if activity[0] == component]
                states, acts = act[0][1], act[0][2]
                smart_comp = sc.SmartComponent(component, states, acts)
                build_comp = ams.ActivityManagementSystem(smart_comp)
                del self.no_constructed[component]
                self.under_construction.append(component)
                print('----------------------------------------------')
                print('This component under construction:', component)
                print('Rest component are not be constructed: ', self.no_constructed)
                print('\n')
                build_comp.auto_construction()

                # check current component finished?
                if smart_comp.current_state == 'constructed':
                    self.under_construction.remove(component)
                    self.constructed[component] = smart_comp.current_state
                    print('Those component are constructed: ', self.constructed)
                    print('----------------------------------------------')
                    print('\n')

                # check if total construction finish, need rewrite
                if len(self.constructed) == self.total_component:
                    self.construction_state = 'all_work_finished'
        print('The construction is finished!')


if __name__ == '__main__':
    component_for_construction = {'12345': 'need construction', '23456': 'need construction'}

    comp_activities = [
        ['12345',
         [{'name': 'need construction'},
          {'name': 'need positioning for picking up'},
          {'name': 'need pick up'},
          {'name': 'need transfer to target'},
          {'name': 'need positioning for assembling'},
          {'name': 'need assembly'},
          {'name': 'constructed'}],
         {'move_to_component': [1, 2, 3],
          'position_for_picking': [2, 3, 4],
          'pick': [3, 4, 5],
          'transfer': [4, 5, 6],
          'position_for_installing': [5, 6, 7],
          'install': [7, 8, 9]}],
        ['23456',
         [{'name': 'need construction'},
          {'name': 'need positioning for picking up'},
          {'name': 'need pick up'},
          {'name': 'need transfer to target'},
          {'name': 'need positioning for assembling'},
          {'name': 'need assembly'},
          {'name': 'constructed'}],
         {'move_to_component': [1.232, 2.232, 3.432],
          'position_for_picking': [2.342, 3.342, 4.342],
          'pick': [3.4324, 4.342, 5.34234],
          'transfer': [4.432, 5.342, 6.4324],
          'position_for_installing': [5.432, 6.432, 7.3423],
          'install': [7.654, 8.4323, 9.3423]}
         ]
    ]

    construction_1 = ComponentOrientedConstructionManagementSystem(component_for_construction)
    construction_1.o_start_construction(comp_activities)
