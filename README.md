# Network Topology with Mininet

This repository is lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program which can generate a network topology using Mininet and use iPerf to measure the bandwidth of the topology.

---
## Objectives

1. Learn how to create a network topology with Mininet
2. Learn how to measure the bandwidth in your network topology with iPerf

---
## Execution

### 工作站的密碼
* Container Password: ```0616091```

### 執行的方式

1. 先到topology.py所在的資料夾

	```
	$ cd /root/Network_Topology/src/
	```
2. 再用sudo chmod +x 轉到可執行的模式

	```
	$ sudo chmod +x topology.py
	```
3. 輸入sudo ./topology.py 來執行程式

	```
	$ sudo ./topology.py
	```
4. 執行的過程時，會將switch跟host的資訊dump出來，並且進到mininet-CLI mode。
5. 接著再把h6當作server跟 h3當作 client，並且把結果輸出到./out/result這個資料夾裡面
	```
	mininet> h6 iperf -s -u -i 1 > ./out/result &
	```
	```
	mininet> h3 iperf -c 10.0.0.6 -u –i 1
	```
6. 獲得輸出的結果
	
	get the rate of packet loss which is an approximate value (13% ~ 18%)

### 輸出的結果

![/image/1.png](/image/1.png)

![/image/2.png](/image/2.png)

![/image/3.png](/image/3.png)

![/image/4.png](/image/4.png)

---
## Description

### Mininet API in Python

* ```from mininet.cli import CLI```:

	讓我們能用command-line的介面來下指令
* ```from mininet.log import setLogLevel```:

	設置日誌級別
* ```from mininet.util import dumpNodeConnections```:

	輸出有關nodes的資訊
* ```from mininet.net import Mininet```: 

	Network emulation with hosts spawned in network namespaces.
* ```from mininet.topo import Topo```:

	Data center network representation for structured multi-trees.
* ```from mininet.node import OVSController```:
	
	打開 vSwitch controller.
* ```from mininet.link import TCLink```:

	Link with symmetric TC interfaces configured via opts.

### iPerf Commands

* ```h6 iperf -s -u -i 1 > ./out/result & ```

	是指說 h6 當作 server 用 udp 傳送，每一秒印出訊息，將結果寫在./out/result裡面。
	
	* ```h6``` 
		
		用 h6 當作host
	* ```-s ```
	
		表示當作server
	* ```-u``` 

		表示用udp傳送，預設為1Mbps。
	* ```-i 1```

		表示每一秒印出訊息
	* ```> ./out/result``` 

		將結果輸出到那個位置
	* ```&``` 
	
		讓command line在背景執行。所以我們能讓server在背景執行，同時間又執行client的指令

	

* ```h3 iperf -c 10.0.0.6 -u –i 1 ```

	是表示說 h3 當作 client 並且連線到 10.0.0.6 ，用 udp 傳送，每一秒印出一次訊息。
	
	* ```h3```
		
		用 h3 當作host
	* ```-c <host>``` 

		表示當成client連線到host的位置，host是server的ip位置。我們將h6當作server，而h6的ip位置是10.0.0.6，所以寫成-c 10.0.0.6。
	* ```-u``` 

		表示用udp傳送，預設為1Mbps。
	* ```-i 1```

		表示每一秒印出訊息
		
### Tasks

1. **Environment Setup**

	用ssh連到學校的工作站裡面，然後clone github上面的檔案下來到 Network_Topology資料夾裡面，用sudo mn 是跑看看mininet有無問題。

2. **Example of Mininet**

	cd到example.py所在的資料夾，再用sudo chmod +x 來將檔案轉成可執行檔，接著便輸入 sudo ./example.py 來執行。若發生像是"RTNETLINK answers: File exists"的問題，可以用mn -c 來將mininet清乾淨。


3. **Topology Generator**

	我的學號是0616091，所以後五碼是16091除3會餘2，因此是topo2.png。
	
	***topology.py 的結構***

	* 在開頭加入```#!/usr/bin/python```，讓系統知道要用python來當作interpreter，所以才能用```chmod +x```來轉換成可執行檔。
	* 接著 import 所需要的 module
	* 再來是建立 class。在 class 裡面，定義一個build的function，在build裡面，用```self.addHost```來建立host 以及用 ```self.addSwitch```來建立 switch，建立好之後，再依照 ![topo2.png](/src/topo/topo2.png) 的要求來建立各個switch 與 switch, host 與 switch 間的連結，使用```self.addLink```來建立連結。
	Example:```self.addSwitch('s5')``` ```self.addHost('h1')```
	
	* 連結的設定便依照圖片中所要求的bandwidth, delay, and loss rate來建立。

		Example:```self.addLink(h1, switch2, bw = 14, delay = '5ms', loss = 13)```
	* 之後在定義一個function來運作整個整體，建立mininet ```net = Mininet(topo = topo, controller = OVSController, link = TCLink)```。用```net.start()```啟動程式，用```dumpNodeConnections(net.hosts)```以及```dumpNodeConnections(net.switches)```來輸出host跟switch的資訊，```net.pingAll()```將host的ping輸出，最後再用```CLI(net)```進到mininet的command line interface。

4. **Measurement**
	
	* 先執行topology.py，若無問題，會順利進入到mininet的CLI。
	* 再輸入```h6 iperf -s -u -i 1 > ./out/result & ```以及```h3 iperf -c 10.0.0.6 -u –i 1```來輸出所想要的資訊。
	* 結果會被輸出到/src/out/result。
	* 最後得到的結果是![/image/4.png](/image/4.png)符合作業所要求的approximate value (13% ~ 18%)。

---
## References

* **My References**

	* [透過 SSH 傳送檔案](https://www.phpini.com/linux/ssh-transfer-file-scp)	
	* [Command Line Basics 基本操作](http://www.vialley.com/240/command-line-basics) 
	* [Linux 的 scp 指令用法教學與範例：遠端加密複製檔案與目錄](https://blog.gtwang.org/linux/linux-scp-command-tutorial-examples/)

* **Mininet**
    * [Mininet Walkthrough](http://mininet.org/walkthrough/)
    * [Introduction to Mininet](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Mininet Python API Reference Manual](http://mininet.org/api/annotated.html)
    * [A Beginner's Guide to Mininet](https://opensourceforu.com/2017/04/beginners-guide-mininet/)
    * [GitHub/OSE-Lab - 熟悉如何使用 Mininet](https://github.com/OSE-Lab/Learning-SDN/blob/master/Mininet/README.md)
    * [菸酒生的記事本 – Mininet 筆記](https://blog.laszlo.tw/?p=81)
    * [Hwchiu Learning Note – 手把手打造仿 mininet 網路](https://hwchiu.com/setup-mininet-like-environment.html)
    * [阿寬的實驗室 – Mininet 指令介紹](https://ting-kuan.blog/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
    * [Mininet 學習指南](https://www.sdnlab.com/11495.html)
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
    * [iPerf3 User Documentation](https://iperf.fr/iperf-doc.php#3doc)
    * [Cheat Sheet of Markdown Syntax](https://www.markdownguide.org/cheat-sheet)
    * [Vim Tutorial – Tutorialspoint](https://www.tutorialspoint.com/vim/index.htm)
    * [鳥哥的 Linux 私房菜 – 第九章、vim 程式編輯器](http://linux.vbird.org/linux_basic/0310vi.php)

---
## Contributors

* [Yu Ying Chen](https://github.com/iamch15542)
* [David Lu](https://github.com/yungshenglu)

---
## License

GNU GENERAL PUBLIC LICENSE Version 3