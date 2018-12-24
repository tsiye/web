#What happened when I entered www.google.com in the browser
1. A current loop is closed when we press the 'enter' key.

2. The keyboard controller received the signal and coded it.

3. Xserver map it into scan code, and window server and the window server's graphics API displays character. 		

4. Meanwhile, browser analysis the URL to determine it is URL or keyword

5. If it is not a URL, the browser would transfer the text to the search engine with a specific string

6. Check the **HSTS list**(Chrome has it) and find that www.google.com are supposed to connect by https to secure the data.

7. Now it is time for us to find the **IP address**.
	first check the cache in the browser 
	
8. Then use library function `gethostbyname` to search in the local Hosts
different system has different hosts location

9. If it fails to find in the **hosts**(of course it is almost impossible), sending query request to DNS server is necessary. DNS server is always the local router or cache DNS server of internet service provider in **port 53**. 

10. **8.8.8.8** is the DNS server provide by google. It can return the IP address

11. If 8.8.8.8 cannot find the IP, it will turn to one of the 13 root servers and their mirror servers for help.

12. We use[ARP](https://zh.wikipedia.org/wiki/%E5%9C%B0%E5%9D%80%E8%A7%A3%E6%9E%90%E5%8D%8F%E8%AE%AE)(adress resolution protocol, which is a protocol to get MAC of target host using target IP) during the processing of DNS searching and google.com linking.

13. The browser get the IP address of target server.

14. The browser use the IP address and the port from URL(Https is 443) to call the system function `socket`, asking for a TCP socket.
 
15. This request is sent to transport layer, packing to TCP segment.  

16. Add the target port at head and select source port at the kernel of system

17. The TCP segment is sent to Internet layer, an IP header which contains IP address of target server and local is added, packaging to an IP segment

18. The IP segment enter the link layer and add frame header, which contains the MAC.

19. This segment start from local computer, the modem change the digital signal to analog signal

20. The package will reach the router managing the local subnets.

21. It will pass the edge router of autonomous system and reach the target router.

22. These routers will extract the target address from its header and send it to the destination. 

23. If the TTL(time to live) = 0 or the internet is stuffed, this package will be throw away.

24. Three-way handshake of TCP

25. Client choose ISN, and send the SYN to server.

26. Server choose its ISN and add SYN + 1 to ACK to indicate it has received the package.

27.The client add the sequence and ACK + 1 and now the link has been established.

28. During the process of data, the seq will add n if N bytes has been transferred. When another side received the package, it will send an ACK, choosing the last sequence number of its received-package.

29.  Firstly, the client send `clientHello` to server, containing its TLS version, available Encryption algorithm and compression algorithm.

30. The server send `serverHello` to client, also containing the messages above and the certificate from CA and public key.

31. The client verify the certificate according to its CA list and use the public key to encrypt a string of random number .

32. The server use its private key to decrypt the random string, and use it as its symetric key.

33. The client and the server use the syemetic key to encrypt from now on. 

34. The google server received the package and send its homepage back.

35. The server send the resoure back, ir contains html, css, js, graph。 

36. The browser analysis the html.

37. Load the external resources(css, js, graph)

38. Page rendering, the browser traversing the dom tree.

39. GPU rendering. 

40. We see the page.
###reference
1. 网址（url），域名，ip地址，dns，hosts之间的关系 https://www.cnblogs.com/fangzuchang/p/6702023.html
2. 在浏览器地址栏输入一个URL后回车，背后会进行哪些技术步骤？ https://mp.weixin.qq.com/s?__biz=MzIxNTM3NDE2Nw==&mid=2247484094&idx=1&sn=4d03c384672cc2f78a13b1dfc6b65efe&chksm=97980286a0ef8b901eb38c667cec796d7cf44c6f303e41c6ab5901ff8aa42d1c8fd683bd854e&token=758955454&lang=zh_CN#rd
3. https://github.com/skyline75489/what-happens-when-zh_CN/blob/master/README.rst
4. ARP https://zh.wikipedia.org/wiki/%E5%9C%B0%E5%9D%80%E8%A7%A3%E6%9E%90%E5%8D%8F%E8%AE%AE
