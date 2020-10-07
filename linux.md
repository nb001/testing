### docker

```docker exec -it mysql-test bash```   进入到容器命令


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


 按ESC键 跳到命令模式，然后：

:w   保存文件但不退出vi

:w file 将修改另外保存到file中，不退出vi

:w!   强制保存，不推出vi

:wq  保存文件并退出vi

:wq! 强制保存文件，并退出vi

q:  不保存文件，退出vi

:q! 不保存文件，强制退出vi

:e! 放弃所有修改，从上次保存文件开始再编辑

KubeSphere 

### docker部署django项目
https://blog.csdn.net/hbnn111/article/details/77176629

https://segmentfault.com/a/1190000017034025 

https://www.cnblogs.com/xueweihan/p/11649630.html



### docker 的远程访问


    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'northblue',
        'PORT':3306,
        'USER':'root',
        'HOST':'127.0.0.1',
        'PASSWORD':'Nb1234567',
    }


    https://cloud.tencent.com/document/product/296/9604

安全运行方案 关闭root登陆权限
https://www.94ip.com/post/851.html

linux运维安全
https://blog.csdn.net/weixin_34216196/article/details/92858043



超级用户无法直接登陆 普通用户登陆之后获取超级用户的所有权限无需输入密码 这个对比超级用户直接登陆 安全性在哪里？

https://blog.csdn.net/weixin_44985068/article/details/97612969?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-1.channel_param


    1. 什么原因导致了无缘无故的进程出现
    2. 怎么修改回密码登陆 服务器
    3. 这个进程一运行 我所有的进程就会被关闭

运维信息安全

https://www.cnblogs.com/jxk001/p/9994252.html

安全运维需要注意的事项
https://blog.csdn.net/weixin_34216196/article/details/92858043
安装完centos必须要做的7件事
http://www.360doc.com/content/17/0717/11/13518188_672035607.shtml


linux 加固方案
https://www.cnblogs.com/heaven-xi/p/9984561.html

日常运维十大技能
https://blog.csdn.net/qq_29677867/article/details/90045048

CentOS SSH密钥登陆改为密码登陆
https://blog.csdn.net/zjqlovell/article/details/79399265


基于K8S的技术 kubesphere
https://kubesphere.com.cn/service-mesh/

电商行业解决方案
https://www.qingcloud.com/solutions/ecommerce/