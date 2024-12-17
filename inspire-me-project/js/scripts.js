
// changing the profile picture and having it saved so it can be used always
function profilePic(picture) {
    var profilePicture = document.getElementById('profilePicture');
          // i stored the picture in local storage so that it wouldnt be removed when the page was changed or refreshed
        localStorage.setItem('selectedPicture', picture);
    profilePicture.src = picture;
}

    var profilePicture = document.getElementById('profilePicture');
    var selectedPicture = localStorage.getItem('selectedPicture');

// i made it so that the selected picture could be used across all the pages and when it was changed, the picture would update on all the pages where it was being used
if (selectedPicture) {
    profilePicture.src = selectedPicture; // this sets the picture to be whatever the chosen source was
}



// I used a similar method with text values instead of images to get the name inputted in the edit-profile.html to output in the profile.html
function submitInfo() {
    var name1 = document.getElementById('firstName').value; // gets text value that was inputted after the button was clicked
    localStorage.setItem('name1', name1); // saves to name1

}

var name1 = localStorage.getItem('name1'); // value is access and assigned a variable
var displayName = document.getElementById('display'); // gets the id for where the name will be outputted

if (name1) { // checks for the value
    displayName.innerHTML = "Hello, " + name1 + "!"; // if there is a value, it will read with the inputted value
} else {
    displayName.innerHTML = "Hello!"; // if there is not value it will read without the value from the variable
}

// I used a similar method again, but this time the information that was inputted was not used anywhere else, it was just saved and shown on the page no matter if it was refreshed or switched. The only way to change the text inputted is to erase it and to write something new and click the button.
var bio = localStorage.getItem('bio'); // this gets the value from the textbox and assigns them to a variable
var interests = localStorage.getItem('interests');

if (bio) {
    document.getElementById('introduceYourself').value = bio; // checks if the value exists
}

if (interests) {
    document.getElementById('interests').value = interests; // checks if the value exists
}

function submitBio() {
    var bio = document.getElementById('introduceYourself').value; // gets the values and assigns them to local variable
    var interests = document.getElementById('interests').value; // gets the values and assigns them to local variable

    localStorage.setItem('bio', bio); // this sets the information from the textbox and keeps it there
    localStorage.setItem('interests', interests);

    if (bio) {
        editProfileFinished.innerHTML = 'changes saved'; // displays a message when the button is clicked to indicate something did happen
    }
    if (interests) {
        editProfileFinished = 'changes saved'; // displays a message when the button is clicked to indicate something did happen
    }
}

// like counter for each picture
function likePost(imageId) { // the function grabs whatever the button id click is and adds a like to that specific caption, every post has its own counter.
    // this information is not saved like the others because it is not necessary
    const likeCount = document.getElementById(`likes${imageId}`);
    let count = Number(likeCount.innerHTML);
    count++;
    likeCount.innerHTML = count.toString(); // this displays the amount of likes as a string in caption

    // trigger a CSS rule
    // when the like counter reaches 2 or more like it changes colors just to indicate that this post has already been like by you

    if (count >= 2) {
        likeCount.classList.add('changeColor'); // adds the class so the rule can be triggered
    } else {
        likeCount.classList.remove('changeColor'); // if not triggered, the rule does not apply
    }
}

