import numpy as np
import math
import angle_calculator.Util as Util
import angle_calculator.joint_number as jointNum

class LowerArmAngle:
    def __init__(self, joints):
        self.joints = joints
        # left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist
        # return [3, 6, 4, 7, 16, 18]

    def lower_arm_flexion_calculator(self):
        body_num = jointNum.body_number()
        lower_arm_num = body_num.lower_arm()
        left_shoulder = self.joints[lower_arm_num[0]]
        right_shoulder = self.joints[lower_arm_num[1]]
        left_elbow = self.joints[lower_arm_num[2]]
        right_elbow = self.joints[lower_arm_num[3]]
        left_wrist = self.joints[lower_arm_num[4]]
        right_wrist = self.joints[lower_arm_num[5]]

        left_v_ElbowtoShoulder = left_shoulder - left_elbow
        right_v_ElbowtoShoulder = right_shoulder - right_elbow
        left_v_ElbowtoWrist = left_wrist - left_elbow
        right_v_ElbowtoWrist = right_wrist - right_elbow

        left_lower_arm_flexion = 180 - Util.get_angle_between_vectors(left_v_ElbowtoShoulder, left_v_ElbowtoWrist)
        right_lower_arm_flexion = 180 - Util.get_angle_between_vectors(right_v_ElbowtoShoulder, right_v_ElbowtoWrist)

        return left_lower_arm_flexion, right_lower_arm_flexion
