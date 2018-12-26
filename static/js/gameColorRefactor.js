var selectedMode = 6;
var colors = null;
var colorPicked = null;

var squares = $(".square");
var h1 = $("#h1");
var colorDisplay = $("#colorDisplay");
var displayMessage = $("#message");
var newColors = $("#reset");
var hardBtn = $("#hardBtn");
var easydBtn = $("#easydBtn");



reset();

//selecting easy mode
easydBtn.on("click", function(){
	$(this).addClass("selected");
	hardBtn.removeClass("selected");

	selectedMode = 3

	reset(selectedMode, squares);
});

//selecting hard mode
hardBtn.on("click", function(){
	$(this).addClass("selected");
	easydBtn.removeClass("selected");

	selectedMode = 6;

	reset(selectedMode, squares);
});

//reset button
newColors.on('click', function() { 
	reset(selectedMode, squares);
 });

//core functionality
function reset(){
	colors = generateRandomColors(selectedMode);
	colorPicked = pickColor(selectedMode);

	//changing RGB in H1
	colorDisplay.html(colorPicked);

	initialSet(selectedMode, squares);

	clickOnSquares();

	displayMessage.textContent = "";
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
				displayMessage.textContent = "Correct!";

				//changing colors for all squares
				winColors(colorPicked);
				h1[0].style.background = clickedColor;
			}
			else {
				this.style.background = "#232323";
				displayMessage.textContent = "Try again!";
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