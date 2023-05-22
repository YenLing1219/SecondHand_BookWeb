function alert_box(alert_message){
    var button = document.querySelector('.popuptest');
    var showtxt = document.querySelector('.show');

    function popup2(e) {
        window.alert(alert_message);
        parent.window.history.go(-1);

    };
    button.addEventListener('click', popup2);
}
