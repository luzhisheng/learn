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

启动docker
-p 映射
docker80端口映射到本地8080端口
-d 守护进程
sudo docker run -p 8080:80 -d nginx

拷贝文件到容器中,页面显示index.html
vim index.html
sudo docker cp index.html 6ad3b7eaf18d://usr/share/nginx/html

查看正在运行的doc容器
sudo docker ps

停止docker容器
sudo docker stop id

docker在容器内的改动都是缺省的,暂时的,需要创建本地镜像。
commit 保存改动
sudo docker commit -m 'fun' 8e23fe5168ca nginx-fun

删除镜像
sudo docker rmi id

查看所有doc容器
sudo docker ps -a

删除容器
sudo docker rm id

删除所有容器
sudo docker rm `sudo docker ps -a -q`

启动一个镜像
sudo docker run -p 8080:80 -d nginx

编辑文件,创建镜像
FROM alpine:latest #基础镜像,类似于python对象继承object
MAINTAINER ayf #共享的时候告诉别人,这是我写的
CMD echo 'hello docker' #打印的信息

# 创建文件
mkdir docker
cd docker
touch Dorkerfile

# vim
FROM alpine:latest #基础镜像,类似于python对象继承object
MAINTAINER ayf #共享的时候告诉别人,这是我写的
CMD echo 'hello docker' #打印的信息

# 构建镜像
-t 标签名hello_docker
. 路径
docker build -t hello_docker .

#生成docker images
#列出所有镜像
sudo docker images
sudo dcoker

#创建一个镜像文件
FROM ubuntu
MAINTAINER ayf
RUN apt-get update
RUN apt-get install -y nginx
COPY index.html /var/www/html
ENTRYPOINT ["/usr/sbin/nginx", '-g', 'daemon off;']
EXPOSE 80

#构建镜像
sudo docker build -t ayf/nginx .

#启动容器
sudo docker run -d -p 8080:80 ayf/nginx

