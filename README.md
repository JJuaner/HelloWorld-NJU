# HelloWorld
## Day1(2020.9.20)
1.找回github账号，熟悉github页面、操作术语（repository、profile简介、gist要点、fork复刻、pull request求拉）<br>
2.配置新电脑：
>>a.查看配置（cpu内存、显卡、硬盘）<br>
>>b.磁盘分区、转储软件 <br>
>>c.操作系统：wsl（windows subsystem for linux） https://zhuanlan.zhihu.com/p/49227132<br> 
>>d.vpn：安装配置ShadowsocksR-win-4.9.2、访问固定google<br> 

## Day2(2020.9.21)
1.linux vim操作
>> esc 切换命令模式
>>> i  insert<br> 
>>> u  撤销一次操作<br> 
>>> Ctrl+r 恢复上一步被撤销的操作<br> 
>>>:w   保存文件但不退出vi<br> 
>>>:w!   强制保存，不推出vi<br> 
>>>:wq  保存文件并退出vi<br> 
>>>:wq! 强制保存文件，并退出vi<br> 
>>>:q  不保存文件，退出vi<br> 
>>>:q! 不保存文件，强制退出vi<br> 
>>>:e! 放弃所有修改，从上次保存文件开始再编辑<br> 

2.玩转 WSL 并配置Linux下的开发调试环境 https://zhuanlan.zhihu.com/p/49227132

3.Ubuntu系统下conda的安装、配置、使用<br>
https://blog.csdn.net/weixin_43840215/article/details/89599559 <br>
Miniconda官网：https://docs.conda.io/en/latest/miniconda.html <br>

4.Ubuntu系统下conda工具下pytorch的安装 <br>
https://blog.csdn.net/liuzhuomei0911/article/details/89784998 <br>
pytorch官网（get started）：https://pytorch.org/get-started/locally/#anaconda <br>
（因为实验室台式机是集显无独显，就没装cuda）

5.CUDA:NVIDIA并行计算库<br>
CUDA是Nvidia推出的只能用于自家GPU的并行计算框架。只有安装这个框架才能够进行复杂的并行计算。主流的深度学习框架也都是基于CUDA进行GPU并行加速的，几乎无一例外。还有一个叫做cudnn，是针对深度卷积神经网络的加速库。

