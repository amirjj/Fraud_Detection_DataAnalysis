// Dashboard 1 Morris-chart

Morris.Area({
    element: 'morris-area-chart',
    data: [{
        period: '2010',
        ERM: 10,
        FRM: 10,
        IA: 10
    }, {
        period: '2011',
        ERM: 10,
        FRM: 10,
        IA: 80
    }, {
        period: '2012',
        ERM: 0,
        FRM: 0,
        IA: 70
    }, {
        period: '2013',
        ERM: 70,
        FRM: 200,
        IA: 140
    }, {
        period: '2014',
        ERM: 180,
        FRM: 150,
        IA: 140
    }, {
        period: '2015',
        ERM: 105,
        FRM: 100,
        IA: 80
    },
        {
            period: '2016',
            ERM: 250,
            FRM: 150,
            IA: 200
        }],


    xkey: 'period',
    // ykeys: ['iphone', 'ipad', 'itouch'],
    ykeys: ['ERM', 'FRM', 'IA'],
    labels: ['ERM', 'FRM', 'IA'],
    pointSize: 3,
    fillOpacity: 0,
    pointStrokeColors: ['#00bfc7', '#fdc006', '#9675ce'],
    behaveLikeLine: true,
    gridLineColor: '#e0e0e0',
    lineWidth: 1,
    hideHover: 'auto',
    lineColors: ['#00bfc7', '#fdc006', '#9675ce'],
    resize: true

});

// Morris.Area({
//     element: 'morris-area-chart2',
//     data: [{
//         period: '2010',
//         SiteA: 0,
//         SiteB: 0,
//
//     }, {
//         period: '2011',
//         SiteA: 130,
//         SiteB: 100,
//
//     }, {
//         period: '2012',
//         SiteA: 80,
//         SiteB: 60,
//
//     }, {
//         period: '2013',
//         SiteA: 70,
//         SiteB: 200,
//
//     }, {
//         period: '2014',
//         SiteA: 180,
//         SiteB: 150,
//
//     }, {
//         period: '2015',
//         SiteA: 105,
//         SiteB: 90,
//
//     },
//         {
//             period: '2016',
//             SiteA: 250,
//             SiteB: 150,
//
//         }],
//     xkey: 'period',
//     ykeys: ['SiteA', 'SiteB'],
//     labels: ['Site A', 'Site B'],
//     pointSize: 0,
//     fillOpacity: 0.4,
//     pointStrokeColors: ['#b4becb', '#01c0c8'],
//     behaveLikeLine: true,
//     gridLineColor: '#e0e0e0',
//     lineWidth: 0,
//     smooth: false,
//     hideHover: 'auto',
//     lineColors: ['#b4becb', '#01c0c8'],
//     resize: true
//
// });


// LINE CHART
var line = new Morris.Line({
    element: 'morris-line-chart',
    resize: true,
    data: [
        {y: '2011 Q1', item1: 2666},
        {y: '2011 Q2', item1: 2778},
        {y: '2011 Q3', item1: 4912},
        {y: '2011 Q4', item1: 3767},
        {y: '2012 Q1', item1: 6810},
        {y: '2012 Q2', item1: 5670},
        {y: '2012 Q3', item1: 4820},
        {y: '2012 Q4', item1: 15073},
        {y: '2013 Q1', item1: 10687},
        {y: '2013 Q2', item1: 8432}
    ],
    xkey: 'y',
    ykeys: ['item1'],
    labels: ['Item 1'],
    gridLineColor: '#eef0f2',
    lineColors: ['#a3a4a9'],
    lineWidth: 1,
    hideHover: 'auto'
});
// Morris donut chart

Morris.Donut({
    element: 'morris-donut-chart',
    data: [{
        label: "Download Sales",
        value: 12,

    }, {
        label: "In-Store Sales",
        value: 30
    }, {
        label: "Mail-Order Sales",
        value: 20
    }],
    resize: true,
    colors: ['#99d683', '#13dafe', '#6164c1']
});

// Morris bar chart
Morris.Bar({
    element: 'morris-bar-chart',
    data: [{
        y: '2006',
        a: 100,
        b: 90,
        c: 60
    }, {
        y: '2007',
        a: 75,
        b: 65,
        c: 40
    }, {
        y: '2008',
        a: 50,
        b: 40,
        c: 30
    }, {
        y: '2009',
        a: 75,
        b: 65,
        c: 40
    }, {
        y: '2010',
        a: 50,
        b: 40,
        c: 30
    }, {
        y: '2011',
        a: 75,
        b: 65,
        c: 40
    }, {
        y: '2012',
        a: 100,
        b: 90,
        c: 40
    }],
    xkey: 'y',
    ykeys: ['a', 'b', 'c'],
    labels: ['A', 'B', 'C'],
    barColors: ['#b8edf0', '#b4c1d7', '#fcc9ba'],
    hideHover: 'auto',
    gridLineColor: '#eef0f2',
    resize: true
});
// Extra chart
// Morris.Area({
//     element: 'extra-area-chart',
//     data: [{
//         period: '2010',
//         ERM: 0,
//         FRM: 0,
//         IA: 0
//     }, {
//         period: '2011',
//         ERM: 50,
//         FRM: 15,
//         IA: 5
//     }, {
//         period: '2012',
//         ERM: 20,
//         FRM: 50,
//         IA: 65
//     }, {
//         period: '2013',
//         ERM: 60,
//         FRM: 12,
//         IA: 7
//     }, {
//         period: '2014',
//         ERM: 30,
//         FRM: 20,
//         IA: 120
//     }, {
//         period: '2015',
//         ERM: 25,
//         FRM: 80,
//         IA: 40
//     }, {
//         period: '2016',
//         ERM: 10,
//         FRM: 10,
//         IA: 10
//     }
//
//
//     ],
//     lineColors: ['#fb9678', '#01c0c8', '#8698b7'],
//     xkey: 'period',
//     ykeys: ['ERM', 'FRM', 'IA'],
//     labels: ['Site A', 'Site B', 'Site C'],
//     pointSize: 0,
//     lineWidth: 0,
//     resize: true,
//     fillOpacity: 0.8,
//     behaveLikeLine: true,
//     gridLineColor: '#e0e0e0',
//     hideHover: 'auto'
//
// });