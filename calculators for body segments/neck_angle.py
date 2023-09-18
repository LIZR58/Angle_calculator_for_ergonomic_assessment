import numpy as np
import math
import angle_calculator.Util as Util
import angle_calculator.joint_number as jointNum

class NeckAngle:
    def __init__(self, joints):
        self.joints = joints

# head, neck, spine, left_shoulder, right_shoulder, left_hip, right_hip
# return [0, 1, 2, 3, 6, 9, 12]

    def normal_neck(self):
        body_num = jointNum.body_number()
        neck_num = body_num.neck()
        head = self.joints[neck_num[0]]
        spine = self.joints[neck_num[2]]

        left_shoulder = self.joints[neck_num[3]]
        right_shoulder = self.joints[neck_num[4]]
        neck = (left_shoulder + right_shoulder)/2
        normal_vector_sagittal = left_shoulder - right_shoulder
        v_SpinetoNeck = neck - spine
        normal_vector_sagittal_new = Util.vector_onto_plane(normal_vector_sagittal, v_SpinetoNeck)
        normal_vector_coronal = Util.compute_normal_vector(spine, left_shoulder, right_shoulder)
        return normal_vector_sagittal_new, normal_vector_coronal

    def neck_flexion_calculator(self):
        body_num = jointNum.body_number()
        neck_num = body_num.neck()
        head = self.joints[neck_num[0]]

        left_shoulder = self.joints[neck_num[3]]
        right_shoulder = self.joints[neck_num[4]]
        neck = (left_shoulder + right_shoulder) / 2
        v_NecktoHead = head - neck
        normal_vector_sagittal, normal_vector_coronal = self.normal_neck()
        v_NecktoHead_projection = Util.vector_onto_plane(v_NecktoHead, normal_vector_sagittal)
        neck_flexion = 90 - Util.get_angle_between_vectors(v_NecktoHead_projection, normal_vector_coronal)
        return neck_flexion

    def neck_bending_calculator(self):
        body_num = jointNum.body_number()
        neck_num = body_num.neck()
        head = self.joints[neck_num[0]]
        left_shoulder = self.joints[neck_num[3]]
        right_shoulder = self.joints[neck_num[4]]
        neck = (left_shoulder + right_shoulder) / 2
        v_NecktoHead = head - neck
        normal_vector_sagittal, normal_vector_coronal = self.normal_neck()
        v_NecktoHead_projection = Util.vector_onto_plane(v_NecktoHead, normal_vector_coronal)
        neck_bending = 90 - Util.get_angle_between_vectors(v_NecktoHead_projection, normal_vector_sagittal)
        return neck_bending

    def neck_angle(self):
        neck_flexion_angle = self.neck_flexion_calculator()
        neck_bending_angle = self.neck_bending_calculator()
        return neck_flexion_angle, neck_bending_angle










