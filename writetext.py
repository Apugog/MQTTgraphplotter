import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
xs = []
ys = []


def on_message(mqttc, obj, msg):

    idata = msg.payload
    if len(idata) > 1:
        x, y = idata.split(',')
        file1 = open("mqttpayload.txt", "a")
        file1.write(x)
        file1.write(",")
        file1.write(y)
        file1.write("\n")
        file1.close()


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.connect("Your Server domain name or ip-address", 1883, 60)
mqttc.subscribe("Select Your Channel")
mqttc.loop_forever()
