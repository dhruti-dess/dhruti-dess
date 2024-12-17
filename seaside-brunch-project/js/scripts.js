// home page

// I used buttons and functions that our triggered when the buttons are clicked to reveal the introduction paragraphs, each paragraph after hte welcome paragraph is assigned to its own button so that each story can be accesses independently
// I used innerHTML so that the paragraphs would display right under the button
function ourStory() {
    document.getElementById("story").innerHTML =
    "Seaside Brunch was founded by two local surfers. Their story is quite spontaneous. One day they were sitting on their boards are enjoying the calm waters when they realized how hungry they were. They thought about how amazing it would be to have a restaurant right on the beach, so they can enjoy their surfs and then chill afterwards with some good food. It did not take long for them to make this idea into a reality. They got all their friends to help them and once they were done, they spent the first night of the restaurant dancing and eating the night away.";
        }
        function ourFood() {
            document.getElementById("food").innerHTML =
            "All the menu items are curated by the makers of the restaurant. They decided when they were making the restaurant, that every friend gets to choose one food item that they had that blew them away throughout their entire lives. That is where our limited, but amazing menu was born. Every food item has a story to it, that can be found in the menu.";
                }
                function dancing() {
                    document.getElementById("dance").innerHTML =
                    "Dancing is something that is very close to our hearts here at Seaside Brunch. We have our very own dance floor outside that is surrounded by the beach and beautiful lights. We start playing dance music once the sun starts setting, and we have had many memorable nights on it. Whether or not you are a good dancer, you will want to join the locals as they enjoy the music and food out on the dancefloor.";
                        }

// menu page

// I used toggle buttons like we had learned in 8-passval, I was interested in making the images for the food toggle so sad they can be shown and hidden.
// I used a query selector All so that I can tap into all of the buttons with the class toggleBtn
const toggleBtns = document.querySelectorAll('.toggleBtn');

// I used for each so that it can go through each of the toggleBtns
toggleBtns.forEach(function(toggleBtn) {
    toggleBtn.addEventListener('click', function() { // I used an event listener so that anytime the button is click, it either shows or hide the image
        const container = this.parentNode; // I used this. from 5-object so that it can grab the parentNode from the toggleBtn activated in the container
        const image = container.querySelector('img'); // I used queryselector again to pick the image associated with the btn in the container
        image.classList.toggle('hide'); // I used classList to add the toggle and hide feature so I can use css with it to make it show or hide on the site
    });
});

// contact page

// I used input fields for the contact info fill outs, and then got them by attaching the different id's for each value, then I used get element by id .value to get the value and assigned the value to a variable
function submitInfo() {
    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    // The function is used when the button is clciked, and the output message goes in the submittedMessage p id field
    const submittedMessage = document.getElementById('submittedMessage');

    submittedMessage.innerHTML = "Thank you for taking your time to fill this out " + firstName + " " + lastName + "!" + " We will get back to you as soon as possible!";

    // I used inner HTML to get the message to have the values from the variables so that the contact info is addressed
}