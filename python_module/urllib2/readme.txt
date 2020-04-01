1、urllib和urllib2的difference
urllib2可以接受一个Request对象，并以此可以来设置一个URL的headers，但是urllib只接收一个URL。这意味着，你不能伪装你的用户代理字符串等。
urllib模块可以提供进行urlencode的方法，该方法用于GET查询字符串的生成，urllib2的不具有这样的功能。这就是urllib与urllib2经常在一起使用的原因。

2、urllib2概述
(1) urllib2模块定义的函数和类用来获取URL（主要是HTTP的），他提供一些复杂的接口用于处理： 基本认证，重定向，Cookies等。
(2) urllib2支持许多的“URL schemes”（由URL中的“：”之前的字符串确定 - 例如“FTP”的URL方案如“ftp://python.org/”），且他还支持其相关的网络协议（如FTP，HTTP）。我们则重点关注HTTP。
(3) 在简单的情况下，我们会使用urllib2模块的最常用的方法urlopen。但只要打开HTTP URL时遇到错误或异常的情况下，就需要一些HTTP传输协议的知识。我们没有必要掌握HTTP RFC2616。这是一个最全面和最权威的技术文档，且不易于阅读。在使用urllib2时会用到HTTP RFC2616相关的知识，了解即可。

3、常用方法和类
(1) urllib2.urlopen(url[, data] [, timeout])
    urlopen方法是urllib2模块最常用也最简单的方法，它打开URL网址，url参数可以是一个字符串url或者是一个Request对象。URL没什么可说的，Request对象和data在request类中说明，定义都是一样的。
    对于可选的参数timeout，阻塞操作以秒为单位，如尝试连接（如果没有指定，将使用设置的全局默认timeout值）。实际上这仅适用于HTTP，HTTPS和FTP连接。
    urlopen方法也可通过建立了一个Request对象来明确指明想要获取的url。调用urlopen函数对请求的url返回一个response对象。这个response类似于一个file对象，所以用.read()函数可以操作这个response对象，关于urlopen函数的返回值的使用，我们下面再详细说。
(2) class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])
    Request类是一个抽象的URL请求。5个参数的说明如下
    URL——是一个字符串，其中包含一个有效的URL。
    data——是一个字符串，指定额外的数据发送到服务器，如果没有data需要发送可以为“None”。目前使用data的HTTP请求是唯一的。当请求含有data参数时，HTTP的请求为POST，而不是GET。数据应该是缓存在一个标准的application/x-www-form-urlencoded格式中。urllib.urlencode()函数用映射或2元组，返回一个这种格式的字符串。通俗的说就是如果想向一个URL发送数据（通常这些数据是代表一些CGI脚本或者其他的web应用）。对于HTTP来说这动作叫Post。例如在网上填的form（表单）时，浏览器会POST表单的内容，这些数据需要被以标准的格式编码（encode），然后作为一个数据参数传送给Request对象。Encoding是在urlib模块中完成的，而不是在urlib2中完成的。
    headers——是字典类型，头字典可以作为参数在request时直接传入，也可以把每个键和值作为参数调用add_header()方法来添加。作为辨别浏览器身份的User-Agent header是经常被用来恶搞和伪装的，因为一些HTTP服务只允许某些请求来自常见的浏览器而不是脚本，或是针对不同的浏览器返回不同的版本。例如，Mozilla Firefox浏览器被识别为“Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11”。默认情况下，urlib2把自己识别为Python-urllib/x.y（这里的xy是python发行版的主要或次要的版本号，如在Python 2.6中，urllib2的默认用户代理字符串是“Python-urllib/2.6。下面的例子和上面的区别就是在请求时加了一个headers，模仿IE浏览器提交请求。
