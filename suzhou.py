import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function(){
  //console.log("coming soon")
  var Signature = Java.use('com.iCitySuzhou.suzhou001.d.d');
  Signature.a.overload('a.u$a').implementation=function(v){
     console.log("i am coming soon")
     return this.a(v)
  }
   printStacktrace();
   var aa = Java.use('com.hualong.framework.b.a');
   //新建一个StringBuffer对象，如果构造参数中有参数的话，new对象的话需要参数的
   var buffer=Java.use('java.lang.StringBuffer').$new();
   var  Integer=Java.use('java.lang.Integer');
   //只能调用公有的方法的
   var instance=Java.use('java.security.MessageDigest').getInstance("MD5");
   var param=Java.use('java.lang.String').$new("IMEI867980020108911-IMSI460NNNNNNNNNNNN&&1639051134&&f1190aca-d08e-4041-8666-29931cd89dde");
   instance.update(param.getBytes());
   var digest=instance.digest();
   for(var index in digest){
       var bytes=digest[index];
       console.log(bytes)
       //buffer.append(Integer.toString((bytes >>> 4) & 15, 16)).append(Integer.toString(bytes & 15, 16));
    }
    for(var i=0; i<digest.length;i++){
       var bytes=digest[i];
       console.log(bytes)
       buffer.append(Integer.toString((bytes >>> 4) & 15, 16)).append(Integer.toString(bytes & 15, 16));
    }
    console.log(buffer.toString());
    var  result=Java.use('java.lang.String').$new("418a4ebda2591ead2b694cc3061042d7");
    //使用js的==来比较字符串的相等的，不能使用java中的equals方法来比较相等操作的。
    console.log("equals=",buffer.toString()==result);
   aa.a.implementation=function(str){
      //打印输入的参数
      console.log(str)
      //获取返回值
      var content= this.a(str);
      console.log(content);
      return content
   }
   //自己使用fork代码来实现a方法的逻辑的
  function printStacktrace(){
     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
  }
})
"""
process = frida.get_usb_device(-1).attach('com.iCitySuzhou.suzhou001')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()