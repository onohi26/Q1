import numpy as np
import json

json_file = open('points.json')
json_dict = json.load(json_file)

q1 = json_dict['Q1_1']
q2 = json_dict['Q1_2']
q3 = json_dict['Q1_3']

q1_ans = []
q2_ans = []
q3_ans = []

#Q1_1
theta = np.radians(30)
affine = np.array([[np.cos(theta),-np.sin(theta)],
                   [np.sin(theta),np.cos(theta)]])
for src in q1:
    src=np.array(src)
    dst = np.matmul(affine,src)
    q1_ans.append(list(dst))

#Q1_2

alpha = 1.28
affine = np.array([[alpha,0],
                    [0,alpha]])
for src in q2:
    src=np.array(src)-128
    dst = np.matmul(affine,src)
    dst=dst+128
    q2_ans.append(list(dst))



#Q1_3
theta = np.radians(12)
alpha = 0.8
affine_rotate = np.array([[np.cos(theta),-np.sin(theta)],
                   [np.sin(theta),np.cos(theta)]])
affine_scale = np.array([[alpha,0],
                   [0,alpha]])
for src in q3:
    src = np.array(src)-128
    dst_rotate = np.matmul(affine_rotate,src)
    dst_scale = np.matmul(affine_scale,dst_rotate)
    dst_scale = dst_scale + 128
    q3_ans.append(list([dst_scale[0]+12,dst_scale[1]+8]))

dic = {
    "Q1_1":q1_ans,
    "Q1_2":q2_ans,
    "Q1_3":q3_ans
}

save_file = open('submission.json','w')
json.dump(dic,save_file)

