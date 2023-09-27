var num = 1;
var q = {
    1: {"title": "1번 문제","type": "EI", "A": "dksldfkadflaknvslaknv", "B": "dlkanflkasnvlsanvlk"},
    2: {"title": "2번 문제","type": "EI", "A": "대답 E", "B": "대답 I"},
    3: {"title": "3번 문제","type": "EI", "A": "대답 E", "B": "대답 I"},
    4: {"title": "4번 문제","type": "SN", "A": "대답 S", "B": "대답 N"},
    5: {"title": "5번 문제","type": "SN", "A": "대답 S", "B": "대답 N"},
    6: {"title": "6번 문제","type": "SN", "A": "대답 S", "B": "대답 N"},
    7: {"title": "7번 문제","type": "TF", "A": "대답 T", "B": "대답 F"},
    8: {"title": "8번 문제","type": "TF", "A": "대답 T", "B": "대답 F"},
    9: {"title": "9번 문제","type": "TF", "A": "대답 T", "B": "대답 F"},
    10: {"title": "10번 문제","type": "JP", "A": "대답 J", "B": "대답 P"},
    11: {"title": "11번 문제","type": "JP", "A": "대답 J", "B": "대답 P"},
    12: {"title": "12번 문제","type": "JP", "A": "대답 J", "B": "대답 P"}
}

function start() {
    $(".start").hide();
    $(".question").show();
    next();
}

$("#A").click(function () {
    var type = $("#type").val();
    var preValue = $("#" + type).val();
    $("#" + type).val(parseInt(preValue) + 1);
    next();
});
$("#B").click(function () {
    next();
});

function next() {
    if (num == 13){
        var mbti = "";
        ($("#EI"). val() < 2) ? mbti += "I" : mbti += "E";
        ($("#SN"). val() < 2) ? mbti += "N" : mbti += "S";
        ($("#TF"). val() < 2) ? mbti += "F" : mbti += "T";
        ($("#JP"). val() < 2) ? mbti += "P" : mbti += "J";

        window.location.href = "./" + mbti;
    }else {
        $(".q-num").html("Q" + num);
        $(".progress-txt").html(num + ' / 12');
        $(".progress-bar").attr('style', 'width: calc(100/12*' + num + '%)');
        $("#title").html(q[num]["title"]);
        $("#type").val(q[num]["type"]);
        $("#A").html(q[num]["A"]);
        $("#B").html(q[num]["B"]);
        num++;
    }
}