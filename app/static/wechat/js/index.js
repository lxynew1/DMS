$(document).ready(function () {
    $.ajax({
        url: "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5", //请求的服务端地址
        type: "post",
        dataType: "JSONP",
        success: function (data) {
            var tojson = $.parseJSON(data.data);
            console.log(tojson);


            $("#nowtime").html(tojson.lastUpdateTime); //时间
            $(".num1").html(tojson.chinaTotal.confirm); //确诊病例
            $(".add_num1").html(tojson.chinaAdd.confirm); //新增确诊病例
            $(".num2").html(tojson.chinaTotal.suspect); //疑似病例
            $(".add_num2").html(tojson.chinaAdd.suspect); //新增疑似病例
            $(".num3").html(tojson.chinaTotal.dead); //死亡人数
            $(".add_num3").html(tojson.chinaAdd.dead); //新增死亡人数
            $(".num4").html(tojson.chinaTotal.heal); //治愈人数
            $(".add_num4").html(tojson.chinaAdd.heal); //新增治愈人数

            var chinaData = tojson.areaTree[0].children;

            // 地图
            var map_echarts = echarts.init(document.getElementById('map_echarts'));
            var dataList = [];

            for (var j = 0; j < chinaData.length; j++) {
                var jsonobj = {};
                jsonobj.name = chinaData[j].name;
                jsonobj.value = chinaData[j].total.confirm;
                dataList.push(jsonobj);
            }
            var nhbd = {
                name: '南海半岛',
                value: 0
            };
            dataList.push(nhbd);
            var map_option = {
                tooltip: {
                    triggerOn: "click",
                    formatter: function (e, t, n) {
                        return .5 == e.value ? e.name + "：有疑似病例" : e.seriesName + "<br />" + e.name + "：" + e.value
                    }
                },
                visualMap: {
                    min: 0,
                    max: 100000,
                    left: 10,
                    bottom: 40,
                    itemWidth: 5, //图元的宽
                    itemHeight: 5, //图元的高
                    itemGap: 5, //两个图元之间的间隔距离
                    textStyle: {
                        fontSize: 9, //图元字体大小
                    },
                    pieces: [{
                        gt: 1000,
                        label: "> 1000",
                        color: "#7f1100"
                    }, {
                        gte: 500,
                        lte: 1000,
                        label: "500 - 1000",
                        color: "#ff5428"
                    }, {
                        gte: 150,
                        lt: 500,
                        label: "150 - 500",
                        color: "#ff8c71"
                    }, {
                        gt: 20,
                        lt: 150,
                        label: "20 - 150",
                        color: "#ffd768"
                    }, {
                        gt: 0,
                        lt: 20,
                        label: "0 - 20",
                        color: "rgb(253,235,207)"
                    }],
                    show: true
                },
                geo: {
                    map: "china",
                    roam: !1, //是否开启鼠标缩放和平移漫游
                    scaleLimit: { //滚轮缩放的极限控制
                        min: 1,
                        max: 2
                    },
                    zoom: 1.2, //当前视角的缩放比例。
                    top: 40,
                    label: {
                        show: !0,
                        fontSize: "7", //地图上文字的大小
                        color: "rgba(0,0,0,0.7)", //文字的颜色
                        position: ['0', '50%'],
                        align: "center",
                        verticalAlign: "middle",
                        distance: '2'
                    },
                    itemStyle: {
                        normal: {
                            //shadowBlur: 50,
                            //shadowColor: 'rgba(0, 0, 0, 0.2)',
                            borderColor: "rgba(0, 0, 0, 0.2)"
                        },
                        emphasis: {
                            areaColor: "#f2d5ad",
                            shadowOffsetX: 0,
                            shadowOffsetY: 0,
                            borderWidth: 0
                        }
                    }
                },
                series: [{
                    name: "确诊病例",
                    type: 'map',
                    mapType: 'china',
                    geoIndex: 0,
                    data: dataList
                }]
            };
            map_echarts.setOption(map_option);


            // 全国疫情新增确诊/新增疑似趋势图
            var addData10 = tojson.chinaDayAddList;
            var xData10 = [];
            var yData11 = [];
            var yData12 = [];
            for (var j = 0; j < addData10.length; j++) {
                xData10.push(addData10[j].date);
                yData11.push(addData10[j].confirm);
                yData12.push(addData10[j].suspect);
            }
            var echarts1 = echarts.init(document.getElementById('echarts1'));
            var echarts1_option = {
                title: {
                    top: '0',
                    left: 'left',
                    text: '全国疫情新增确诊/新增疑似趋势图',
                    textStyle: {
                        align: 'left',
                        color: '#000',
                        fontWeight: '500',
                        fontSize: 13,
                    }
                },
                backgroundColor: '#fff',
                legend: {
                    right: '0',
                    top: '20px',
                    itemWidth: 10,
                    itemHeight: 5,
                    itemGap: 15,
                    textStyle: {
                        color: '#333',
                        fontSize: 10,
                    },
                    icon: 'roundRect',
                    data: ['新增确诊', '新增疑似']
                },
                grid: {
                    right: '0',
                    bottom: '0',
                    left: '0',
                    top: '50px',
                    containLabel: true
                },
                xAxis: [{
                    type: 'category',
                    data: xData10,
                    axisLine: { //坐标轴轴线相关设置
                        lineStyle: {
                            color: "#aaa"
                        }
                    },
                    axisTick: { //坐标轴刻度相关设置
                        show: true,
                        lineStyle: {
                            color: '#aaa',
                            width: 1,
                        },
                        length: 3,
                    },
                    axisLabel: { //坐标轴刻度标签的相关设置
                        show: true,
                        // interval:1,
                        textStyle: {
                            color: "#aaa",
                            fontSize: 9,
                        },
                        rotate: 30
                    }
                }],
                yAxis: [{
                    type: 'value',
                    position: 'left',
                    interval: 1000,
                    max: 6000,
                    axisLine: { //坐标轴轴线相关设置
                        show: false
                    },
                    axisTick: { //坐标轴刻度相关设置
                        show: false
                    },
                    axisLabel: { //坐标轴刻度标签的相关设置
                        show: true,
                        color: "#aaa",
                        fontSize: 9

                    },
                    splitLine: { //坐标轴在 grid 区域中的分隔线
                        lineStyle: {
                            color: "#eee",
                        }
                    }
                }, ],
                series: [{
                        name: '新增确诊',
                        type: 'line',
                        yAxisIndex: 0,
                        symbolSize: 4,
                        itemStyle: {
                            normal: {
                                color: 'rgb(255,215,104)',
                            }
                        },
                        data: yData11
                    },
                    {
                        name: '新增疑似',
                        type: 'line',
                        yAxisIndex: 0,
                        symbolSize: 4,
                        itemStyle: {
                            normal: {
                                color: 'rgb(127,17,0)',
                            }
                        },
                        data: yData12
                    }

                ]
            };
            echarts1.setOption(echarts1_option);

            // 全国疫情累计确诊/疑似趋势图
            var addData20 = tojson.chinaDayList;
            var xData20 = [];
            var yData21 = [];
            var yData22 = [];
            for (var k = 0; k < addData20.length; k++) {
                xData20.push(addData20[k].date);
                yData21.push(addData20[k].confirm);
                yData22.push(addData20[k].suspect);
            }
            var echarts2 = echarts.init(document.getElementById('echarts2'));
            var echarts2_option = {
                title: {
                    top: '0',
                    left: 'left',
                    text: '全国疫情累计确诊/疑似趋势图',
                    textStyle: {
                        align: 'left',
                        color: '#000',
                        fontWeight: '500',
                        fontSize: 13,
                    }
                },
                backgroundColor: '#fff',
                legend: {
                    right: '0',
                    top: '20px',
                    itemWidth: 10,
                    itemHeight: 5,
                    itemGap: 15,
                    textStyle: {
                        color: '#333',
                        fontSize: 10,
                    },
                    icon: 'roundRect',
                    data: ['累计确诊', '累计疑似']
                },
                grid: {
                    right: '0',
                    bottom: '0',
                    left: '0',
                    top: '50px',
                    containLabel: true
                },
                xAxis: [{
                    type: 'category',
                    data: xData20,
                    axisLine: { //坐标轴轴线相关设置
                        lineStyle: {
                            color: "#aaa"
                        }
                    },
                    axisTick: { //坐标轴刻度相关设置
                        show: true,
                        lineStyle: {
                            color: '#aaa',
                            width: 1,
                        },
                        length: 3,
                    },
                    axisLabel: { //坐标轴刻度标签的相关设置
                        show: true,
                        // interval:1,
                        textStyle: {
                            color: "#aaa",
                            fontSize: 9,
                        },
                        rotate: 30
                    }
                }],
                yAxis: [{
                    type: 'value',
                    position: 'left',
                    interval: 6000,
                    max: 48000,
                    axisLine: { //坐标轴轴线相关设置
                        show: false
                    },
                    axisTick: { //坐标轴刻度相关设置
                        show: false
                    },
                    axisLabel: { //坐标轴刻度标签的相关设置
                        show: true,
                        color: "#aaa",
                        fontSize: 9

                    },
                    splitLine: { //坐标轴在 grid 区域中的分隔线
                        lineStyle: {
                            color: "#eee",
                        }
                    }
                }, ],
                series: [{
                        name: '累计确诊',
                        type: 'line',
                        yAxisIndex: 0,
                        symbolSize: 4,
                        itemStyle: {
                            normal: {
                                color: 'rgb(255,215,104)',
                            }
                        },
                        data: yData21
                    },
                    {
                        name: '累计疑似',
                        type: 'line',
                        yAxisIndex: 0,
                        symbolSize: 4,
                        itemStyle: {
                            normal: {
                                color: 'rgb(127,17,0)',
                            }
                        },
                        data: yData22
                    }

                ]
            };
            echarts2.setOption(echarts2_option);

            // 全国疫情累计死亡/治愈趋势图
            var addData30 = tojson.chinaDayList;
            var xData30 = [];
            var yData31 = [];
            var yData32 = [];
            for (var m = 0; m < addData30.length; m++) {
                xData30.push(addData30[m].date);
                yData31.push(addData30[m].dead);
                yData32.push(addData30[m].heal);
            }
            var echarts3 = echarts.init(document.getElementById('echarts3'));
            var echarts3_option = {
                title: {
                    top: '0',
                    left: 'left',
                    text: '全国疫情累计死亡/治愈趋势图',
                    textStyle: {
                        align: 'left',
                        color: '#000',
                        fontWeight: '500',
                        fontSize: 13,
                    }
                },
                backgroundColor: '#fff',
                legend: {
                    right: '0',
                    top: '20px',
                    itemWidth: 10,
                    itemHeight: 5,
                    itemGap: 15,
                    textStyle: {
                        color: '#333',
                        fontSize: 10,
                    },
                    icon: 'roundRect',
                    data: ['累计死亡', '累计治愈']
                },
                grid: {
                    right: '0',
                    bottom: '0',
                    left: '0',
                    top: '50px',
                    containLabel: true
                },
                xAxis: [{
                    type: 'category',
                    data: xData30,
                    axisLine: { //坐标轴轴线相关设置
                        lineStyle: {
                            color: "#aaa"
                        }
                    },
                    axisTick: { //坐标轴刻度相关设置
                        show: true,
                        lineStyle: {
                            color: '#aaa',
                            width: 1,
                        },
                        length: 3,
                    },
                    axisLabel: { //坐标轴刻度标签的相关设置
                        show: true,
                        // interval:1,
                        textStyle: {
                            color: "#aaa",
                            fontSize: 9,
                        },
                        rotate: 30
                    }
                }],
                yAxis: [{
                    type: 'value',
                    position: 'left',
                    interval: 600,
                    max: 6000,
                    axisLine: { //坐标轴轴线相关设置
                        show: false
                    },
                    axisTick: { //坐标轴刻度相关设置
                        show: false
                    },
                    axisLabel: { //坐标轴刻度标签的相关设置
                        show: true,
                        color: "#aaa",
                        fontSize: 9

                    },
                    splitLine: { //坐标轴在 grid 区域中的分隔线
                        lineStyle: {
                            color: "#eee",
                        }
                    }
                }, ],
                series: [{
                        name: '累计死亡',
                        type: 'line',
                        yAxisIndex: 0,
                        symbolSize: 4,
                        itemStyle: {
                            normal: {
                                color: 'rgb(180,192,213)',
                            }
                        },
                        data: yData31
                    },
                    {
                        name: '累计治愈',
                        type: 'line',
                        yAxisIndex: 0,
                        symbolSize: 4,
                        itemStyle: {
                            normal: {
                                color: 'rgb(102,204,153)',
                            }
                        },
                        data: yData32
                    }

                ]
            };
            echarts3.setOption(echarts3_option);

            // china 表格
            $(".china.table_pro .content").html(eachchina(chinaData));
            var china_line_first = $('.china.table_pro .content li.c_line .line_first');
            china_line_first.on('click', function () {
                $(this).next().slideToggle(500);
                $(this).find('img').toggleClass('rotate');
            });

            // world 表格
            tojson.areaTree.shift();
            var worldData = tojson.areaTree;
            $(".world.table_pro .content").html(eachworld(worldData));

        },
        error: function () {
            console.log('请求数据出错');
        }
    });


    $.ajax({
        url: "https://view.inews.qq.com/g2/getOnsInfo?name=wuwei_ww_time_line", //请求的服务端地址
        type: "post",
        dataType: "JSONP",
        success: function (data) {
            var ssdata = JSON.parse(data.data);
            // console.log(ssdata);
            var newestdata = ssdata.reverse().slice(0, 20); //20条数据

            var newswrap = $(".dongtai .main .cbp_tmtimeline");
            newswrap.html(eachnews(newestdata));

        },
        error: function () {
            console.log('请求数据出错');
        }
    });
});




