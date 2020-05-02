// // // const api_url = 'https://api.covid19india.org/data.json'
// // // const response = fetch(api_url);
// // // const data = response.json();
// // // console.log(data)
// // //
// //
// // // function getdata(){
// // 	url = 'https://api.covid19india.org/data.json';
// // 	fetch(url).then((response)=>{
// // 		return response.json();
// // 	}).then((data)=>{
// // 		var d = data.statewise;
// // 		var x, txt = "";
// // 		for (x in d) {
// // 			var kl = []
// // 			as = (d[x].active)
// // 			kl.push(as)
// //
// // 			var x;
// // 			for (x of kl) {
// // 			  console.log(x)
// // 			}
// // 		};
// // 	})
// //
// //
// //
// //
// // // getdata()
//
// $(document).ready(function () {
//
// 	var ctx = $("#bar-chartcanvas");
//
// 	var data = {
// 		labels : ["HR", "PB", "MH", "JK", "KL","DL","RJ","HR", "PB", "MH", "JK", "KL","DL","RJ","HR", "PB", "MH", "JK", "KL","DL","RJ","HR", "PB", "MH", "JK", "KL","DL","RJ"],
// 		datasets : [
// 			{
// 				label : "TeamA score",
// 				data : [60, 50, 25, 70, 40,60, 50, 25, 0, 40,60, 50, 25, 70, 0,60, 50, 5, 70, 40,60, 0, 25, 70, 40,60, 50, 25],
// 				backgroundColor :
// 					"rgba(10, 20, 30, 0.3)",
//
// 				borderColor :
// 					"rgba(10, 20, 30, 1)",
//
// 				borderWidth : 1
// 			},
// 		]
// 	};
//
// 	var options = {
// 		maintainAspectRatio: false,
// 		title : {
// 			display : true,
// 			position : "top",
// 			text : "Bar Graph",
// 			fontSize : 14,
// 			fontColor : "#111"
// 		},
// 		legend : {
// 			display : true,
// 			position : "bottom"
// 		},
// 		scales : {
// 			yAxes : [{
// 				ticks : {
// 					min : 0
// 				}
// 			}]
// 		}
// 	};
//
// 	var chart = new Chart( ctx, {
// 		type : "bar",
// 		data : data,
// 		options : options
// 	});
//
// });
