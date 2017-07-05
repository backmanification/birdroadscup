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
          [[12, 13, 'Western Conference Final']]
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
          [[0, 1,'Match 1'], [2, 1, 'Match 2'], [4, 5, 'Match 3'], [6, 7, 'Match 4']],
          [[8, 9,'Central Division Final'], [10, 11, 'Pacific Division Final']],
          [[12, 13, 'Western Conference Final']]
      ]
  ]
}
 
/* Render function is called for each team label when data is changed, data
 * contains the data object given in init and belonging to this slot.
 *
 * 'state' is one of the following strings:
 * - empty-bye: No data or score and there won't team advancing to this place
 * - empty-tbd: No data or score yet. A team will advance here later
 * - entry-no-score: Data available, but no score given yet
 * - entry-default-win: Data available, score will never be given as opponent is BYE
 * - entry-complete: Data and score available
 */
function edit_fn(container, data, doneCb) {
  var input = $('<input type="text">')
  input.val(data ? data : '')
  //container.html(input)
  //input.focus()
  input.blur(function() {
    var inputValue = input.val()
    if (inputValue.length === 0) {
      doneCb(null); // Drop the team and replace with BYE
    } else {
      var flagAndName = inputValue.split(':') // Expects correct input
      doneCb(inputValue)
    }
  })
}
 

function render_fn(container, data, score, state) {
  switch(state) {
    case "empty-bye":
      container.append("No team")
      return;
    case "empty-tbd":
      container.append("Upcoming")
      return;
 
    case "entry-no-score":
    case "entry-default-win":
    case "entry-complete":
      container.append('<img src="2017/teams/'+data+'/'+data+'logo.png" height="100%" ></img> ').append(data)
      return;
  }
}


$(function() {
    $('#westBracket').bracket({
	skipConsolationRound: true,
	disableTeamEdit: true,
	disableToolbar: true,
	init: bracketWest,
	save: function(){},
	decorator: {edit: edit_fn,
		    render: render_fn}
    })
    $('#eastBracket').bracket({
	skipConsolationRound: true,
	dir: 'rl',
	disableTeamEdit: true,
	disableToolbar: true,
	init: bracketEast,
	save: function(){},
	decorator: {edit: edit_fn,
	    render: render_fn}
    })
    $('.score').off('click')
});



// http://www.aropupu.fi/bracket/