function eachchina(obj) {
    var str = '';
    if (obj.constructor == Array) {
        for (var i = 0, len = obj.length; i < len; i++) {
            str += `<li class="c_line">
                        <div class="line_first">
                            <span class="c_area">
                                <img src="images/arrow.png">`;
            str += `<div style="display:inline-block;margin-left:0.1rem;">` + obj[i].name + `</div>`;
            str += `</span>`;
            str += `<span class="c_confirm">` + obj[i].total.confirm + `</span>`;
            str += `<span class="c_dead">` + obj[i].total.dead + `</span>`;
            str += `<span class="c_heal">` + obj[i].total.heal + `</span>`;
            str += `</div>`;

            if (obj[i].children) {
                str += `<div class="line_hide">`;
                for (var j = 0; j < obj[i].children.length; j++) {
                    var thefirstchildren = obj[i].children[j];
                    str += `<div class="hide_content">`;
                    str += `<span class="c_area">` + thefirstchildren.name + `</span>`;
                    str += `<span class="c_confirm">` + thefirstchildren.total.confirm + `</span>`;
                    str += `<span class="c_dead">` + thefirstchildren.total.dead + `</span>`;
                    str += `<span class="c_heal">` + thefirstchildren.total.heal + `</span>`;
                    str += `</div>`;
                }
                str += `</div>`;
            }
            str += `</li>`;
        }
        return str;
    }
}

