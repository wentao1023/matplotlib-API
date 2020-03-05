from random import choice
import pygal
class RandomWalk():
#TODO'''一个生成随机漫步数据的类'''
     def __init__(self,num_points=5000):
         '''初始化随机漫步的属性'''
         self.num_points = num_points
         # 所有随机漫步都始于（0,0）
         self.values = []
         self.x_values = [0]
         self.y_values = [0]

     def fill_walk(self):
         while len(self.x_values)<self.num_points:
             # x_direction = choice([1,-1])
             # x_distance = choice([0,1,2,3,4])
             # x_step = x_direction * x_distance
             #
             # y_direction = choice([1,-1])
             # y_diatance = choice([0,1,2,3,4])
             # y_step = y_direction*y_diatance
             x_step = self.get_step()
             y_step = self.get_step()
             if x_step == 0 and y_step == 0:
                 continue
             next_x = self.x_values[-1] + x_step
             next_y = self.y_values[-1] + y_step

             self.x_values.append(next_x)
             self.y_values.append(next_y)
             self.values.append((next_x,next_y))

     def get_step(self):
         direction = choice([-1,1])
         distance = choice([0,1,2,3,4])
         step = direction * distance
         return step

rw = RandomWalk()
rw.fill_walk()
sandiantu = pygal.XY(stroke = False)
sandiantu.title = "Result of Randomwalk"
sandiantu.add('A',rw.values)
sandiantu.render_to_file('randomwalk-2.svg')
print(rw.values)
