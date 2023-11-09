### ICMP协议

    确认 IP 包是否成功送达目标地址、报告发送过程中 IP 包被废弃的原因和改善网络设置等。


    ICMP 报文是封装在 IP 包里面，它工作在网络层，是 IP 协议的助手。

    类型 + 代码 + 校验和 + 数据内容

    traceroute--差错报文类型的使用
    它的原理就是利用 IP 包的生存期限 从 1 开始按照顺序递增的同时发送 UDP 包，强制接收 ICMP 超时消息的一种方法。

    发送主机端每次收到 ICMP 差错报文时就减少包的大小，以此来定位一个合适的 MTU 值，以便能到达目标主机。

### 断网了 还能ping通127.0.0.1吗

**[Click](https://www.baidu.com)**
```
mdhl
要高亮的内容
多行文本也可以
```



<div style="border-left: 5px solid green;">
这是一个绿色的引用块
  
[Click](https://www.baidu.com)
</div>
> ddd
> dafa
> Test
>
> ddd 
> 
> []
> 
> 
> 


    127.0.0.1
        回环地址， 发现目标IP是回环地址时，就会选择本地网卡。

        ping回环地址和ping本机地址没有区别。 都没有走网卡进入网络

    localhost: 127.0.0.1的域名

    如果此时 listen 的是本机的 0.0.0.0 , 那么它表示本机上的所有IPV4地址。