# from die import Die
# import pygal
# die = Die()
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)
#
# frequencies = []
# for  value in range(1,die.num_sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
#
# print(frequencies)
# hist = pygal.Bar()
# hist.title = "Result of rolling one D6 1000 times."
# hist.x_labels = ['1','2','3','4','5','6']
# hist.x_title = "Result"
# hist.y_title = "Frequency of Result"
# hist.add('D6', frequencies)
# hist.render_to_file('die_visulal.svg')


from die import Die
import pygal
die_1 = Die()
die_2 = Die()
results = []
for _ in range(5000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for  value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times."
hist.x_labels = ['1','2','3','4','5','6','7','8','9','10','11',
                 '12','13','14','15','16','17','18','19','20','21','22','23','24','25'
                 ,'26','27','28','29','30','31','32','33','34','35','36']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visulal2.svg')