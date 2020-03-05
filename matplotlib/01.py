# import matplotlib.pyplot as plt
# squares = [1,4,9,16,25]
# plt.plot(squares)
# plt.show()

import matplotlib.pyplot as plt
# input_value = [1,2,3,4,6]
# squares = [1,4,9,16,25]
# plt.plot(input_value, squares, linewidth=5)
# plt.title("Square Number",fontsize=24)
# plt.xlabel("value",fontsize=24)
# plt.ylabel("Square of Value", fontsize=14)
# plt.tick_params(axis='both',labelsize=20)
# plt.show()
# x_values = list(range(1,11))
# y_values = [x**3 for x in x_values]
# plt.scatter(x_values,y_values, c=y_values,cmap=plt.cm.Wistia,
#             edgecolors='none',s = 200)
# plt.title("Square Number",fontsize=24)
# plt.xlabel("value",fontsize=24)
# plt.ylabel("Square of Value", fontsize=14)
# #plt.tick_params(axis='both',which='major',labelsize=14)
# plt.axis([0,11,0,1100])
#
# plt.show()
# from random import choice
# class RandomWalk():
#      '''一个生成随机漫步数据的类'''
#      def __init__(self,num_points=5000):
#          '''初始化随机漫步的属性'''
#          self.num_points = num_points
#          # 所有随机漫步都始于（0,0）
#          self.x_values = [0]
#          self.y_values = [0]
#
#      def fill_walk(self):
#          while len(self.x_values)<self.num_points:
#              x_direction = choice([1,-1])
#              x_distance = choice([0,1,2,3,4])
#              x_step = x_direction * x_distance
#
#              y_direction = choice([1,-1])
#              y_diatance = choice([0,1,2,3,4])
#              y_step = y_direction*y_diatance
#              if x_step == 0 and y_step == 0:
#                  continue
#              next_x = self.x_values[-1] + x_step
#              next_y = self.y_values[-1] + y_step
#
#              self.x_values.append(next_x)
#              self.y_values.append(next_y)

# import matplotlib.pyplot as plt
# from randow_walk import RandomWalk
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#     #point_numbers = list(range(rw.num_points))
#     plt.plot(rw.x_values,rw.y_values,linewidth = 5)
#     # plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
#     #             edgecolors='none',
#     #         cmap=plt.cm.Blues,s=1)
#     #突出起点和终点
#     # plt.scatter(0,0,c='green',edgecolors='none',s=100)
#     # plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',
#     #             edgecolors='none',s=100)
#     # plt.axes().get_xaxis().set_visible(False)
#     # plt.axes().get_yaxis().set_visible(False)
#     # plt.figure(dpi=1080,figsize=(10,6))
#     plt.show()
#     keep_running = input("Make another walk? (y/n): ")
#     if keep_running == 'n':
#         break

