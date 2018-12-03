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

### topology.py 的結構

&emsp;&emsp;一開始先 import 所需要的 module，再來是建立 class。在 class 裡面，我們將所需要的 host 跟 switch 一一建立出來，建立好之後，再依照 ![topo2.png](/src/topo/topo2.png) 的要求來建立各個host 與 host, switch 與 switch, host 與 switch 間的連結。之後在定義一個function來運作整個整體，建立mininet，以及用dumpNodeConnections跟CLI。

### 執行的方式
1. 先到topology.py所在的資料夾
2. 再用sudo chmod +x 轉到可執行的模式
3. 輸入sudo ./topology.py 來執行程式
4. 跑完後，再輸入h6 iperf -s -u -i 1 > ./out/result &
5. 以及h3 iperf -c 10.0.0.6 -u –i 1
6. 獲得輸出的結果

h6 iperf -s -u -i 1 > ./out/result & 是指說 h6當作server 用 udp 傳送，每一秒印出一次訊息，將檔案寫在./out/result裡面。

h3 iperf -c 10.0.0.6 -u –i 1 則是表示說 h3 當作 client 並且連線到 10.0.0.6 ，用 udp 傳送，每一秒印出一次訊息。

### 輸出的結果

![/image/4.png](/image/4.png)

---
## Description

### Mininet API in Python

> TODO:
> * Describe the meaning of Mininet API in Python you used in detail

### iPerf Commands

> TODO:
> * Describe the meaning of iPerf command you used in detail

### Tasks

> TODO:
> * Describe how you finish this work step-by-step in detail

1. **Environment Setup**


2. **Example of Mininet**


3. **Topology Generator**


4. **Measurement**

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