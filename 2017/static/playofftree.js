var bracketEast = {
  "teams": [              // Matchups
      ['<img src="static/thumbnails/MTLthumbnail.png" height="100%"></img> MTL',
       '<img src="static/thumbnails/NYRthumbnail.png" height="100%"></img> NYR'],  
      ['<img src="static/thumbnails/OTTthumbnail.png" height="100%"></img> OTT',
       '<img src="static/thumbnails/BOSthumbnail.png" height="100%"></img> BOS'],   
      ['<img src="static/thumbnails/WSHthumbnail.png" height="100%"></img> WSH',
       '<img src="static/thumbnails/TORthumbnail.png" height="100%"></img> TOR'],  
      ['<img src="static/thumbnails/PITthumbnail.png" height="100%"></img> PIT',
       '<img src="static/thumbnails/CBJthumbnail.png" height="100%"></img> CBJ']
  ],
  results: [
      [
          [[2, 4,'R1-G5'], [4, 2, 'R1-G6'], [4, 2, 'R1-G7'], [1, 4, 'R1-G8']],
          [[2, 4,'DF-G3'], [3, 4, 'DF-G4']],
          [[3, 4,'CF-G2']]
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
          [[0, 4,'R1-G1'], [1, 4, 'R1-G2'], [4, 0, 'R1-G3'], [4, 2, 'R1-G4']],
          [[4, 2,'DF-G1'], [4, 3, 'DF-G2']],
          [[4, 2,'CF-G1']]
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
    //$('#matchCallback').text( data )
    window.open("/games/"+data,$('#matchCallback').text( data ) ,'width=800,height=600,scrollbars=yes')
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

