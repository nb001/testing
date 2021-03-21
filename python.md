### python的数据类型：
https://blog.csdn.net/as480133937/article/details/87305247

### python中类的讲解

https://www.cnblogs.com/insane-Mr-Li/p/9758776.html


### python 类的参数

def fun_3(*args):
    print(args)

fun_3(1)
fun_3("hello",1)
fun_3(1,[1,"Hello",False])
fun_3("hello",134,True)

*args 表示任意个参数

python 中 *args 和 **kwargs 的区别
https://www.cnblogs.com/yunguoxiaoqiao/p/7626992.html



class object:
    """ The most base type """

    # del obj.xxx或delattr(obj,'xxx')时被调用，删除对象中的一个属性
    def __delattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement delattr(self, name). """
        pass

    # 对应dir(obj)，返回一个列表，其中包含所有属性和方法名（包含特殊方法）
    def __dir__(self, *args, **kwargs):  # real signature unknown
        """ Default dir() implementation. """
        pass

    # 判断是否相等 equal ，在obj==other时调用。如果重写了__eq__方法，则会将__hash__方法置为None
    def __eq__(self, *args, **kwargs):  # real signature unknown
        """ Return self==value. """
        pass

    # format(obj)是调用，实现如何格式化obj对象为字符串
    def __format__(self, *args, **kwargs):  # real signature unknown
        """ Default object formatter. """
        pass

    # getattr(obj,'xxx')、obj.xxx时都会被调用，当属性存在时，返回值，不存在时报错（除非重写__getattr__方法来处理）。
    # 另外，hasattr(obj,'xxx')时也会被调用（估计内部执行了getattr方法）
    def __getattribute__(self, *args, **kwargs):  # real signature unknown
        """ Return getattr(self, name). """
        pass

    # 判断是否大于等于 greater than or equal，在obj>=other时调用
    def __ge__(self, *args, **kwargs):  # real signature unknown
        """ Return self>=value. """
        pass

    # 判断是否大于 greater than，在obj>other时调用
    def __gt__(self, *args, **kwargs):  # real signature unknown
        """ Return self>value. """
        pass

    # 调用hash(obj)获取对象的hash值时调用
    def __hash__(self, *args, **kwargs):  # real signature unknown
        """ Return hash(self). """
        pass

    def __init_subclass__(self, *args, **kwargs):  # real signature unknown
        """
        This method is called when a class is subclassed.

        The default implementation does nothing. It may be
        overridden to extend subclasses.
        """
        pass

    # object构造函数，当子类没有构造函数时，会调用object的__init__构造函数
    def __init__(self):  # known special case of object.__init__
        """ Initialize self.  See help(type(self)) for accurate signature. """
        pass

    # 判断是否小于等于 less than or equal，在obj<=other时调用
    def __le__(self, *args, **kwargs):  # real signature unknown
        """ Return self<=value. """
        pass

    # 判断是否小于 less than，在obj<other时调用
    def __lt__(self, *args, **kwargs):  # real signature unknown
        """ Return self<value. """
        pass

    # 创建一个cls类的对象，并返回
    @staticmethod  # known case of __new__
    def __new__(cls, *more):  # known special case of object.__new__
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    # 判断是否不等于 not equal,在obj!=other时调用
    def __ne__(self, *args, **kwargs):  # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce_ex__(self, *args, **kwargs):  # real signature unknown
        """ Helper for pickle. """
        pass

    def __reduce__(self, *args, **kwargs):  # real signature unknown
        """ Helper for pickle. """
        pass

    # 如果不重写__str__，则__repr__负责print(obj)和交互式命令行中输出obj的信息
    # 如果重写了__str__，则__repr__只负责交互式命令行中输出obj的信息
    def __repr__(self, *args, **kwargs):  # real signature unknown
        """ Return repr(self). """
        pass

    # 使用setattr(obj,'xxx',value)、obj.xxx=value是被调用（注意，构造函数初始化属性也要调用）
    def __setattr__(self, *args, **kwargs):  # real signature unknown
        """ Implement setattr(self, name, value). """
        pass

    # 获取对象内存大小
    def __sizeof__(self, *args, **kwargs):  # real signature unknown
        """ Size of object in memory, in bytes. """
        pass

    # 设置print(obj)打印的信息，默认是对象的内存地址等信息
    def __str__(self, *args, **kwargs):  # real signature unknown
        """ Return str(self). """
        pass

    @classmethod  # known case
    def __subclasshook__(cls, subclass):  # known special case of object.__subclasshook__
        """
        Abstract classes can override this to customize issubclass().

        This is invoked early on by abc.ABCMeta.__subclasscheck__().
        It should return True, False or NotImplemented.  If it returns
        NotImplemented, the normal algorithm is used.  Otherwise, it
        overrides the normal algorithm (and the outcome is cached).
        """
        pass
    # 某个对象是由什么类创建的，如果是object，则是type类<class 'type'>
    __class__ = None
    # 将对象中所有的属性放入一个字典，例如{'name':'Leo','age':32}
    __dict__ = {}
    # 类的doc信息
    __doc__ = ''
    # 类属于的模块,如果是在当前运行模块，则是__main__，如果是被导入，则是模块名（即py文件名去掉.py）
    __module__ = ''

    你可以把object理解为一个很大的类，然后加括号表示继承object里，
    然后即可调用object里的这些双下划线的方法




    ### python 函数的参数传递
    https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888