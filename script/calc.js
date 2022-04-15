function calc(){
    var a = document.getElementsByTagName("input")[0].value;  //0번째 input
    var b = document.getElementsByTagName("input")[1].value;  //1번째 input
    var result = parseInt(a) + parseInt(b);
    document.getElementsByTagName("input")[2].value = result;
}