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

### What is the meaning of the executing command (both Mininet and Ryu controller)?

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

### SimpleController.py forwarding by this picture

![/img/img3.png](/img/img3.png)

### controller.py forwarding by this picture

![/img/img8.png](/img/img4.png)

### Show the screenshot of using iPerf command in Mininet (both `SimpleController.py` and `controller.py`)

* 可以先用```mininet> pingall```來確定h1與h2有順利連線
* 再輸入```mininet> h1 iperf -s -u -i 1 –p 5566 > ./out/result1 &``` 以及 ```h2 iperf -c 10.0.0.1 -u –i 1 –p 5566```來將結果輸出到/out/result1去

* SimpleController.py的結果輸出到result1，controller.py輸出到result2

* SimpleController.py

	![/img/img2.png](/img/img2.png)

* controller.py

	![/img/img8.png](/img/img8.png)

---
## Description

### Tasks

1. **Environment Setup**

	用ssh連到學校的工作站裡面，然後clone github上面的檔案下來到 Route_Configuration資料夾裡面，用sudo mn 是跑看看mininet有無問題。

2. **Example of Ryu SDN**

	1. 用ssh連到學校的工作站裡面，並且cd到SimpleTopo.py所在的資料夾。
	
	2. 先執行```$ [sudo] mn --custom SimpleTopo.py --topo topo --link tc --controller remote```

		* 若發生像是"RTNETLINK answers: File exists"的問題，可以用mn -c 來將mininet清乾淨。

	3. 再執行```[sudo] ryu-manager SimpleController.py --observe-links```

	4. 要離開Ryu controller的話，先在SimpleTopo.py的terminal輸入```mininet> exit```

	5. 再到 SimpleController.py 的 terminal 執行 ```ctrl-z```

	6. 最後再輸入```$ mn -c```來確保RTNETLINK有被清乾淨

3. Mininet Topology

	1. 先在src資料夾裡面，輸入```$ cd SimpleTopo.py topo.py```來將SimpleTopo.py的程式碼複製到topo.py裡面

	2. 再依照topo/topo.png來新增bandwidth, delay, and loss rate上去
		
		![/src/topo/topo.png](/src/topo/topo.png)
	3. 先在終端機跑topo.py
	 
		```$mn --custom topo.py --topo topo --link tc --controller remote```

	4. 再到另外一個終端機跑SimpleController.py
	
		```$ryu-manager SimpleController.py --observe-links``` 
		
	5. 出現![/img/img5.png](/img/img5.png)

		表示你的 controller.py 有問題，需要進行修改。
	6. 出現![/img/img6.png](/img/img6.png)

		表示你的 topo.py 有問題，需要進行修改。
	7. 可以在Mininet’s CLI mode用 ping 來測試連接
	
		Example:```mininet> h1 ping h2```

4. Ryu Controller

	1. 先在src資料夾裡面，輸入```$ cd SimpleController.py controller.py```來將SimpleController.py的程式碼複製到controller.py裡面

	2. 再依照![/img/img4.png](/img/img4.png)來修改controller.py

	3. 將controller.py裡面的```def switch_features_handler(self, ev)```內容，依據上面圖片的要求來設定，其他部分不需要做任何的變動。

5. Measurement

	1. 先在終端機跑topo.py

		```$mn --custom topo.py --topo topo --link tc --controller remote```
		
	2. 再到另外一個終端機跑SimpleController.py
	
		```$ryu-manager SimpleController.py --observe-links``` 
		
	3. 用 iPerf commands 來進行測試，並將結果輸出到result1，最後結束程式運行。
		```mininet> h1 iperf -s -u -i 1 –p 5566 > ./out/result1 &```
		
		```mininet> h2 iperf -c 10.0.0.1 -u –i 1 –p 5566```
		
		```mininet> exit```
		
		```mn -c```
	4. 再來是在跑一次topo.py

		```$mn --custom topo.py --topo topo --link tc --controller remote```
	
	5. 再到另外一個終端機跑controller.py

		```$ryu-manager controller.py --observe-links```
	6. 一樣用 iPerf commands 來進行測試，並將結果輸出到result2，最後結束程式運行。

		```mininet> h1 iperf -s -u -i 1 –p 5566 > ./out/result2 &```
		
		```mininet> h2 iperf -c 10.0.0.1 -u –i 1 –p 5566```
		
		```mininet> exit```
		
		```mn -c```
6. 最後跑出來的結果

	* SimpleController.py

	![/img/img2.png](/img/img2.png)

	* controller.py

	![/img/img8.png](/img/img8.png)

### Discussion

1. Describe the difference between packet-in and packet-out in detail.

	```packet-in```是指將接到的封包轉送到 controller 的動作。而```packet-out```則是將從 controller 傳送到的封包轉送到指定的連接埠。
   
