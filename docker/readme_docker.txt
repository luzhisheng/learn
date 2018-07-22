docker
1、解决了很多痛点，他能软件包装的问题，能使开发和运维用同一个语言进行沟通。
2、docker是云计算的技术，教程中用到大量的shell命令行

什么是docker
1、官方：开源的项目，将任何的应用进行打包，运行
2、node.js：docker允许一个运行程序用一种标准的单位来打包
3、docker我们可以粗糙的理解为轻量的虚拟机
4、开了挂的chroot
5、docker没有虚拟层，所以比虚拟机更加轻量化


docker下载(ubuntu)
sudo wget -qO- https://get/docker.com | sh
wget命令用来从指定的URL下载文件
-q：不显示指令执行过程；
O-:直接标准输出，不输出文件
