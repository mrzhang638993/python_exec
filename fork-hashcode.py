import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function(){
  var Signature = Java.use('android.content.pm.Signature');
  Signature.hashCode.implementation=function(){
     console.log(" i am coming soon")
     return this.hashCode()
  }
  //对应的存在toByteArray的fork机制的。但是无法查询到相关的信息，需要查看相关的调用堆栈信息的
  Signature.toByteArray.implementation=function(){
      console.log("toByteArray")
      printStacktrace()
      return this.toByteArray()
  }
  function printStacktrace(){
     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
  }
  var mainClass = Java.use('com.chaozhuo.texteditor.widget.a');
  mainClass.a.overload("android.content.Context").implementation=function(v){
    console.log(" coming a");
    //return this.a(v)
    return true;
  }
})
"""
device = frida.get_usb_device(-1)
pid = device.spawn('com.chaozhuo.texteditor')
process = device.attach(pid)
script = process.create_script(jscode)
script.on('message', on_message)
script.load()
device.resume(pid)
sys.stdin.read()
