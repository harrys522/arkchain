import pickle
import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parentdir)
import src.node as node



node1 = node.node(configpath='conf1.ini')
node2 = node.node(configpath='conf2.ini')
node3 = node.node(configpath='conf3.ini')
