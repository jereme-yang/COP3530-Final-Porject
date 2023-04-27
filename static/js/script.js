<script>
    let current_index = 0; // Initialize current_index
    let level = 0; // Initialize level
    let has_lost = false; // Initialize has_lost

    let game_state = {
        "game_over": false,
        "level": level,
        "current_artist": "Start the game",
        "option1": "Option 1",
        "option2": "Option 2"
    };

    function updateUI() {
        $("#level").text(game_state.level);
        $("#current-artist").text(game_state.current_artist);
        $("#option1").text(game_state.option1);
        $("#option2").text(game_state.option2);
    }

    function submitChoice(choice) {
        if (game_state.game_over) return;

        $.ajax({
            url: "/api/new_round",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({user_choice: choice.toString(), game_state: [current_index, level, has_lost]}),
            dataType: "json",
            success: function(response) {
                game_state = response;
                current_index = response.current_index; // Update current_index
                level = response.level; // Update level
                has_lost = response.game_over; // Update has_lost
                
                if (game_state.game_over) {
                    $("#game-over").show();
                    $("#final-score").text(game_state.final_score);
                } else {
                    updateUI();
                }
            },
            error: function(error) {
                console.log("Error:", error);
            }
        });
    }

    updateUI();
</script>