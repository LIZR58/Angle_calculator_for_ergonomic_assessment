import numpy as np
import math
import angle_calculator.Util as Util
import angle_calculator.joint_number as jointNum

class LegAngle:
    def __init__(self, joints):
        self.joints = joints

# [9, 12, 10, 13, 17, 19]

    def leg_support_calculator(self):
        body_num = jointNum.body_number()
        leg_num = body_num.leg()
        left_ankle = self.joints[leg_num[4]]
        right_ankle = self.joints[leg_num[5]]
        left_knee = self.joints[leg_num[2]]
        right_knee = self.joints[leg_num[3]]
        lenth_left_lower_leg = Util.get_distance_between(left_knee, left_ankle)
        lenth_right_lower_leg = Util.get_distance_between(right_knee, right_ankle)
        leg_support = (left_ankle[2] - right_ankle[2]) / (lenth_left_lower_leg / 2 + lenth_right_lower_leg / 2)
        return leg_support

    def leg_angle_calculator(self):
        body_num = jointNum.body_number()
        leg_num = body_num.leg()
        left_hip = self.joints[leg_num[0]]
        right_hip = self.joints[leg_num[1]]
        left_knee = self.joints[leg_num[2]]
        right_knee = self.joints[leg_num[3]]
        left_ankle = self.joints[leg_num[4]]
        right_ankle = self.joints[leg_num[5]]
        v_left_KneetoHip = left_hip - left_knee
        v_left_KneetoFoot = left_ankle - left_knee
        v_right_KneetoHip = right_hip - right_knee
        v_right_KneetoFoot = right_ankle - right_knee
        left_leg_angle = 180 - Util.get_angle_between_vectors(v_left_KneetoHip, v_left_KneetoFoot)
        right_leg_angle = 180 - Util.get_angle_between_vectors(v_right_KneetoHip, v_right_KneetoFoot)
        return left_leg_angle, right_leg_angle

    def leg_angle(self):
        leg_support = self.leg_support_calculator()
        left_leg_angle, right_leg_angle = self.leg_angle_calculator()
        return leg_support, left_leg_angle, right_leg_angle



