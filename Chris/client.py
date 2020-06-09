import bluetooth

# This demo makes your PC talk to an EV3 over Bluetooth.
#
# This is identical to the EV3 client example in ../bluetooth_client
#
# The only difference is that it runs in Python3 on your computer, thanks to
# the Python3 implementation of the messaging module that is included here.
# As far as the EV3 is concerned, it thinks it just talks to an EV3 client.
#
# So, the EV3 server example needs no further modifications. The connection
# procedure is also the same as documented in the messaging module docs:
# https://docs.pybricks.com/en/latest/messaging.html
#
# So, turn Bluetooth on on your PC and the EV3. You may need to make Bluetooth
# visible on the EV3. You can skip pairing if you already know the EV3 address.

# This is the address of the server EV3 we are connecting to.
target_address = '40:BD:32:30:E5:6D'

# nearby_devices = bluetooth.discover_devices()

# for bdaddr in nearby_devices:
#     if target_address == bluetooth.lookup_address( bdaddr ):
#         target_address = bdaddr
#         break

# if target_address is not None:
#     print("found target bluetooth device with address " + target_address)
# else:
#     print("could not find target bluetooth device nearby")

services = bluetooth.find_service(address=target_address)

if len(services) > 0:
    print("Found {} services on {}.".format(len(services), target_address))
else:
    print("No services found.")

for svc in services:
    print("\nService Name:", svc["name"])
    print("    Host:       ", svc["host"])
    print("    Description:", svc["description"])
    print("    Provided By:", svc["provider"])
    print("    Protocol:   ", svc["protocol"])
    print("    channel/PSM:", svc["port"])
    print("    svc classes:", svc["service-classes"])
    print("    profiles:   ", svc["profiles"])
    print("    service id: ", svc["service-id"])
# print("Performing inquiry...")


# client = BluetoothMailboxClient()
# mbox = TextMailbox('greeting', client)

client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# client_socket.settimeout(10)
print('establishing connection...')
# for i in range(1000):
# 	try:
# 		client_socket.connect((target_address, i))
# 	except Exception as e:
# 		pass

client_socket.connect((target_address,2))
print("here")
# client_socket.listen(1)
# c,add=client_socket.accept()
# print(add)
# print(data)

client_socket.send("Hello World")
client_socket.read()
print('connected!')

# print(client_socket.read())

# In this program, the client sends the first message and then waits for the
# server to reply.
client_socket.close()
c.close()