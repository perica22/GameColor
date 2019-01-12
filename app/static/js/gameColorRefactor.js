var colors = null;
var colorPicked = null;

var squares = $(".square");
var h1 = $("#h1");
var colorDisplay = $("#colorDisplay");
var newColors = $("#new_colors");
var hardBtn = $("#hardBtn");
var easydBtn = $("#easydBtn");
var play = $("#play");
var home = $("a[href*='user/']");
var logout = $("a[href*='logout']")




reset();



//core functionality
function reset(){
	var cookie = document.cookie

	selectedMode = Number(cookie)
	colors = generateRandomColors(selectedMode);
	colorPicked = pickColor(selectedMode);

	//changing RGB in H1
	colorDisplay.html(colorPicked);

	initialSet(selectedMode, squares);

	clickOnSquares();
	
	$('#message').text('');
	h1[0].style.background = "steelblue";
}

//generating random colors
function generateRandomColors(number){
	colors = [];

	for (i = 0; i < number; i++){
		var color = "rgb(";

		for (j = 0; j < 3; j++){
			var n = Math.floor(Math.random() * 255);
			if (j == 2){
				color = color + n + ")";
			}
			else{ 
				color = color + n + ", ";
			}
		}
		colors.push(color);	
	}
	return colors;
};


//randomly picking number
function pickColor(number){
	var random = Math.floor(Math.random() * number);
	return colors[random];
};


//setting color for all squares
function initialSet(selectedMode, squares){
	for (i = 0; i < squares.length; i++){
		if (colors[i]){
			//changing color of squares
			squares[i].style.display="block";
			squares[i].style.backgroundColor = colors[i];
		}
		else{
			squares[i].style.display="none";
		}
	}
	clickOnSquares();
};


//adding a click event to all squares
function clickOnSquares(){
	for (i = 0; i < squares.length; i++){
		squares[i].addEventListener("click", function(){
			var clickedColor = this.style.backgroundColor;
			
			//checking if clicked square is correct one
			if (clickedColor === colorPicked){
				$('#message').text('Correct!');

				//changing colors for all squares
				winColors(colorPicked);
				h1[0].style.background = clickedColor;
			}
			else {
				this.style.background = "#232323";
				$('#message').text('Try again!');
			}
		})	
	}
};


//change colors of all squares after win
function winColors(color){
for (j = 0; j < squares.length; j++){
		squares[j].style.backgroundColor = color;
	}
};


function reset_to_hardmode(){
	document.cookie = "3; expires=Thu, 08 Jan 2019 00:00:00 UTC;"
	document.cookie = "6; path=/game";
};




//reset button
newColors.on('click', function() { 
	reset(selectedMode, squares);
 });


//selecting easy mode
easydBtn.on("click", function(){	
	$(this).addClass("selected");
	hardBtn.removeClass("selected");

	document.cookie = "6; expires=Thu, 08 Jan 2019 00:00:00 UTC;"
	document.cookie = "3; path=/game";

	reset(squares);
});

//selecting hard mode
hardBtn.on("click", function(){
	$(this).addClass("selected");
	easydBtn.removeClass("selected");

	reset_to_hardmode()
	
	reset(squares);
});


//selecting easy mode
home.on("click", function(){	
	reset_to_hardmode()

});


logout.on("click", function(){	
	reset_to_hardmode()

});


play.on("click", function(){	
	if (document.cookie == null){
		document.cookie = "6; path=/game";
	}
});