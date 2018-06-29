var bracketEast = {
  "teams": [              // Matchups
      ['<img src="static/thumbnails/TBLthumbnail.png" height="100%"></img> TBL',
       '<img src="static/thumbnails/NJDthumbnail.png" height="100%"></img> NJD'],  
      ['<img src="static/thumbnails/BOSthumbnail.png" height="100%"></img> BOS',
       '<img src="static/thumbnails/TORthumbnail.png" height="100%"></img> TOR'],   
      ['<img src="static/thumbnails/WSHthumbnail.png" height="100%"></img> WSH',
       '<img src="static/thumbnails/CBJthumbnail.png" height="100%"></img> CBJ'],  
      ['<img src="static/thumbnails/PITthumbnail.png" height="100%"></img> PIT',
       '<img src="static/thumbnails/PHIthumbnail.png" height="100%"></img> PHI']
  ],
  results: [
      [
          [[0, 0,'R1-G5'], [0, 0, 'R1-G6'], [0, 0, 'R1-G7'], [0, 0, 'R1-G8']],
          [[0, 0,'DF-G3'], [0, 0, 'DF-G4']],
          [[0, 0,'CF-G2']]
      ]
  ]
}


var bracketWest = {
  "teams": [              // Matchups
      ['<img src="static/thumbnails/NASthumbnail.png" height="100%"></img> NAS',
       '<img src="static/thumbnails/COLthumbnail.png" height="100%"></img> COL'],
      ['<img src="static/thumbnails/WPGthumbnail.png" height="100%"></img> WPG',
       '<img src="static/thumbnails/MINthumbnail.png" height="100%"></img> MIN'],
      ['<img src="static/thumbnails/VGKthumbnail.png" height="100%"></img> VGK',
       '<img src="static/thumbnails/LAKthumbnail.png" height="100%"></img> LAK'],
      ['<img src="static/thumbnails/ANAthumbnail.png" height="100%"></img> ANA',
       '<img src="static/thumbnails/SJSthumbnail.png" height="100%"></img> SJS']
  ],
  results: [
      [
          [[0, 0,'R1-G1'], [0, 0, 'R1-G2'], [0, 0, 'R1-G3'], [0, 0, 'R1-G4']],
          [[0, 0,'DF-G1'], [0, 0, 'DF-G2']],
          [[0, 0,'CF-G1']]
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
    window.open("/games/"+data,$('#matchCallback').text( data ) ,'width=800,height=600,toolbar=yes,scrollbars=yes')
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