function eachworld(obj) {
    var str = '';
    if (obj.constructor == Array) {
        for (var i = 0, len = obj.length; i < len; i++) {
            str += `<li class="c_line">
                        <div class="line_first">`;
            str += `<span class="c_area" style="text-align:center;">` + obj[i].name + `</span>`;
            str += `<span class="c_confirm">` + obj[i].total.confirm + `</span>`;
            str += `<span class="c_dead">` + obj[i].total.dead + `</span>`;
            str += `<span class="c_heal">` + obj[i].total.heal + `</span>`;
            str += `</div>`;
            str += `</li>`;
        }
        return str;
    }
}

function eachnews(obj) {
    var str = '';
    if (obj.constructor == Array) {
        for (var i = 0, len = obj.length; i < len; i++) {
            var thetime = obj[i].time.split(" ");

            if (obj[i].time != "") {
                str += `<li>
                            <div class="cbp_tmtime">`;
                str += `<span>` + thetime[0] + `</span>`;
                str += `<span>` + thetime[1] + `</span>`;
                str += `</div>
                            <div class="cbp_tmlabel">`;
                str += `<h2>` + obj[i].title + `</h2>`;
                str += `<p style="font-size: 0.25rem;padding:10px 0 0 0;">` + obj[i].desc + `</p>`;
                str += `</div>`;
                str += `</li>`;
            }
        }
        return str;
    }
}

var ospan = document.querySelectorAll('.middle_con .wrap .tabs .tabs_wrap span');
var num_op = 0;
var tabs_list = document.querySelectorAll('.middle_con .wrap div.tabs_content .tabs_list');
tabs_list[0].style.display = 'block';

for (var i = 0; i < ospan.length; i++) {
    ospan[i].index = i;
    //一级标题：滑入事件
    ospan[i].onclick = function () {
        //一级标题：style变化
        ospan[num_op].className = '';
        this.className = 'sty';
        //二级内容：block变化
        tabs_list[num_op].style.display = '';
        tabs_list[this.index].style.display = 'block';
        num_op = this.index;
    }
}