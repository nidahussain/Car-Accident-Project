Plotly.d3.csv("NJ\Just_NJ.csv",function(err, rows){

     function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

  var data = [{
      type: 'scatter',
      mode: 'markers',
      x: unpack(rows, 'Astronomical_Twilight'),
      y: unpack(rows, 'Temperature(F)'),
      text: unpack(rows, 'County'),
      marker: {
        size: unpack(rows, 'pop'),
        sizemode: "area",
        sizeref: 200000
      },
      transforms: [
        {
        type: 'filter',
        target: unpack(rows, 'year'),
        operation: '=',
        value: '2018'
        }, {
        type: 'groupby',
        groups: unpack(rows, 'County'),
        styles: [
          {target: 'Middlesex', value: {marker: {color: 'red'}}},
          {target: 'Union', value: {marker: {color: 'blue'}}},
          {target: 'Passaic', value: {marker: {color: 'orange'}}},
          {target: 'Morris', value: {marker: {color: 'green'}}},
          {target: 'Union', value: {marker: {color: 'purple'}}},
          {target: 'Camden', value: {marker: {color: 'yellow'}}},
          {target: 'Bergen', value: {marker: {color: 'brown'}}},
          {target: 'Hudson', value: {marker: {color: 'pink'}}},
          {target: 'Essex', value: {marker: {color: 'gray'}}}
        ]
  }]
    }]

var layout = {
  yaxis: {
    type: 'log'
  }
}

Plotly.plot('myDiv', data, layout)
});