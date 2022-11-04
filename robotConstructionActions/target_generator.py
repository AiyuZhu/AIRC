import rospy
from gazebo_msgs.srv import GetModelState

class target_pose_generator(object):
    def __init__(self):
        pass

    def move_to_component(self):
        # connect simulator to get component info
        sim_get = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        comp_info = sim_get(self.comp_id, '')

        # get comp current position
        position_x = comp_info.pose.position.x
        position_y = comp_info.pose.position.y
        position_z = comp_info.pose.position.z

        # set the destination location to robot
        dest_p = [position_x - 0.55, position_y, position_z]
        dest_q = [0.0, 0.0, 1, 1]

        return (dest_p, dest_q)