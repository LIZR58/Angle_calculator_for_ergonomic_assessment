import math
import numpy as np

def get_angle_between_vectors(v1, v2):
    lenth_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)
    lenth_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2 + v2[2] ** 2)
    result = math.acos(round(np.dot(v1, v2) / (lenth_v1 * lenth_v2), 3)) * 180 / math.pi
    return result

def get_distance_between(p1, p2):
    result = [x + y for x, y in zip(p2, np.dot(p1, -1))]
    return math.sqrt(result[0] ** 2 + result[1] ** 2 + result[2] ** 2)

def compute_normal_vector(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    normal_vector = np.cross(v1, v2)
    return normal_vector

def vector_onto_plane(v, normal_vector):
    vector_onto = v - np.dot(v, normal_vector) * normal_vector
    return vector_onto

def normalization(vector):
    l = math.sqrt(vector[0] ** 2 + vector[1] ** 2 + vector[2] ** 2)
    if l == 0:
        l += 0.01
    normal_vector = [vector[0] / l, vector[1] / l, vector[2] / l]
    return normal_vector

