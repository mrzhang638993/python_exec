import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

test_sigx = '''
Java.perform(
    function(){
        console.log('i am enter')

        var EE = Java.use('com.picovr.assistantphone.c.a.e')
        EE.d.overload('java.lang.String', 'java.lang.String').implementation = function(p1,p2){
            console.log('p1:'+p1)
            console.log('p2:'+p2)
            return this.d(p1,p2)
        }
        
        EE.a.overload('java.util.Map').implementation = function(p1){
            console.log('p1:'+p1)

            var ret =  this.a(p1)

            console.log('bbb1:'+ret)
            console.log(JSON.stringify(ret))
            console.log(ret.$className)

          
            var HashMap = Java.use('java.util.HashMap')
            var newret = Java.cast(ret, HashMap)
            printMap(newret)
            return ret
        }


        var D = Java.use('com.blankj.utilcode.util.D')
        D.d.overload('java.lang.String').implementation = function(p1){
            console.log('p1:'+p1)
            return this.d(p1)
        }

        /*var secureRandom = Java.use('java.security.SecureRandom').$new()
        var stringBuffer = Java.use('java.lang.StringBuffer').$new()
        //var i3 = 0;
        for (var i3 = 0; i3 < 10; i3++){
            var ran = secureRandom.nextInt(10)
            console.log('ran:'+ran)
            stringBuffer.append(ran)
        }
        console.log('ret:'+stringBuffer)*/

        var AA = Java.use('com.picovr.assistantphone.c.a.a')
        AA.b.implementation = function(p1){
            console.log('xxx pp:'+p1)
            var ret =  AA.b(p1)

            console.log(JSON.stringify(ret))
            console.log('bb:'+ret)

            var pwd = Java.use("java.lang.String").$new(ret);
            console.log('vvwd:'+pwd)
            return ret
        }

        function printMap(param){
            var keys = param.keySet();
            var iterator = keys.iterator();
            while (iterator.hasNext()) {
                var k = iterator.next();
                console.log(k + " : " + param.get(k));
            }
        }

        var pwd = Java.use("java.lang.String").$new('password=iloveyou&salt=3103305672');

        console.log(pwd.getBytes())
        var byt = pwd.getBytes()
        var newpwd = Java.use("java.lang.String").$new(byt);
        console.log(newpwd)

    }
)
'''



test_sig = '''
Java.perform(
    function(){
        console.log('11 enter hook')
        var SortedMap = Java.use('java.util.SortedMap')
        var TreeMap = Java.use('java.util.TreeMap')
        
        var PublicKey = Java.use('java.security.PublicKey')

        
        var DK = Java.use('com.picovr.assistantphone.c.a.d')
        DK.b.overload('java.lang.String').implementation = function(p) {
            console.log('eeee')
            var ret =  DK.b(p)
            //var args = Java.cast(ret, PublicKey)
            //console.log('getEncoded:'+ret.getEncoded())
            return ret
        }

        var DD = Java.use('com.blankj.utilcode.util.D')
        DD.d.overload('java.lang.String').implementation = function(p) {
            console.log('method d before sign:'+p)
            var ret =  DD.d(p)
            console.log('method d real sign:'+ret)
            return ret
        }

        var secureRandom = Java.use('java.security.SecureRandom').$new()
        console.log(secureRandom.nextInt(10))
        
        var EE = Java.use('com.picovr.assistantphone.c.a.e')
        EE.a.overload('java.util.SortedMap').implementation = function(p) {
            console.log('print map:'+p.$className)
            var args = Java.cast(p, TreeMap)
            printMap(args)
            console.log('method d ori sign:'+args.toString())     
            var ret = this.a(p)
            console.log('sss:'+ret)
            return ret
        }
        
        EE.e.overload('java.lang.String').implementation = function(p) {
            var a = "cQ5jDgHn1mT6OxsGiClx2zskVXbATwc574GcaKMJN8YB8+zLjWnpoKLSNeb4AdkY3PQGk52ByIquo9RV4totBDPazxCQF6pjf9diMY00/GUxCsDAUcYr6nN6KP0q9cFoq0eYGxCVNks2h6ROWRvFmZlKSrXe3evD8Ofx2h35+rI=";
            return a;
        }

        EE.d.overload('java.lang.String').implementation = function(p) {
            console.log('EE d p:'+p)
            var ret = this.d(p)
            console.log('EE d ret:'+ret)
            return ret
        }
        var AA = Java.use('com.picovr.assistantphone.c.a.a')

        AA.b.implementation = function(p) {
            console.log("AA b")
            var ret = this.b(p)

            var javaString = Java.use('java.lang.String');
            console.log(javaString.$new(ret))

            console.log('json:'+JSON.stringify(ret))

            var ByteString = Java.use("com.android.okhttp.okio.ByteString");
            console.log('hex:'+ByteString.of(ret).hex());

            return ret
        }
        /*AA.a.implementation = function(p) {
            console.log(''+JSON.stringify(ret))
            var ret =  this.a(p)
            console.log('ret enc:'+ret)
            return ret
        }*/

        function printstack() {
            console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new()))
        }

        function printMap(param){
            console.log('fffffffff')
            var keys = param.keySet();
            var iterator = keys.iterator();
            while (iterator.hasNext()) {
                var k = iterator.next();
                console.log(k + " : " + param.get(k));
            }
            console.log('vvvvvvvvvv')
        }

        function printstring(ret) {
            var buffer = Java.array('byte', ret)

            var javaString = Java.use('java.lang.String');
            console.log(javaString.$new(buffer))
        }
    }
)

'''



