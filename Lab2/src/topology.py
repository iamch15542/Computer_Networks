#!/usr/bin/python                                                                            
                        
# import modules from mininet                                                   
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI

# Create Switch and Host
class Topo_two(Topo):
    def build(self):
        # create 5 switch to a topology
        switch1 = self.addSwitch('s1')
        switch2 = self.addSwitch('s2')
        switch3 = self.addSwitch('s3')
        switch4 = self.addSwitch('s4')
        switch5 = self.addSwitch('s5')
        # create 10 host
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')
        h5 = self.addHost('h5')
        h6 = self.addHost('h6')
        h7 = self.addHost('h7')
        h8 = self.addHost('h8')
        h9 = self.addHost('h9')
        h10 = self.addHost('h10')
        # Add a bidirectional link to a topology
        # create link between switch and switch
        self.addLink(switch2, switch1, bw = 30, delay = '87us', loss = 3)
        self.addLink(switch3, switch1, bw = 35, delay = '48us', loss = 2)
        self.addLink(switch4, switch1, bw = 38, delay = '76us', loss = 4)
        self.addLink(switch5, switch1, bw = 40, delay = '52us', loss = 2)
        # create link between switch and host 
        self.addLink(h1, switch2, bw = 14, delay = '5ms', loss = 13)
        self.addLink(h2, switch2, bw = 12, delay = '4ms', loss = 15)
        self.addLink(h3, switch3, bw = 15, delay = '3ms', loss = 8)
        self.addLink(h4, switch3, bw = 11, delay = '2ms', loss = 9)
        self.addLink(h5, switch1, bw = 22, delay = '3ms', loss = 9)
        self.addLink(h6, switch1, bw = 25, delay = '1ms', loss = 7)
        self.addLink(h7, switch1, bw = 18, delay = '4ms', loss = 6)
        self.addLink(h8, switch1, bw = 20, delay = '2ms', loss = 8)
        self.addLink(h9, switch4, bw = 30, delay = '7ms', loss = 12)
        self.addLink(h10, switch5, bw = 25, delay = '5ms', loss = 10)


def lab_task():
    # Create a topology
    topo = Topo_two()
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(topo = topo, controller = OVSController, link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")

    # Dump every connections
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)

    net.pingAll()
    # using CLI mode
    CLI(net)

# main function
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # run the lab task
    lab_task()
