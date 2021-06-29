Morris.Area({
    element: 'morris-area-chart_for_mss_Location_check_tab',
    data: (function () {

        var request = new XMLHttpRequest();
        request.open("GET", 'get_mss_location_checks', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                var line = res[i];
                var username = line.split(",")[0];
                var count = parseInt(line.split(",")[1]);
                var threshold = 10;
                var len = i;
                var dictionary = {leng: len, msisdn: username,serial: count ,  count: count, threshold: threshold};
                arr.push(dictionary);

            }
        };

        request.send();
        console.log("Location Check API Called");

        console.log(arr);
        return arr;

    })(),
    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Count of Location Checks'],
    pointSize: 3,
    fillOpacity: 0,
    pointStrokeColors: ['#00bfc7', '#fdc006', '#9675ce'],
    behaveLikeLine: false,
    gridLineColor: '#e0e0e0',
    lineWidth: 1,
    hideHover: 'auto',
    lineColors: ['#00bfc7'],
    resize: true

});
