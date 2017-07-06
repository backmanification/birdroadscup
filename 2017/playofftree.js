var bracketEast = {
  "teams": [              // Matchups
      ['<img src="teams/MTL/MTLthumbnail.png" height="100%"></img> MTL', '<img src="teams/NYR/NYRthumbnail.png" height="100%"></img> NYR'],  
      ['<img src="teams/OTT/OTTthumbnail.png" height="100%"></img> OTT', '<img src="teams/BOS/BOSthumbnail.png" height="100%"></img> BOS'],   
      ['<img src="teams/WSH/WSHthumbnail.png" height="100%"></img> WSH', '<img src="teams/TOR/TORthumbnail.png" height="100%"></img> TOR'],  
      ['<img src="teams/PIT/PITthumbnail.png" height="100%"></img> PIT', '<img src="teams/CBJ/CBJthumbnail.png" height="100%"></img> CBJ']
  ],
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
      ['<img src="teams/CHI/CHIthumbnail.png" height="100%"></img> CHI', '<img src="teams/NAS/NASthumbnail.png" height="100%"></img> NAS'],
      ['<img src="teams/MIN/MINthumbnail.png" height="100%"></img> MIN', '<img src="teams/STL/STLthumbnail.png" height="100%"></img> STL'],
      ['<img src="teams/ANA/ANAthumbnail.png" height="100%"></img> ANA', '<img src="teams/CGY/CGYthumbnail.png" height="100%"></img> CGY'],
      ['<img src="teams/EDM/EDMthumbnail.png" height="100%"></img> EDM', '<img src="teams/SJS/SJSthumbnail.png" height="100%"></img> SJS']
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

