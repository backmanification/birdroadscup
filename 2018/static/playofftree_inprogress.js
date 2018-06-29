var bracketEast = {
    function("East") {handleFiles("East")};
    matchup = []
    counter = 0
    old_team1 = "kls"
    old_team2 = "hgl"
    for (var m = 1; m < tarr.length; i++) {
	team1 = tarr[i][0]
	team2 = tarr[i][1]
	if (team1 != old_team1) {
	    counter +=1
	    latest_i = i
	    matchup[counter] = ['<img src="static/thumbnails/'+team1+'thumbnail.png" height="100%"></img> '+team2,
				'<img src="static/thumbnails/'+team2+'thumbnail.png" height="100%"></img> '+team2]
	    
	}
	
    }
    "teams": matchup,
    results: [
	[
            [[3, 0,'Match 1'], [3, 2, 'Match 2'], [3, 2, 'Match 3'], [0, 3, 'Match 4']],
            [[3, 2,'Atlantic Division Final'], [0, 3, ' Division Final']],
            [[0, 3, 'Western Conference Final']]
	]
    ]
}


var bracketWest = {
    "teams": [              // Matchups
	['<img src="static/thumbnails/CHIthumbnail.png" height="100%"></img> CHI',
	 '<img src="static/thumbnails/NASthumbnail.png" height="100%"></img> NAS'],
	['<img src="static/thumbnails/MINthumbnail.png" height="100%"></img> MIN',
	 '<img src="static/thumbnails/STLthumbnail.png" height="100%"></img> STL'],
	['<img src="static/thumbnails/ANAthumbnail.png" height="100%"></img> ANA',
	 '<img src="static/thumbnails/CGYthumbnail.png" height="100%"></img> CGY'],
	['<img src="static/thumbnails/EDMthumbnail.png" height="100%"></img> EDM',
	 '<img src="static/thumbnails/SJSthumbnail.png" height="100%"></img> SJS']
    ],
    results: [
	[
            [[0, 3,'Match 1'], [2, 3, 'Match 2'], [0, 3, 'Match 3'], [0, 3, 'Match 4']],
            [[2, 3,'Central Division Final'], [3, 2, 'Pacific Division Final']],
            [[3, 2, 'Western Conference Final']]
	]
    ]
}
/*
moddad renderfunction som skulle ge logos

function defaultRender(container: JQuery, team: string, score: any, state: EntryState): void {
    switch (state) {
      case 'empty-bye':
        container.append('BYE');
        return;
      case 'empty-tbd':
        container.append('TBD');
        return;

      case 'entry-no-score':
      case 'entry-default-win':
      case 'entry-complete':
        container.append('<img src="2017/teams/'+team+'/'+team+'logo.png" height="100%" ></img> ').append(team);
        return;
    }
}
*/

function onclick(data) {
    alert("weeeo")
}

function onhover(data, hover) {
    $('.dropdown-toggle').hover(function() {
    $('.dropdown-menu').toggle();
  });
}

$(function() {
    $('#westBracket').bracket({
	skipConsolationRound: true,
	onMatchClick: onclick,
	onMatchHover: onhover,
	init: bracketWest
    })
    $('#eastBracket').bracket({
	skipConsolationRound: true,
	dir: 'rl',
	onMatchClick: onclick,
	init: bracketEast
    })
    $('.score').off('click')

});



// http://www.aropupu.fi/bracket/

function handleFiles(side) {
    $(document).ready(function() {
        $.ajax({
            type: "GET",
            url: "static/stats/MatchStats"+side+".csv",
            dataType: "csv",
            success: function(data) { processData(data); }
        });
    });
}

function processData(allText) {
    var allTextLines = allText.split(/\r\n|\n/);
    var headers = allTextLines[0].split(',');
    var lines = [];

    for (var i = 1; i < allTextLines.length; i++) {
        var data = allTextLines[i].split(',');
        if (data.length == headers.length) {

            var tarr = [];
            for (var j = 0; j < headers.length; j++) {
                tarr.push(data[j]);
            }
            lines.push(tarr);
        }
    }
    console.log(lines);
}
/*
function drawOutput(lines) {
    //Clear previous data
    document.getElementById("output").innerHTML = "";
    var table = document.createElement("table");
    for (var i = 0; i < lines.length; i++) {
        var row = table.insertRow(-1);
        for (var j = 0; j < lines[i].length; j++) {
            var firstNameCell = row.insertCell(-1);
            firstNameCell.appendChild(document.createTextNode(lines[i][j]));
        }
    }
    document.getElementById("output").appendChild(table);
}
*/
