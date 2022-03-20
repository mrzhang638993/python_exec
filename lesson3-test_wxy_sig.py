import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


test_sig = '''

Java.perform(
    function(){
        var Signature = Java.use('android.content.pm.Signature')
        Signature.hashCode.implementation = function() {
            console.log('hashCode')
            return this.hashCode()
        }

        Signature.toByteArray.implementation = function() {
            console.log('toByteArray')
            printstack()
            return this.toByteArray()
        }

        function printstack() {
            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()));
        }

        var AA = Java.use('com.chaozhuo.texteditor.widget.a')
        AA.a.overload('android.content.Context').implementation = function() {
            return true
            //this.a()
        }
    }
)

'''


test_context = '''
Java.perform(
    function(){
        var currentApplication = Java.use('android.app.ActivityThread').currentApplication()
        var context = currentApplication.getApplicationContext()

        console.log(context.getPackageName())

        console.log(context.getPackageManager().getPackageInfo(context.getPackageName(), 64).signatures.value[0].toByteArray())

        send(context.getPackageManager().getPackageInfo(context.getPackageName(), 64).signatures.value[0].toByteArray())

        console.log(context.getPackageManager().getPackageInfo(context.getPackageName(), 64).signatures.value[0].hashCode())
    }
)
'''


#两种启动方式

#启动方式1


# process = frida.get_usb_device(-1).attach('com.chaozhuo.texteditor')
# script = process.create_script(test_context)
# script.on('message', on_message)
# script.load()
# sys.stdin.read()


#启动方式2 spawn 重启APP 可以hook APP启动阶段
device = frida.get_usb_device(-1)
pid = device.spawn(['com.chaozhuo.texteditor'])
process = device.attach(pid)

script = process.create_script(test_context)
script.on('message', on_message)
print('[*] Running')
script.load()
device.resume(pid)
sys.stdin.read()
