# Route Configuration

This repository is a lab for NCTU course "Introduction to Computer Networks 2018".

---
## Abstract

In this lab, we are going to write a Python program with Ryu SDN framework to build a simple software-defined network and compare the different between two forwarding rules.

---
## Objectives

1. Learn how to build a simple software-defined networking with Ryu SDN framework
2. Learn how to add forwarding rule into each OpenFlow switch

---
## Execution

### 工作站的密碼
* Container Password: ```0616091```

### How to run your program?

1. 先連到工作站裡面

	```
	ssh -p 16091 root@140.113.195.69
	```
2. 再到topo.py 跟 controller.py 所在的資料夾

	```
	$ cd /root/Route_Configuration/src/	
	``` 
3. 先啟動 topo.py 

	```
	$ [sudo] mn --custom topo.py --topo topo --link tc --controller remote
	```
4. 再啟動 controller.py

	```
	$ [sudo] ryu-manager controller.py --observe- links
	```
5. 先在執行topo.py的terminal執行exit

	```
	mininet > exit
	```
6. 再輸入mn -c 來結束掉controller.py

	```
	$ mn -c
	```

###What is the meaning of the executing command (both Mininet and Ryu controller)?

* ```mn --custom topo.py --topo topo --link tc --controller remote```:
	* ```--custom topo.py```:
	
		使用客製化的.py檔案，所以我們用自己寫的topo.py
	* ```--topo topo```:
		
		使用topo.py裡面的topo
	* ```--link tc```:
	
		使用TCLink來連接
	* ```--controller remote```:
		
		使用遠端的controller，我們使用的是用ryu所建立起來的controller

* ```ryu-manager controller.py --observe- links```:

	* ```ryu-manager controller.py```:
		
		讓ryu-manager 執行controller.py這個程式碼

	
	* ```--observe- links```:

		 觀察連結來看有無事件發生出來
###Show the screenshot of using iPerf command in Mininet (both `SimpleController.py` and `controller.py`)
* SimpleController.py

![/img/img1.png](/image/img.png)

* controller.py

![/img/img6.png](/img/img6.png)

---
## Description

### Tasks

> TODO:
> * Describe how you finish this work in detail

1. Environment Setup

2. Example of Ryu SDN

3. Mininet Topology

4. Ryu Controller

5. Measurement

### Discussion

> TODO:
> * Answer the following questions

1. Describe the difference between packet-in and packet-out in detail.
   
2. What is “table-miss” in SDN?
   
3. Why is "`(app_manager.RyuApp)`" adding after the declaration of class in `controller.py`?
   
4. Explain the following code in `controller.py`.
    ```python
    @set_ev_cls(ofp_event.EventOFPPacketIn, CONFIG_DISPATCHER)
    ```

5. What is the meaning of “datapath” in `controller.py`?
   
6. Why need to set "`ip_proto=17`" in the flow entry?
   
7. Compare the differences between the iPerf results of `SimpleController.py` and `controller.py` in detail.
   
8. Which forwarding rule is better? Why?

---
## References

* **My References** 
	* [使用 RYU 實現簡易 Switch](http://blog.laochanlam.me/2017/11/17/RYU-%E5%AF%A6%E7%8F%BE%E7%B0%A1%E6%98%93-Switch/)
	* [simple_switch_中文詳解.py](https://gist.github.com/aweimeow/d3662485aa224d298e671853aadb2d0f)
	* [mn 介紹](https://manpages.ubuntu.com/manpages/xenial/en/man1/mn.1.html?fbclid=IwAR0P2Q0vNMq4Dv2CDRjJ4TVx98FbEP9qQcPGWm1a7c3c8_cGIqMi9CT4U5M)


* **Ryu SDN**
    * [Ryubook Documentation](https://osrg.github.io/ryu-book/en/html/)
    * [Ryubook [PDF]](https://osrg.github.io/ryu-book/en/Ryubook.pdf)
    * [Ryu 4.30 Documentation](https://github.com/mininet/mininet/wiki/Introduction-to-Mininet)
    * [Ryu Controller Tutorial](http://sdnhub.org/tutorials/ryu/)
    * [OpenFlow 1.3 Switch Specification](https://www.opennetworking.org/wp-content/uploads/2014/10/openflow-spec-v1.3.0.pdf)
    * [Ryubook 說明文件](https://osrg.github.io/ryu-book/zh_tw/html/)
    * [GitHub - Ryu Controller 教學專案](https://github.com/OSE-Lab/Learning-SDN/blob/master/Controller/Ryu/README.md)
    * [Ryu SDN 指南 – Pengfei Ni](https://feisky.gitbooks.io/sdn/sdn/ryu.html)
    * [OpenFlow 通訊協定](https://osrg.github.io/ryu-book/zh_tw/html/openflow_protocol.html)
    
* **Python**
    * [Python 2.7.15 Standard Library](https://docs.python.org/2/library/index.html)
    * [Python Tutorial - Tutorialspoint](https://www.tutorialspoint.com/python/)
* **Others**
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
