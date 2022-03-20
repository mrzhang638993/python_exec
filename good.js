console.log("i am coming");
var Signature = Java.use("android.content.pm.Signature");
Signature.hashCode.implementation = function () {
    console.log(" i am coming soon");
    return this.hashCode();
}
Signature.toByteArray.implementation = function () {
    console.log("toByteArray");
    showStacks3(" toByteArray ");
    return this.toByteArray();
}

function showStacks3(str_tag) {
    var Exception = Java.use("java.lang.Exception");
    var ins = Exception.$new("Exception");
    var straces = ins.getStackTrace();
    if (undefined == straces || null == straces) {
        return;
    }
    console.log("=============================" + str_tag + " Stack strat=======================");
    console.log("");
    for (var i = 0; i < straces.length; i++) {
        var str = "   " + straces[i].toString();
        console.log(str);
    }
    console.log("");
    console.log("=============================" + str_tag + " Stack end=======================\r\n");
    Exception.$dispose();
)
}