2. What is “table-miss” in SDN?

	當有封包傳入 switch 的時候，會解開封包的標頭區，再根據流程表進行配對，若沒有配對成功，則到下一個流程表，直到配對成功並決定應該採取的動作為止。若該封包沒有符合任何一個流程表的配對，便是“table-miss"。當發生"table-miss"時，會根據“table-miss flow entry”來做決定。
   
3. Why is "`(app_manager.RyuApp)`" adding after the declaration of class in `controller.py`?

	class xxx(something):表示 xxx 這個 class 將會繼承 something 這個父class。在 controller.py 裡面，我們寫```class SimpleController1(app_manager.RyuApp)```，表示說```SimpleController1```這個class將會繼承```ryu.base.app_manager.RyuApp```，因為所有有關ryu的應用程式都必須繼承 app_manager.RyuApp 。
   
4. Explain the following code in `controller.py`.
    ```python
    @set_ev_cls(ofp_event.EventOFPPacketIn, CONFIG_DISPATCHER)
    ```

    1. 這是一個```decorator```，主要是讓函式成為在特定狀態接收特定封包的 Handler。
    
    2. ```@set_ev_cls```則指定事件類別得以接受訊息和交換器狀態作為參數。

    3. 事件類別的規則為```ryu.controller.ofp_event.EventOFP + <OpenFlow訊息名稱>```，所以程式碼裡的```ofp_event.EventOFPPacketIn```是事件的名稱，而```PacketIn```便是OpenFlow訊息名稱。```PacketIn```代表的是在 Packet-In 訊息的狀態下。
    
    4. ```CONFIG_DISPATCHER```則是表示狀態，```CONFIG_DISPATCHER```所代表的是```接收 SwitchFeatures訊息```。 
    
5. What is the meaning of “datapath” in `controller.py`?

	datapath 在 controller.py 裡面，是作為 switch 的實體來做運用。
   
6. Why need to set "`ip_proto=17`" in the flow entry?
	
	```ip_proto``` 是代表什麼網路協定類型，為了讓 flow 用UDP協定來傳輸，所以需要設定```ip_proto```，而UDP協定的protocol numbers是17，所以設定成```ip_proto=17```。
   
7. Compare the differences between the iPerf results of `SimpleController.py` and `controller.py` in detail.

	兩個主要的差別，在於h2 -> h1 傳送的途徑：
	
	```SimpleController.py```是 h2 -> s3 -> s1 -> h1。
	
	```controller.py```是 h2 -> s3 -> s2 -> s1 -> h1。
	
	controller.py在中間多經過了s2這個switch。
	
	SimpleController.py 的結果為 result1，controller.py的結果為 result2。
	
	result1 ![/img/img9.png](/img/img9.png)
	
	result2 ![/img/img10.png](/img/img10.png)
	
	從結果來看，result2 遺失的資料比較多，為1.9%，而result1 遺失的資料較少，為 1.2% 。再來看到 Bandwidth ，result1 與 result2 相近，但result1大部分都比較大ㄧ點點。最後看到 Jitter ，result1 與 result2 相近的，只有 3 - 4秒、4 - 5秒以及最後一筆資料，result2 是明顯大於 result1 的。
8. Which forwarding rule is better? Why?

	我個人是覺得就數據來講，result1 (也就是SimpleController.py)的方式會比較好，因為延遲較少，lost 的 Datagrams 也比較少，會是比較好的forwarding rule。但我覺得因為傳輸的資料量太少，檔案也太小，所以感覺不太出來差異。

---
## References

* **My References** 
	* [使用 RYU 實現簡易 Switch](http://blog.laochanlam.me/2017/11/17/RYU-%E5%AF%A6%E7%8F%BE%E7%B0%A1%E6%98%93-Switch/)
	* [simple_switch_中文詳解.py](https://gist.github.com/aweimeow/d3662485aa224d298e671853aadb2d0f)
	* [mn referemce](https://manpages.ubuntu.com/manpages/xenial/en/man1/mn.1.html?fbclid=IwAR0P2Q0vNMq4Dv2CDRjJ4TVx98FbEP9qQcPGWm1a7c3c8_cGIqMi9CT4U5M)
	* [ryu-manager reference](https://manpages.ubuntu.com/manpages/xenial/en/man8/ryu-manager.8.html)
	* [List of IP protocol numbers](https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers)
	* [交換器(Switching Hub)](https://osrg.github.io/ryu-book/zh_tw/html/switching_hub.html)
	* [SDN 筆記](https://ppundsh.github.io/posts/2a39/)
	* [繼承](https://openhome.cc/Gossip/Python/Inheritance.html)


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
