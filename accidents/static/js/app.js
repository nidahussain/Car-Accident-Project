// var pg = require(pg);

function buildPlot() {
    /* data route */
  // Attempting to bring DB into js... not needed anymore
  // var connectionString = "postgres://postgres:Catpuss10!@localhost/ip:5432/US_Accidents";
  // var pgClient = new pg.Client(connectionString);
  
  // we might use this csv if all else fails... 
  // var acc_data = "/data/US_Accidents_May19_2018_2019.csv";

  d3.json(acc_data).then(function(response) {
    // console.log(response);
    // console.log(csv);
    var data = response;

    var layout = {
      scope: "usa",
      title: "Accidents",
      showlegend: false,
      height: 600,
            // width: 980,
      geo: {
        scope: "usa",
        projection: {
          type: "albers usa"
        },
        showland: true,
        landcolor: "rgb(217, 217, 217)",
        subunitwidth: 1,
        countrywidth: 1,
        subunitcolor: "rgb(255,255,255)",
        countrycolor: "rgb(255,255,255)"
      }
    };

    Plotly.newPlot("plot", data, layout);
  });
}

buildPlot();
