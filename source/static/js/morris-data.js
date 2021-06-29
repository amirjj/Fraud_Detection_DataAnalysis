Morris.Area({
    element: 'morris-area-chart_for_mss_Location_check',
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

Morris.Area({
    element: 'morris-area-chart_for_usn_Location_check',
    data: (function () {

        var request = new XMLHttpRequest();
        request.open("GET", 'get_usn_location_checks', false);
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



Morris.Area({
    element: 'morris-area-chart',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'getvoucherused', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                var line = res[i];
                var msisdn = line.split(",")[0];
                var serial = line.split(",")[1];
                var count = parseInt(line.split(",")[2]);
                var threshold = 10;
                // var len = i.toString();
                var len = i;
                var dictionary = {leng: len, msisdn: msisdn, serial: serial, count: count, threshold: threshold};
                arr.push(dictionary);


            }


        };

        request.send();
        return arr;
    })(),

    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Days after sold date'],
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


Morris.Area({
    element: 'morris-area-chart_for_p2p',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'getp2p', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                var line = res[i];
                var msisdn = line.split(",")[0];
                var count = parseInt(line.split(",")[1]);
                var amount = line.split(",")[2];
                var threshold = 10;
                var len = i;
                var dictionary = {leng: len, msisdn: msisdn, count: count, serial: amount, threshold: threshold};
                arr.push(dictionary);

            }
        };

        request.send();
        return arr;

    })(),


    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Count of p2p transfer'],
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



Morris.Area({
    element: 'morris-area-chart_simc',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'simc', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                // console.log(res[i]);
                var line = res[i];
                var msisdn = line.split(",")[0];
                var count = parseInt(line.split(",")[4]);
                var amount = line.split(",")[3];

                var threshold = 10;
                var len = i;
                var dictionary = {leng: len, msisdn: msisdn, count: count, serial: amount, threshold: threshold};
                arr.push(dictionary);

            }


        };

        request.send();

        return arr;

    })(),


    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Dif of SIMC and activ. date'],
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


Morris.Area({
    element: 'morris-area-chart_reg_per_day',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'regperday', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                // console.log(res[i]);
                var line = res[i];
                var msisdn = line.split(",")[0];
                var count = parseInt(line.split(",")[1]);
                var amount = line.split(",")[1];
                // console.log(count);
                var threshold = 10;
                var len = i;
                var dictionary = {leng: len, msisdn: msisdn, count: count, serial: amount, threshold: threshold};
                arr.push(dictionary);

            }
        };

        request.send();

        return arr;

    })(),


    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Count of Registeration: '],
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




Morris.Area({
    element: 'morris-area-chart_cow_per_dealer',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'cowperday', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                // console.log(res[i]);
                var line = res[i];
                var msisdn = line.split(",")[0];
                var count = parseInt(line.split(",")[1]);
                var amount = line.split(",")[1];
                // console.log(count);
                var threshold = 10;
                var len = i;
                var dictionary = {leng: len, msisdn: msisdn, count: count, serial: amount, threshold: threshold};
                arr.push(dictionary);

            }
        };

        request.send();

        return arr;

    })(),


    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Count of Registeration: '],
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



Morris.Area({
    element: 'morris-area-chart_location_based_registration',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'location_based_reg', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                var line = res[i];
                var msisdn = line.split(",")[0];
                var count = parseInt(line.split(",")[1]);
                var amount = line.split(",")[1];
                var threshold = 10;
                var len = i;
                var dictionary = {leng: len, msisdn: msisdn, count: count, serial: amount, threshold: threshold};
                arr.push(dictionary);

            }
        };

        request.send();

        return arr;

    })(),


    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['% of registerations out of dealer location: '],
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



Morris.Area({
    element: 'morris-area-invoice',
    data: (function () {
        var request = new XMLHttpRequest();
        request.open("GET", 'invoice_rep', false);
        var arr = [];

        request.onload = function () {
            var res = request.response;
            res = res.split('\n');
            for (var i = 0; i < res.length - 1; i++) {
                // console.log(res[i]);
                var line = res[i];
                var supplier = line.split(",")[0];
                var count = parseInt(line.split(",")[2]);
                var amount = line.split(",")[1];

                var threshold = 10;
                var len = i;
                // var dictionary = {leng: len, supplier: supplier, count: count, amount: amount, threshold: threshold};

                var dictionary = {leng: len, msisdn: supplier, count: count, serial: amount, threshold: threshold};

                arr.push(dictionary);

            }


        };

        request.send();

        return arr;

    })(),


    // xkey: 'period',
    xkey: 'leng',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['count'],
    labels: ['Count of PO'],
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
