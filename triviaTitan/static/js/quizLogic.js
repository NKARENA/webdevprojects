
const ansArray = [
    document.querySelector("#an1").innerText,
    document.querySelector("#an2").innerText,
    document.querySelector("#an3").innerText,
    document.querySelector("#an4").innerText,
    document.querySelector("#an5").innerText,
    document.querySelector("#an6").innerText,
    document.querySelector("#an7").innerText,
    document.querySelector("#an8").innerText,
    document.querySelector("#an9").innerText,
    document.querySelector("#an10").innerText
];

let selectedOptions = {};

function handleRadioChange(groupName, selectedRadio) {
    const radioButtons = document.querySelectorAll('input[name="' + groupName + '"]');
    radioButtons.forEach(radio => {
        if (radio !== selectedRadio) {
            radio.disabled = true;
        }
    });

    const selectedOption = document.querySelector('input[name="' + groupName + '"]:checked');

    if (selectedOption) {
        const selectedValue = selectedOption.value;
        const quesGroup = selectedOption.name;
        selectedOptions[quesGroup] = selectedValue;
    } else {
        console.log("No radio button selected for " + groupName);
    }
}



function calculateScore() {
    let score = 0;
    for (let i = 1; i <= 10; i++) {
        const userAnswer = selectedOptions[`ques${i}`];
        const correctAnswer = ansArray[i - 1];
        if (userAnswer && userAnswer.toLowerCase() === correctAnswer.toLowerCase()) {
            score++;
        }
    }
    console.log("User's Score:", score);

    // Store the score in local storage
    localStorage.setItem('userScore', score);

    // Redirect to the results page
    window.location.href = '/results'; // Change '/results' to the actual URL of your results page
}




function refreshPage() {
    location.reload(true);
}

// Attach the calculateScore function to the form submission
document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the form from submitting and refreshing the page
    calculateScore();
});


