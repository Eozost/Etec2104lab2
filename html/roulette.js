// Define the roulette wheel
var wheel = ["00"].concat(Array.from({length: 36}, (_, i) => i.toString()));

function spinRoulette() {
    // Spin the wheel
    var spin = wheel[Math.floor(Math.random() * wheel.length)];
    
    // Determine color
    var color = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"].includes(spin) ? "Rouge" : "Noir";
    
    // Determine even/odd
    var evenOdd = spin === "0" || spin === "00" ? "Neither Pair nor Impair" : parseInt(spin) % 2 === 0 ? "Pair" : "Impair";
    
    // Determine failed/passed
    var failedPassed = spin === "0" || spin === "00" ? "Neither Manque nor Passe" : parseInt(spin) <= 18 ? "Manque" : "Passe";
    
    // Create a results row
    var resultsRow = "<tr>" +
                     "<td>" + spin + "</td>" +
                     "<td class='" + color.toLowerCase() + "'>" + color + "</td>" +
                     "<td class='" + evenOdd.toLowerCase() + "'>" + evenOdd + "</td>" +
                     "<td class ='" + failedPassed.toLocaleLowerCase() + "'>" + failedPassed + "</td>"
                     "</tr>";
    
    // Add the results row to the table
    document.getElementById("results").innerHTML += resultsRow;
}