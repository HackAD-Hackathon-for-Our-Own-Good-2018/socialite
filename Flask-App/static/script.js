var questions = [
{question:"Enter your net id.", type:"text"},
{question:"Please confirm your net id.", type:"text"},
{question:"Full name?",type:"text"},
{question:"Preferred name?",type:"text"},
{question:"Three things you like?",type:"text"},
//separate by commas? 
{question:"Enter the net ids of people you don't want to meet.",type:"text"},
{question:"Graduation class?"},
{question:"Ways to contact you?"}
]
var buttonFields = document.getElementById("buttonFields");
var containerInput = document.getElementById("containerInput");
var label = document.getElementById("label");
var field = document.getElementById("field");
var position = 0;
var leftArrow = document.getElementById("leftArrow");
var rightArrow=document.getElementById("rightArrow");
var nextButton = document.getElementById("nextButton");

nextQuestion();

function nextQuestion() {
	//need a cleaner way to do this
  if (position===0){
  leftArrow.setAttribute('style','visibility:hidden');
} else {
  leftArrow.setAttribute('style','visibility:visible');
}
	if (position === 6) {
    field.setAttribute('style','display:none');
    field.required = false;
		buttonFields.innerHTML='<input type="radio" id="firstYear" name="class" value="firstyear"><label class="buttonLabel" for="firstYear">First Year</label><br><input type="radio" id="sophomore" name="class" value="sophomore"><label class="buttonLabel" for="sophomore">Sophomore</label><br><input type="radio" id="junior" name="class" value="junior"><label class="buttonLabel" for="junior">Junior</label><br><input type="radio" id="senior" name="class" value="senior"><label class="buttonLabel" for="senior">Senior</label>'
		containerInput.appendChild(buttonFields);

                    
	} else if (position===7){
		buttonFields.innerHTML='<input type="checkbox" id="facebook" name="contact" value="facebook"><label class="buttonLabel" for="facebook">Facebook/Messenger</label><br><input type="checkbox" id="instagram" name="contact" value="instagram"><label class="buttonLabel" for="instagram">Instagram</label><br><input type="checkbox" id="whatsapp" name="contact" value="whatsapp"><label class="buttonLabel" for="whatsapp">Whatsapp</label>'
		containerInput.appendChild(buttonFields);
	} 
	label.innerHTML = questions[position].question;
	field.type = questions[position].type;
	
field.value='';
	showQuestion();
}
leftArrow.addEventListener('click', prevQuestion);
rightArrow.addEventListener('click', submit);
  // field.addEventListener('keyup', function(enter){
  //   // ie hack to redraw
  //   if(enter.keyCode === 13) {
  //   	console.log("yes!");
  //   	submit();
  //   }
  // })
function prevQuestion() {
  position -=1;
  hideQuestion(nextQuestion)
}
  function submit() {

  	questions[position].value = field.value;
  if (position===1){
      if (questions[0].value !== questions[1].value){
        label.innerHTML = "Incorrect ID. Please enter your net ID again."
        field.value='';

      }
    }
  	position +=1;
  
  	 if (questions[position]) {hideQuestion(nextQuestion)}
  }

      function hideQuestion(callback) {
        containerInput.style.opacity = 0
        label.style.marginLeft = 0
   
        containerInput.style.border = null
        setTimeout(callback, 200)
    }

    function showQuestion(callback) {
        containerInput.style.opacity = 1
        containerInput.style.transition = ''
        containerInput.style.width = '100%'
        setTimeout(callback, 200)
    }