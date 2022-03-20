import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


# jscode 中不要出现python的注释代码的,需要使用到的是json的注释方法
jscode = """
Java.perform(function () {
  console.log("coming")
  var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
  var onClick = MainActivity.onClick;
  onClick.implementation = function (v) {
    console.log("i am coming")
    this.onClick(v);
  };
  //要想产生对应的一直win的操作的话，需要重启服务器端执行操作即可的。
  var t1 = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity$1');
  t1.run.implementation=function(){
          this.this$0.value.m.value=1;
          this.this$0.value.n.value=2;
          this.run();
  };
  var Log = Java.use('android.util.Log');
  function stackTraceHere() {
    return Log.getStackTraceString(Exception.$new());
  }
});
"""
# 这种启动方式只能解决的是程序已经启动了,无法监控程序尚未启动过程中的一些问题的。
process = frida.get_usb_device(-1).attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
# 启动方式2 spawn 重启APP 可以hook APP启动阶段，会导致app闪崩的。这个存在闪崩的问题的。
#device = frida.get_usb_device(-1)
#pid = device.spawn(['com.example.seccon2015.rock_paper_scissors'])
#process = device.attach(pid)
#script = process.create_script(jscode)
#script.on('message', on_message)
#print('[*] Running')
#script.load()
#device.resume(pid)
#sys.stdin.read()
