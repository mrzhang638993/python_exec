import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

#apiaccount=vrpuc-aaf91f835147ce2d01216bd3bd5c3516&phone=13392112455&sign=4B2BCF6F288ABB69EB003A6E4D471E81&enc=F9lNsQu4l45K2fVPNpQ/vc1UdRnyx1jPevFYSxC7y6TcIfEZpOzqERspAlu1AH6+ChG4svL83tIivgQ3TVDp2YGvg9RyWpNBKA1TDKFuqWetswwPbipiZ5ErkzFwqBIHdFQNM3YoewLr1Z//QE58B57WEJvZHI3SfRNmrG150kE=&timestamp=1639220616511&key=a0f723c011346j39w049d7bf0356b34b
jscode = """
Java.perform(function(){
  //存在一个问题,遇到对应的object的话,我们应该怎么打印出来相关的对象信息了？
  printStacktrace()
  var aa=Java.use('com.picovr.assistantphone.c.a.a');
  aa.b.implementation=function(p){
     console.log("input param "+p)
     var result=this.b(p)
     //方式1：使用JSON.stringfy,其中JSON是js模块自身含有的。默认的是无法打印出来的。
     //打印出来的是字节码的数据信息的。
     console.log("output  result "+JSON.stringify(result))
     //对于字节数组中包含了相关的不可见的字符的话，会出现这些问题的。输出的字符串还有不可见的内容的话，只能使用字节的方式来实现操作的。
     //需要一个个的不断地比对字节的信息从而来判断和获取相关的信息的。字符串存在不可见的话,对应的就是无法打印出来的内容的。
     var origin=Java.use('java.lang.String').$new(result,'iso8859-1')
     console.log("origin result is "+origin)
     return result
  }
  //console.log("coming soon")
  var sign = Java.use('com.picovr.assistantphone.c.a.e');
    //获取enc的入参以及出参的参数情况
  /**
  sign.e.overload('java.lang.String').implementation=function(p){
     console.log(p)
     var result=this.e(p)
     console.log(result)
     return result
  }
  */
  /**
  sign.d.overload('java.lang.String').implementation=function(p){
      console.log("enc 入参=",p)
      var result=this.d(p)
      console.log(result)
      return result
  }
  */
  //问题:怎么实现python代码主动的调用按照的代码,直接使用安卓的代码从而避免书写复杂的代码逻辑
  //获取得到pubickey的数据信息
  var key = Java.use('com.picovr.assistantphone.c.a.d')
  /**key.b.overload('java.lang.String').implementation=function(p){
    console.log("key=",p)
    var result=this.b(p)
    var public_key = Java.use('java.security.PublicKey')
    var newret = Java.cast(result, public_key)
    console.log("public key data=",newret)
    return result;
  }*/
  //开始fork相关的代码和机制信息
  /**
  var aa=Java.use('com.picovr.assistantphone.c.a.a')
  var ByteString = Java.use("com.android.okhttp.okio.ByteString");
  aa.b.implementation=function(p){
     console.log("input="+p)
     var result=this.b(p)
     //怎么将byte数组转化成为字符串进行操作,对应的字符串是iso8859-1的字符串信息的。
     console.log("com.ss.sys.ces.a => result string:" + ByteString.of(result).hex() );
     return result
  }
  */
  function byteToString(arr) {  
    if(typeof arr === 'string') {  
        return arr;  
    }  
    var str = '',  
        _arr = arr;  
    for(var i = 0; i < _arr.length; i++) {  
        var one = _arr[i].toString(2),  
            v = one.match(/^1+?(?=0)/);  
        if(v && one.length == 8) {  
            var bytesLength = v[0].length;  
            var store = _arr[i].toString(2).slice(7 - bytesLength);  
            for(var st = 1; st < bytesLength; st++) {  
                store += _arr[st + i].toString(2).slice(2);  
            }  
            str += String.fromCharCode(parseInt(store, 2));  
            i += bytesLength - 1;  
        } else {  
            str += String.fromCharCode(_arr[i]);  
        }  
    }  
    return str;  
}  
 /**
  sign.d.overload('java.lang.String', 'java.lang.String').implementation=function(p,v){
     //打印入参信息
     console.log("p="+p);
     console.log("v="+v);
     printStacktrace();
     return this.d(p,v)
  }
  */
  //加载获取sign的数据信息
  /**
  sign.a.overload('java.util.Map').implementation=function(p){
     console.log("入参是=",printMap(p))
     var signs=this.a(p);
     var HashMap = Java.use('java.util.HashMap')
     var newret = Java.cast(signs, HashMap)
     console.log("出参是=",printMap(newret))
     return signs;
  }*/
  /**
  sign.a.overload('java.util.SortedMap').implementation=function(p){
      console.log("入参1类型是=",p.$className)
      var HashMap = Java.use('java.util.TreeMap')
      var newret = Java.cast(p, HashMap)
      console.log("入参1是=",newret)
      var result=this.a(p)
      console.log("出参1是="+result)
      return result
  }
  */
  var dd=Java.use('com.picovr.assistantphone.c.a.d')
  //怎么获取publickey的数据信息的。
  /**dd.b.overload('java.lang.String').implementation=function(p){
     console.log(p)
     var content=this.b(p)
     console.log(content)
     return content
  }*/
  //获取用于加密的数据信息。
  function printMap(param){
     var content=""
     var keys = param.keySet();
     var iterator = keys.iterator();
     while (iterator.hasNext()) {
         var k = iterator.next();
         content+=k + "=" + param.get(k)+"&";
     }
    content+="key=a0f723c011346j39w049d7bf0356b34b"
    return content;
  }
  /**
  这种方式对应的是被动的调用的,可以主动的进行调用操作的。sign.a(10)，对应的是静态方法调用的
  调用无参数的构造方法的，有参数的构造方法还需要对应的构造参数的。
  成员方法的调用,需要使用到new执行操作的。Java.use('com.picovr.assistantphone.c.a.e').$new()
  */
  /**
  sign.a.overload('int').implementation=function(val){
    var random=this.a(val);
    console.log(random);
    return random;
  }*/
  //对应的也是可以直接使用java的相关的机制完成对应的实现操作和管理实现的。
  /**var secure=Java.use('java.security.SecureRandom').$new();
  var buffer=Java.use('java.lang.StringBuffer').$new();
  for(var  i=0;i<10;i++){
    var num=secure.nextInt(10)
    console.log(num)
    buffer.append(num);
  }*/
  //3.07.00.01.00.01.06.08.02.01.0对应的数据不符合预期的。可以想办法解决这种问题的。
  //console.log(buffer.toString());
  //使用python代码实现相关的fork机制的。
  function printStacktrace(){
     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
  }
  //获取一个登录的随机数数值
})
"""

rpcx="""
rpc.exports = {
    testfunc: function(str){
        var enc = ''
        Java.perform(function () {
            var a = Java.use("com.picovr.assistantphone.c.a.e");
            enc = a.d(str)
        });
        return enc
    }
}
"""
def start_rpc():
    process = frida.get_usb_device(-1).attach('com.picovr.assistantphone')
    #script = process.create_script(rpcx)
    script = process.create_script(jscode)
    script.on('message', on_message)
    print('[*] Running CTF')
    script.load()
    #return script.exports
    sys.stdin.read()
#直接调用函数
start_rpc()