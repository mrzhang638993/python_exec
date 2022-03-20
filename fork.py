# 尝试fork一个类下面的所有的方法
import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

#对应的frida的fork代码实现操作,python和frida混写出现的问题就是对应的代码出现错误不容易排查。
jscode = """
function hook_class(className){
     console.log("i am coming")
     var  content=Java.use(className)
     //使用反射获取到对应的class的所有的方法
     var methods=content.class.getDeclaredMethods()
     //使用反射操作调用对应的代码实现和操作管理
      methods.forEach(function(method){
              //对应的method是相关的函数的,
         //method中出现access$000这样的方法,可以测试的。对应的是在内部类中调用外部的方法的。
         var methodName=method.getName()
         //搜索所有重载的方式进行调用操作
         var overloads=content[methodName].overloads
         overloads.forEach(function(overload){
             //执行方法调用操作实现
                //argumentTypes对应的是frida的默认的参数的，可以获取得到对应的参数的
                var prot="("
                for(var j=0;j<overload.argumentTypes.length;j++){
                    prot+=overload.argumentTypes[j].className+","
                }
                prot +=")"
                var wMethodName=content+"."+methodName+prot
                console.log(wMethodName)
             //下面的操作对应的只有在方法调用触发的情况下，才会有对应的数据打印操作的。不触发是不会打印数据的
             overload.implementation=function(){
               //获取方法的调用关系以及对应的堆栈信息。
                printStacktrace()
                //arguments对应的是frida的一个隐藏的参数的,不需要额外的进行关注的。
                for (var i=0; i<arguments.length;i++){
                    console.log('argument:'+JSON.stringify(arguments[i]))
                }
                var ret=this[methodName].apply(this,arguments)
                console.log("ret:"+ret)
                return ret
             }
         }) 
      })
}
Java.perform(function () {
    hook_class('com.xbiao.utils.net.NetContent')
})
function printStacktrace(){
     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
}
"""
process = frida.get_usb_device(-1).attach('com.xbiao')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
