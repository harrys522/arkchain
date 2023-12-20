import pickle
import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
import src.node as node
import datetime

# Slice 1
node1 = node.node(configpath='conf1.ini')
node2 = node.node(configpath='conf2.ini')
node3 = node.node(configpath='conf3.ini')
node4 = node.node(configpath='conf4.ini')
slice1 = [node1,node2,node3,node4]

for n in slice1:
    n.local_tree().insert_thread_safe(datetime.dateime.now(),n.block)
    



