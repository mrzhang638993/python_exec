Java.perform(function () {
    var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
    var onClick = MainActivity.onClick;
    onClick.implementation = function (v) {
        console.log("i am coming")
        //stackTraceHere()
        onClick.call(this, v);
        this.m.value = 0;
        this.n.value = 1;
        this.cnt.value = 999;
        console.log("mmm==" + this.m.value)
        console.log("nnn==" + this.n.value)
        console.log("cnt==" + this.cnt.value)
        console.log('Done:' + JSON.stringify(this.cnt.value));
    };
    var TT = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity$1');
    TT.run.implementation = function () {
        this.this$0.value.m.value = 1
        this.this$0.value.n.value = 2
        console.log("i am coming")
        this.run()
    }
    var Log = Java.use('android.util.Log');

    function stackTraceHere() {
        return Log.getStackTraceString(Exception.$new());
    }
})

String.fromCharCode.apply(null, new Uint8Array(data
					.value))