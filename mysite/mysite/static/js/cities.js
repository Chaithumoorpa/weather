let cities =[]

function fetchCities(url){

    console.log("Fetching cities...")
    fetch(url)
    .then(response => response.json())
    .then(
    data => {
        cities = data
    }
    ).catch(error => console.error("Error fetching cities :", error));


};


function loadSuggestions(){

    const input = document.getElementById("city");
    const filter = input.ariaValueText.toLocaleLowerCase();
    const SuggestionBox = document.getElementById("suggestions");


    //to clear previous suggestions
    SuggestionBox.innerHTML = "";


    //display matching cities from the json data
    const matchingCities = cities.filter(city => city.name.toLocaleLowerCase().includes(filter));

    if(matchingCities.length > 0 ){
        SuggestionBox.style.display = "block";

        matchingCities.forEach( city => {
            const suggestionDiv = document.createElement("div");

            suggestionDiv.textContent = city.name;

            suggestionDiv.addEventListener("click", function(){

                input.value = city.name;
                SuggestionBox.style.display = "none";
                
            });
            SuggestionBox.appendChild(suggestionDiv);
        });

    }else{
        SuggestionBox.style.display = "none";
    }


}

// Hide suggestions when clicking outside
document.addEventListener("click", function(e) {
    const suggestionsBox = document.getElementById("suggestions");
    if (e.target !== document.getElementById("city-input")) {
suggestionsBox.style.display = "none";  // Hide the suggestions box
    }
});