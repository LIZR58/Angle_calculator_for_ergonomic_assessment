import numpy as np
import math
import angle_calculator.Util as Util
import angle_calculator.joint_number as jointNum

class TrunkAngle:
    def __init__(self, joints):
        self.joints = joints

# left_shoulder, right_shoulder,left_hip, right_hip
# return [3, 6, 9, 12]

    def mid_trunk(self):
        body_num = jointNum.body_number()
        neck_num = body_num.neck()
        mid_head = [(a + b) / 2 for a, b in zip(self.joints[neck_num[1]], self.joints[neck_num[2]])]
        mid_neck = [(a + b) / 2 for a, b in zip(self.joints[neck_num[3]], self.joints[neck_num[4]])]
        mid_waist = [(a + b) / 2 for a, b in zip(self.joints[neck_num[5]], self.joints[neck_num[6]])]
        mid_head = np.array(mid_head)
        mid_neck = np.array(mid_neck)
        mid_waist = np.array(mid_waist)
        return mid_head, mid_neck, mid_waist

    def normal_trunk(self):
        body_num = jointNum.body_number()
        trunk_num = body_num.trunk()
        left_hip = self.joints[trunk_num[2]]
        right_hip = self.joints[trunk_num[3]]
        normal_vector_sagittal = left_hip - right_hip
        v_upright = [0, 0, 1]
        normal_vector_coronal = np.cross(normal_vector_sagittal, v_upright)
        return normal_vector_sagittal, normal_vector_coronal

    def trunk_flexion_calculator(self):
        mid_head, mid_neck, mid_waist = self.mid_trunk()
        v_WaisttoNeck = mid_neck - mid_waist
        normal_vector_sagittal, normal_vector_coronal = self.normal_trunk()
        v_WaisttoNeck_projection = Util.vector_onto_plane(v_WaisttoNeck, normal_vector_sagittal)
        trunk_flexion = 90 - Util.get_angle_between_vectors(v_WaisttoNeck_projection, normal_vector_coronal)
        return trunk_flexion

    def trunk_bending_calculator(self):
        mid_head, mid_neck, mid_waist = self.mid_trunk()
        v_WaisttoNeck = mid_neck - mid_waist
        normal_vector_sagittal, normal_vector_coronal = self.normal_trunk()
        v_WaisttoNeck_projection = Util.vector_onto_plane(v_WaisttoNeck, normal_vector_coronal)
        trunk_bending = 90 - Util.get_angle_between_vectors (v_WaisttoNeck_projection, normal_vector_sagittal)
        return trunk_bending

    def trunk_twisting_calculator(self):
        mid_head, mid_neck, mid_waist = self.mid_trunk()
        body_num = jointNum.body_number()
        trunk_num = body_num.trunk()
        left_shoulder = self.joints[trunk_num[0]]
        right_shoulder = self.joints[trunk_num[1]]
        left_hip = self.joints[trunk_num[2]]
        right_hip = self.joints[trunk_num[3]]
        right_to_left_shoulder_now = left_shoulder - right_shoulder
        right_to_left_shoulder_previous = left_hip - right_hip
        normal_vector_FlexionandBending = mid_neck - mid_waist
        right_to_left_shoulder_previous_projection = Util.vector_onto_plane(right_to_left_shoulder_previous, normal_vector_FlexionandBending)
        right_to_left_ear_now_vertical = np.cross(right_to_left_shoulder_now, normal_vector_FlexionandBending)

        trunk_twisting = 90 - Util.get_angle_between_vectors(right_to_left_ear_now_vertical, right_to_left_shoulder_previous_projection)
        return trunk_twisting

    def trunk_angle(self):
        trunk_flexion_angle = self.trunk_flexion_calculator()
        trunk_bending_angle = self.trunk_bending_calculator()
        trunk_twisting_angle = self.trunk_twisting_calculator()
        return trunk_flexion_angle, trunk_bending_angle, trunk_twisting_angle











