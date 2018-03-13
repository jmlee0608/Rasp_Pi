# import the sense-hat library
from sense_hat import SenseHat
# declare a sensehat instance
sense = SenseHat()
# read the temperature - multiply by thousand for number shortening
temp = sense.get_temperature()*1000
# read the humidity- multiply by thousand for number shortening
hum = sense.get_humidity()*1000
# change the resulting float numbers which can get quite long into ints
temp2 = int(temp)
hum2  = int(hum)
# set the led for lower light condition, less energy 
sense.low_light= True
# rotate to our taste - you might want to change this to 90 180 270 - however you want to read your display
sense.set_rotation(0)
# define two colours
red=(255,0,0)
blue=(0,0,255)
# some number formating
temp3 = float(temp2)/1000
hum3 = float(hum2)/1000
# now we show the numbers with speed 0.2, smaller number means slower and in different colours
sense.show_message(str(repr(temp3)),text_colour=red,scroll_speed=0.2)
sense.show_message(str(repr(hum3)),text_colour=blue,scroll_speed=0.2)
# reset the led lighting condition to get an orderly exit condition
sense.low_light= True
