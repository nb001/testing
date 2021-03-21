
### docker部署

https://zhuanlan.zhihu.com/p/98314609




### 意象商城

https://doc.yixiang.co/guide/#%E9%A1%B9%E7%9B%AE%E7%AE%80%E4%BB%8B


https://yshop.org/pages/work-with-us


django-oscar
E-Commerce
Satchmo

### docker

```docker exec -it mysql-test bash```   进入到容器命令
```docker run -it --name web_demo -p 8000:80  aaa:v1  /bin/bash``` docker根据镜像启动容器并且指定端口
第一个为宿主机端口 第二个为容器内部端口 将容器命名为 web_demo 使用 aaa:v1镜像
```mysql -u root -p```

```Password：Nb123456```

``` docker rmi mysql:8.0 docker ``` 删除某个镜像文件

```docker inspect 0b0d9192ee45```  查看容器相关信息
```dokcer port 容器名 端口名```    查看容器映射的宿主机端口 


```docker stop containername```停止容器
``` docker rm containername``` delete container


``` vim filename ``` use vim to open the filename
use the keyboard "i" to edit the config files.
and use the "esc" to quit the configuration status.
use the shift+: to give the command 
use the "wq!" to write the files and quit.


 ### docker django 部署参考帖子
  https://zhuanlan.zhihu.com/p/141976805
进入到django容器内部 运行 ```python3 manage.py runserver 0.0.0.0:8000``` 指定在容器内部运行的端口为8000 
ctrl + p + q 退出容器但是不结束容器


  https://www.zhihu.com/question/37792200

  docker history 命令的使用
  https://www.cnblogs.com/cooper-73/p/9830371.html

  关于docker的木马问题
  https://www.blog.lijinghua.club/article/180

  docker 的安全接口问题

  http://www.dockerinfo.net/1760.html

  docker TLS配置参数
  https://www.cnblogs.com/smlile-you-me/p/7524406.html

  ### docker启用TLS进行安全配置

  https://www.cnblogs.com/xiaoqi/p/docker-tls.html
  https://blog.csdn.net/dounine/article/details/74840080
  https://blog.csdn.net/m0_47161295/article/details/108842097

  ### docker部署django项目

  https://segmentfault.com/a/1190000017034025
  https://blog.csdn.net/hbnn111/article/details/77176629
  https://blog.csdn.net/larger5/article/details/81252773?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param
  
 

  ### dockerfile文件详解

  https://blog.csdn.net/swinfans/article/details/84577445


  ### 80端口被封
  https://jingyan.baidu.com/article/c910274b909275cd361d2d89.html