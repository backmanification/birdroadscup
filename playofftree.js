var minimalData = {
    teams : [
      ["Team 1", "Team 2"], /* first matchup */
      ["Team 3", "Team 4"]  /* second matchup */
    ],
    results : [
      [[1,2], [3,4]],       /* first round */
      [[4,6], [2,1]]        /* second round */
    ]
  }
// $(document).ready()

var bracketEast = {
  "teams": [              // Matchups
      ["MTL", "NYR"],     // Match 1
      ["OTT", "BOS"],     // Match 2
      ["WSH", "TOR"],     // Match 3
      ["PIT", "CBJ"]      // Match 4
  ],
  results: [
      [
          [[0, 1,'Match 1'], [2, 3, 'Match 2'], [4, 5, 'Match 3'], [6, 7, 'Match 4']],
          [[8, 9,'Atlantic Division Final'], [10, 11, ' Division Final']],
          [[12, 13, 'Western Conference Final'], [null, null, 'game']]
      ]
  ]
}


var bracketWest = {
  "teams": [              // Matchups
      ["CHI", "NAS"],     // Match 1
      ["MIN", "STL"],     // Match 2
      ["ANA", "CGY"],     // Match 3
      ["EDM", "SJS"]      // Match 4
  ],
  results: [
      [
          [[0, 1,'Match 1'], [2, 3, 'Match 2'], [4, 5, 'Match 3'], [6, 7, 'Match 4']],
          [[8, 9,'Central Division Final'], [10, 11, 'Pacific Division Final']],
          [[12, 13, 'Western Conference Final'], [null, null, 'game']]
      ]
  ]
}
 
 
$(function() {
    $('#demo').bracket({
	skipConsolationRound: true,
	init: bracketWest /* data to initialize the bracket with */ })
    $('#demo2').bracket({
	skipConsolationRound: true,
	dir: 'rl',
	init: bracketEast /* data to initialize the bracket with */ })
});



// http://www.aropupu.fi/bracket/

