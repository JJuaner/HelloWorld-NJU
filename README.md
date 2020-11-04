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

2.玩转 WSL 并配置Linux下的开发调试环境(linux自带python) https://zhuanlan.zhihu.com/p/49227132

3.Ubuntu系统下conda的安装、配置、使用<br>
conda是什么，有什么用：虚拟环境管理器(创建高度独立的虚拟环境)+包管理器https://blog.csdn.net/zhouchen1998/article/details/84671528
https://blog.csdn.net/weixin_43840215/article/details/89599559 <br>
https://www.cnblogs.com/liangxuran/p/13473664.html<br>
Miniconda官网：https://docs.conda.io/en/latest/miniconda.html <br>

4.Ubuntu系统下conda工具下pytorch的安装 <br>
https://blog.csdn.net/liuzhuomei0911/article/details/89784998 <br>
https://blog.csdn.net/tuyim7124/article/details/80723997 <br>
pytorch官网（get started）：https://pytorch.org/get-started/locally/#anaconda <br>
（因为实验室台式机是集显无独显，就没装cuda）

5.CUDA:NVIDIA并行计算库<br>
CUDA是Nvidia推出的只能用于自家GPU的并行计算框架。只有安装这个框架才能够进行复杂的并行计算。主流的深度学习框架也都是基于CUDA进行GPU并行加速的，几乎无一例外。还有一个叫做cudnn，是针对深度卷积神经网络的加速库。

## Day3(2020.9.22)
1.教育邮箱、安装pycharm、激活
https://www.jarod8.cn/index.php/archives/5/

## Day4(2020.9.23)
1.学习pytorch 官网tutorial

## Day5(2020.9.29)
1.踩坑pycharm不支持wsl虚拟环境(wsl+conda+pycharm不行)<br>
2.目标使用自带python,环境乱七八糟不太懂
>>直接卸载重新安装wsl<br>
>>安装后注意修改源并更新<br>
>>`sudo apt install python3-pip`装pip包管理工具<br>
>>安装pytorch
>>>坑：pycharm中import torch不能识别，重启pycharm！！

## Day6(2020.10.7)
1.pycharm
>>main+enter/tab  

2.矩阵论编程作业  
>>算法原理：OMP贪婪迭代算法的正交匹配算法 https://zhuanlan.zhihu.com/p/52276805  
>>编程实现：pytorch+线性代数
>>>torch.randn @  torch.cat ZeroPad2d(0填充)  
>>>matrix.t() matrix.pinverse()矩阵的伪逆
>>>np.argmax() np.array()

## Day7(2020.10.8)
1.TCA论文
>>学习KL散度 https://www.jianshu.com/p/43318a3dc715  
>>学习核函数

## Day8(2020.10.10)
1.git代码:踩坑pycharm不支持wsl1的git，所以考虑：
>>1.不通过pycharm直接使用wsl的git操作文件   
>>2.windows安装git：github是服务端，要想在自己电脑上使用git我们还需要一个git客户端  
>>>模式一：https://blog.csdn.net/galoislyj/article/details/53552182  
>>>模式二：https://www.cnblogs.com/xueweisuoyong/p/11914045.html  https://www.cnblogs.com/cxk1995/p/5800196.html

## Day9(2020.10.11)
1.实现BST构造及其前序中序的栈遍历  
2.熟悉repo->本地模式2，代码提交到mian(git push origin main)，并解决每次提交需要输密码问题https://www.cnblogs.com/sky6862/p/7992736.html    
3.阅读点点第2篇多标签论文  

## Day10(2020.10.16)
1.阅读JDA论文
>>学习《统计学习方法》PCA  

## Day11(2020.10.17)
1.复现JDA代码
>>a.参考王晋东github：https://github.com/jindongwang/transferlearning/blob/master/code/traditional/JDA/JDA.py  
>>b.pip导包：1.打开的目录pip即可 2.注意使用pip3 3.如果极慢第一次记得修改镜像源
1)创建文件夹 mkdir -p 文件夹名  p 确保目录名称存在，不存在的就建一个。   
2)创建文件  如：touch a.txt    
https://www.cnblogs.com/feifanrensheng/p/9669769.html  

## Day(2020.10.30)
pycharm连接远程服务器
https://www.cnblogs.com/zhuminghui/p/10947930.html

## Day(2020.10.31)
AS
>>git clone报错 OpenSSL SSL_connect: Connection was reset in connection to github.com:443  解决：https://www.jianshu.com/p/3ca2d0f049e7    
>>Gradle sync failed: Read timed out报错，解决：https://blog.csdn.net/mxy19891106/article/details/105826939/

## Day(2020.11.2)
fix DAN（Xlearn）代码：1.datalist路径 2.narrow //  3.data[0]->data.item()    
MMD的平方理解 https://www.zhihu.com/question/288185961

