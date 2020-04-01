1、logging模块的位置级别
DEBUG	最详细的日志信息，典型应用场景是 问题诊断
INFO	信息详细程度仅次于DEBUG，通常只记录关键节点信息，用于确认一切都是按照我们预期的那         样进行工作
WARNING	当某些不期望的事情发生时记录的信息（如，磁盘可用空间较低），但是此时应用程序还是正        常运行的
ERROR	由于一个更严重的问题导致某些功能不能正常运行时记录的信息
CRITICAL	当发生严重错误，导致应用程序不能继续运行时记录的信息

2、logging模块的使用方法

第一种方式是使用logging提供的模块级别的函数
logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
logging.basicConfig(**kwargs)	对root logger进行一次性配置

第二种方式是使用Logging日志系统的四大组件
loggers	提供应用程序代码直接使用的接口
handlers	用于将日志记录发送到指定的目的位置
filters	提供更细粒度的日志过滤功能，用于决定哪些日志记录将会被输出（其它的日志记录将会被忽略）
formatters	用于控制日志信息的最终输出格式

日志器（logger）需要通过处理器（handler）将日志信息输出到目标位置，如：文件、sys.stdout、网络等；
不同的处理器（handler）可以将日志输出到不同的位置；
日志器（logger）可以设置多个处理器（handler）将同一条日志记录输出到不同的位置；
每个处理器（handler）都可以设置自己的过滤器（filter）实现日志过滤，从而只保留感兴趣的日志；
每个处理器（handler）都可以设置自己的格式器（formatter）实现同一条日志以不同的格式输出到不同的地方。
简单点说就是：日志器（logger）是入口，真正干活儿的是处理器（handler），处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。

logger类
Logger对象有3个任务要做：
1）向应用程序代码暴露几个方法，使应用程序可以在运行时记录日志消息；
2）基于日志严重等级（默认的过滤设施）或filter对象来决定要对哪些日志进行后续处理；
3）将日志消息传送给所有感兴趣的日志handlers。

Logger对象最常用的方法分为两类：配置方法 和 消息发送方法
Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象

关于Logger.setLevel()方法的说明：
内建等级中，级别最低的是DEBUG，级别最高的是CRITICAL。例如setLevel(logging.INFO)，此时函数参数为INFO，那么该logger将只会处理INFO、WARNING、ERROR和CRITICAL级别的日志，而DEBUG级别的消息将会被忽略/丢弃

方法	                                                                                              描述
Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical()	创建一个与它们的方法名对应等级的日志记录
Logger.exception()	                                                                创建一个类似于Logger.error()的日志消息
Logger.log()	                                                                        需要获取一个明确的日志level参数来创建一个日志记录

Logger.exception()与Logger.error()的区别在于：Logger.exception()将会输出堆栈追踪信息，另外通常只是在一个exception handler中调用该方法。
Logger.log()与Logger.debug()、Logger.info()等方法相比，虽然需要多传一个level参数，显得不是那么方便，但是当需要记录自定义level的日志时还是需要该方法来完成。

那么，怎样得到一个Logger对象呢？一种方式是通过Logger类的实例化方法创建一个Logger类的实例，但是我们通常都是用第二种方式--logging.getLogger()方法。

logging.getLogger()方法有一个可选参数name，该参数表示将要返回的日志器的名称标识，如果不提供该参数，则其值为'root'。若以相同的name参数值多次调用getLogger()方法，将会返回指向同一个logger对象的引用。

关于logger的层级结构与有效等级的说明：

logger的名称是一个以'.'分割的层级结构，每个'.'后面的logger都是'.'前面的logger的children，例如，有一个名称为 foo 的logger，其它名称分别为 foo.bar, foo.bar.baz 和 foo.bam都是 foo 的后代。
logger有一个"有效等级（effective level）"的概念。如果一个logger上没有被明确设置一个level，那么该logger就是使用它parent的level;如果它的parent也没有明确设置level则继续向上查找parent的parent的有效level，依次类推，直到找到个一个明确设置了level的祖先为止。需要说明的是，root logger总是会有一个明确的level设置（默认为 WARNING）。当决定是否去处理一个已发生的事件时，logger的有效等级将会被用来决定是否将该事件传递给该logger的handlers进行处理。
child loggers在完成对日志消息的处理后，默认会将日志消息传递给与它们的祖先loggers相关的handlers。因此，我们不必为一个应用程序中所使用的所有loggers定义和配置handlers，只需要为一个顶层的logger配置handlers，然后按照需要创建child loggers就可足够了。我们也可以通过将一个logger的propagate属性设置为False来关闭这种传递机制。

Handler类
Handler对象的作用是（基于日志消息的level）将消息分发到handler指定的位置（文件、网络、邮件等）。Logger对象可以通过addHandler()方法为自己添加0个或者更多个handler对象。比如，一个应用程序可能想要实现以下几个日志需求：

1）把所有日志都发送到一个日志文件中；
2）把所有严重级别大于等于error的日志发送到stdout（标准输出）；
3）把所有严重级别为critical的日志发送到一个email邮件地址。
这种场景就需要3个不同的handlers，每个handler复杂发送一个特定严重级别的日志到一个特定的位置。

一个handler中只有非常少数的方法是需要应用开发人员去关心的。对于使用内建handler对象的应用开发人员来说，似乎唯一相关的handler方法就是下面这几个配置方法：
Handler.setLevel()	设置handler将会处理的日志消息的最低严重级别
Handler.setFormatter()	为handler设置一个格式器对象
Handler.addFilter() 和 Handler.removeFilter()	为handler添加 和 删除一个过滤器对象
需要说明的是，应用程序代码不应该直接实例化和使用Handler实例。因为Handler是一个基类，它只定义了素有handlers都应该有的接口，同时提供了一些子类可以直接使用或覆盖的默认行为。下面是一些常用的Handler：
Handler	描述
logging.StreamHandler	将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
logging.FileHandler	将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
logging.handlers.RotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按大小切割
logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
logging.handlers.HTTPHandler	将日志消息以GET或POST的方式发送给一个HTTP服务器
logging.handlers.SMTPHandler	将日志消息发送给一个指定的email地址
logging.NullHandler	该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。

Formater类
Formater对象用于配置日志信息的最终顺序、结构和内容。与logging.Handler基类不同的是，应用代码可以直接实例化Formatter类。另外，如果你的应用程序需要一些特殊的处理行为，也可以实现一个Formatter的子类来完成。

Formatter类的构造方法定义如下：

logging.Formatter.__init__(fmt=None, datefmt=None, style='%')
可见，该构造方法接收3个可选参数：

fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'
