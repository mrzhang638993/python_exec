function main() {
    console.log("i am coming");
    Java.perform(function () {
        console.log("i am 1");
        var Signature = Java.use('android.content.pm.Signature');
        Signature.hashCode.implementation = function () {
            console.log(" i am coming soon")
            return this.hashCode()
        }
        Signature.toByteArray.implementation = function () {
            console.log("toByteArray")
            return this.toByteArray()
        }
    })
}
setImmediate(main);