import numpy as np
import math
import angle_calculator.Util as Util
import angle_calculator.joint_number as jointNum

class UpperArmAngle:
    def __init__(self, joints):
        self.joints = joints
        # head, neck, spine, left_shoulder, right_shoulder, left_elbow, right_elbow, left_hip, right_hip
        # [0, 1, 2, 3, 6, 4, 7, 9, 12]

    def normal_vector(self):

        body_num = jointNum.body_number()
        upper_arm_num = body_num.upper_arm()

        spine = self.joints[upper_arm_num[2]]

        body_num = jointNum.body_number()
        upper_arm_num = body_num.upper_arm()
        left_shoulder = self.joints[upper_arm_num[3]]
        right_shoulder = self.joints[upper_arm_num[4]]
        neck = (left_shoulder + right_shoulder) / 2
        normal_vector_sagittal = left_shoulder - right_shoulder
        v_SpinetoNeck = neck - spine
        normal_vector_sagittal_new = Util.vector_onto_plane(normal_vector_sagittal, v_SpinetoNeck)
        v_upright = [0, 0, 1]
        normal_vector_coronal_new = np.cross(normal_vector_sagittal, v_upright)
        return normal_vector_sagittal_new, normal_vector_coronal_new

    def upper_arm_flexion_calculator(self):
        body_num = jointNum.body_number()
        upper_arm_num = body_num.upper_arm()
        left_shoulder = self.joints[upper_arm_num[3]]
        right_shoulder = self.joints[upper_arm_num[4]]
        left_elbow = self.joints[upper_arm_num[5]]
        right_elbow = self.joints[upper_arm_num[6]]
        normal_vector_sagittal, normal_vector_coronal = self.normal_vector()

        left_v_ShouldertoElbow = left_elbow - left_shoulder
        right_v_ShouldertoElbow = right_elbow - right_shoulder
        left_v_ShouldertoElbow_projection = Util.vector_onto_plane(left_v_ShouldertoElbow, normal_vector_sagittal)
        right_v_ShouldertoElbow_projection = Util.vector_onto_plane(right_v_ShouldertoElbow, normal_vector_sagittal)

        v_updown = [0, 0, -1]
        left_angle = Util.get_angle_between_vectors(left_v_ShouldertoElbow_projection, v_updown)
        left_dot = np.dot(left_v_ShouldertoElbow_projection, normal_vector_coronal)
        if left_dot > 0:
            left_angle = left_angle
        elif left_dot == 0:
            left_angle = 0
        else:
            left_angle = -left_angle

        right_angle = Util.get_angle_between_vectors(right_v_ShouldertoElbow_projection, v_updown)
        right_dot = np.dot(right_v_ShouldertoElbow_projection, normal_vector_coronal)
        if right_dot > 0:
            right_angle = right_angle
        elif right_dot == 0:
            right_angle = 0
        else:
            right_angle = -right_angle

        left_flexion = left_angle
        right_flexion = right_angle

        return left_flexion, right_flexion


    def shoulder_gap_angle_calculator(self):
        body_num = jointNum.body_number()
        upper_arm_num = body_num.upper_arm()
        left_shoulder = self.joints[upper_arm_num[3]]
        right_shoulder = self.joints[upper_arm_num[4]]
        normal_vector_sagittal, normal_vector_coronal = self.normal_vector()
        spine = self.joints[upper_arm_num[2]]

        neck = (left_shoulder + right_shoulder) / 2
        v_shoulders_right_left = left_shoulder - right_shoulder
        v_shoulders_right_left_projection = Util.vector_onto_plane(v_shoulders_right_left, normal_vector_coronal)
        v_SpinetoNeck = neck - spine
        shoulder_gap_angle = 90 - Util.get_angle_between_vectors(v_shoulders_right_left_projection, v_SpinetoNeck)

        return shoulder_gap_angle

    def upper_arm_abducted_calculator(self):
        body_num = jointNum.body_number()
        upper_arm_num = body_num.upper_arm()
        head = self.joints[upper_arm_num[0]]
        spine = self.joints[upper_arm_num[2]]
        left_shoulder = self.joints[upper_arm_num[3]]
        right_shoulder = self.joints[upper_arm_num[4]]
        neck = (left_shoulder + right_shoulder) / 2
        left_elbow = self.joints[upper_arm_num[5]]
        right_elbow = self.joints[upper_arm_num[6]]
        left_v_ShouldertoElbow = left_elbow - left_shoulder
        right_v_ShouldertoElbow = right_elbow - right_shoulder
        normal_vector_sagittal = left_shoulder - right_shoulder
        v_SpinetoNeck = neck - spine
        normal_vector_sagittal = Util.vector_onto_plane(normal_vector_sagittal, v_SpinetoNeck)
        normal_vector_coronal = Util.compute_normal_vector(spine, left_shoulder, right_shoulder)
        left_v_ShouldertoElbow_projection = Util.vector_onto_plane(left_v_ShouldertoElbow, normal_vector_coronal)
        right_v_ShouldertoElbow_projection = Util.vector_onto_plane(right_v_ShouldertoElbow, normal_vector_coronal)
        v_updown = [0, 0, -1]
        left_angle = Util.get_angle_between_vectors(left_v_ShouldertoElbow_projection, v_updown)
        left_dot = np.dot(left_v_ShouldertoElbow_projection, normal_vector_sagittal)
        if left_dot > 0:
            left_angle = left_angle
        elif left_dot == 0:
            left_angle = 0
        else:
            left_angle = -left_angle

        right_angle = Util.get_angle_between_vectors(right_v_ShouldertoElbow_projection, v_updown)
        right_dot = np.dot(right_v_ShouldertoElbow_projection, normal_vector_sagittal)
        if right_dot > 0:
            right_angle = -right_angle
        elif right_dot == 0:
            right_angle = 0
        else:
            right_angle = right_angle

        left_abduction = left_angle
        right_abduction = right_angle
        return left_abduction, right_abduction

    def upper_arm_angle(self):
        upper_arm_left_flexion_angle, upper_arm_right_flexion_angle = self.upper_arm_flexion_calculator()
        upper_arm_shoulder_gap_angle = self.shoulder_gap_angle_calculator()
        upper_arm_left_abduction_angle, upper_arm_right_abduction_angle = self.upper_arm_abducted_calculator()
        return upper_arm_left_flexion_angle, upper_arm_right_flexion_angle, upper_arm_shoulder_gap_angle, upper_arm_left_abduction_angle, upper_arm_right_abduction_angle