test_rpcx = '''
rpc.exports = {
 geta: function(str){//PS: 函数名不要大写
    var enc = '' 
    Java.perform(function () {
        console.log('str:'+str)
        var e = Java.use('com.picovr.assistantphone.c.a.e')
        enc = e.d(str)
        console.log('enc:'+enc)
    });
    return enc
 }
}
'''

test_enc = '''
Java.perform(
    function(){
        var KeyFactory = Java.use('java.security.KeyFactory')
        var X509EncodedKeySpec = Java.use('java.security.spec.X509EncodedKeySpec')
        
        var Constants = Java.use('com.picovr.assistantphone.c.a.b')

        var Base64Utils = Java.use('com.picovr.assistantphone.c.a.a')
        var PublicKey = KeyFactory.getInstance("RSA").generatePublic(X509EncodedKeySpec.$new(Base64Utils.a(Constants.p.value)))

        console.log(PublicKey.class)
        console.log(PublicKey.class.getMethods())
        //var p = Java.use("java.lang.String").$new("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDDZ2bnVXHfDEJnTic8//BK3Bkm"+"\\r"+"2DnraCvnknXdqd+84ZYtRhYA/+MsQWv1k6qH6aR1yXagtnGVZeoO3722fWDtIQFK"+"\\r"+"egY2LZuADRONNNJC75+WTaHuQfXULXynMGwkkhtXCt0HrGtOVpJ1jP60HrJ4qVYa"+"\\r"+"lM+8svZbYNYLqfOsHwIDAQAB")
        //console.log(p)
        //var str = 'password=iloveyou&salt=5711344821'
        //var EE = Java.use('com.picovr.assistantphone.c.a.e')
        //var AA = Java.use('com.picovr.assistantphone.c.a.a')
        /*var BB = Java.use('com.picovr.assistantphone.c.a.b')
        console.log(BB.p.value)
        console.log('pubkey:'+JSON.stringify(AA.a(BB.p.value)))
        var ByteString = Java.use("com.android.okhttp.okio.ByteString");
        console.log('hex:'+ByteString.of(AA.a(BB.p.value)).hex());

        AA.b.overload('java.lang.String').implementation = function(p) {
            console.log('ddd')
            return this.b(p)
        }
        AA.a.overload('[B').implementation = function(p) {
            console.log('ppp')
            return AA.a(p)
        }*/
        //var ret = EE.d(str)
        //var ss = Java.use('java.lang.String').$new(str)
        //var ret = AA.a(ss.getBytes())
        //console.log('ret:'+ret)
})
'''

test_rpc='''
rpc.exports = { 
    testfunc: function(qq){//PS: 函数名不要大写
        var enc = ''    
        Java.perform(function () {
            console.log('eeeeee');
            var pwd = Java.use("java.lang.String").$new('password=iloveyou&salt=3103305672');
            //console.log(JSON.stringify(pwd.getBytes()))
            var public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCfeke6QsD7GSeu3r+S0fghY4S93CQwq7GQSwx/mf+7bCL0XPweIFKAKYtZ6hXqRxmjmDJbZSl4imWVYZM3dNCbf4kDcthvlhEzR/Jcr/yHi5W1tL+yqBdnnAfcGkMT9tdZl/1sYB+aOMIP4tw07y53zFWtXszz/wCrA/jHopXHNQIDAQAB";

            var a = Java.use("com.picovr.assistantphone.c.a.a");
            var d = Java.use("com.picovr.assistantphone.c.a.d");
            enc = a.a(d.a(pwd.getBytes(), d.b(public_key)))

            //
            var e = Java.use("com.picovr.assistantphone.c.a.e");
            //console.log(JSON.stringify(pwd.getBytes()))
            //enc = e.d(pwd)
            /*var a = Java.use("com.picovr.assistantphone.c.a.a");
            var d = Java.use("com.picovr.assistantphone.c.a.d");
            var KeyFactory = Java.use("java.security.KeyFactory");
            var X509EncodedKeySpec = Java.use("java.security.spec.X509EncodedKeySpec");
            console.log('gggggggggggg');
            var pubkey = Java.use("java.lang.String").$new(pubkey);
            console.log('mmmmmmmm');
            var publickey = KeyFactory.getInstance("RSA").generatePublic(X509EncodedKeySpec.$new(pubkey.getbytes()))

            enc = a.a(d.a(pwd.getBytes(), publickey))*/

/*
            var pubk = d.b(pubkey);
            console.log('rrrr');
            var enc_byte = d.a(pwd.getBytes(), pubk)
            console.log('gggggggg');
            var Base64 = Java.use("java.util.Base64");
            console.log('yyyyyy');
            enc = Base64.getEncoder().encodeToString(enc_byte)
*/

            //enc = a.a(enc_byte);
            console.log('enc11:'+enc);
        });
        return enc
    }
}
'''

#两种启动方式

#启动方式1


def start_rpc():
    process = frida.get_usb_device(-1).attach('com.picovr.assistantphone')
    script = process.create_script(test_sigx)
    script.on('message', on_message)
    script.load()
    #return script.exports
    #script.exports.gett('IMEI867979020991839-IMSI460NNNNNNNNNNNN&&1629536144&&f1190aca-d08e-4041-8666-29931cd89dde')
    sys.stdin.read()


#启动方式2 spawn 重启APP 可以hook APP启动阶段
# device = frida.get_usb_device(-1)
# pid = device.spawn(['com.iCitySuzhou.suzhou001'])
# process = device.attach(pid)

# script = process.create_script(test_context)
# script.on('message', on_message)
# print('[*] Running')
# script.load()
# device.resume(pid)
# sys.stdin.read()
start_rpc()