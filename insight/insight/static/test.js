var num = 1;
var q = {
    1: {"title": "일과가 끝났다 나의 행동은?","type": "EI", "A": "집 가서 쉬어야지..", "B": "술먹자!"},
    2: {"title": "프로젝트 중 나의 직책은?","type": "EI", "A": "조장 or 발표자", "B": "자료조사 or PPT제작"},
    3: {"title": "개발 후 코드 리뷰 방법은?","type": "EI", "A": "다른사람들 앞에서 코드 리뷰", "B": "블로그에 공유하기"},
    4: {"title": "내가 더 자주 사용하는 말은?","type": "SN", "A": "아니..! 현실적으로 좀 생각해 봐", "B": "아니..! 상상을 좀 해봐"},
    5: {"title": "밸런스 게임을 하자고 했을 때 나의 생각은?","type": "SN", "A": "그런걸 왜 해?", "B": "히히히 재밌다!"},
    6: {"title": "시험이 다가오는데 공부가 손에 안잡힌다면?","type": "SN", "A": "내가 왜 공부를 해야하지?", "B": "지난 시험이 어떻게 나왔더라..?"},
    7: {"title": "팀원이 나한테 &quot그쪽이랑 저랑 잘 안맞네요&quot 라고 했을 때 드는 생각은?","type": "TF", "A": "흑흐흐흑..ㅠㅠ 내가 뭘 잘못했나..?", "B": "왜요?"},
    8: {"title": "슬픔을 둘로 나누면?","type": "TF", "A": "반이 된다.", "B": "아 스프스프!!"},
    9: {"title": "친구가 차 사고가 났다 이때 나의 반응은?","type": "TF", "A": "괜찮아..?", "B": "과실 몇대 몇이야?"},
    10: {"title": "나의 공부 방법은?","type": "JP", "A": "나는 나만의 정리 방법을 가지고 있다", "B": "친구들의 필기노트를 빌려서 공부한다"},
    11: {"title": "작업이 1주일 남았을 때 나의 행동은?","type": "JP", "A": "빨리 끝내자", "B": "술 마실 사람?"},
    12: {"title": "나의 여행계획 스타일은?","type": "JP", "A": "세부적인 계획까지 다 세워둔다", "B": "대략적인 코스만 짠다"}
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