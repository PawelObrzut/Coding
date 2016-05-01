// Created 05/01/2016 by Pawel Obrzut
// This is a program for managers of multi-shift teams. It helps to create weekly workplans.
// There are 3 shifts: 1st DAY 09:00-17:00, 2nd EVENING 17:00-01:00, 3rd NIGHT 01:00-09:00
// At least 4 employees must be assigned to each shift and the maximum number of employees per shift is 10.
// Employees were assigned to shifts by default but can change their shifts if possible.
// Employees from the night shift have priority in changing the shift because the night shift is the most demanding one.
// The program takes into account vacation weeks.

// allWorkers is a JavaScript Object Array storing information about employees (name, assigned shift, switch preferences and possible absences). 
// --- Ideally this information would be stored in an external data base e.g. SQL, MongoDB...

var allWorkers = [
    {name: "Pawel", shift: 1, desiredShift: 3, onHoliday: true},
    {name: "Tomek", shift: 2, desiredShift: 1, onHoliday: false},
    {name: "Daniel", shift: 3, desiredShift: 2, onHoliday: false},
    {name: "Marcin", shift: 1, desiredShift: 2, onHoliday: false},
    {name: "Monika", shift: 2, desiredShift: 3, onHoliday: false},
    {name: "Anna", shift: 3, desiredShift: 1, onHoliday: false},
    {name: "Kasia", shift: 1, desiredShift: 3, onHoliday: false},
    {name: "Krzysiek", shift: 2, desiredShift: 1, onHoliday: false},
    {name: "Wojtek", shift: 3, desiredShift: 2, onHoliday: false},
    {name: "Karol", shift: 1, desiredShift: 2, onHoliday: true},
    {name: "Magda", shift: 2, desiredShift: 3, onHoliday: false},
    {name: "Rafal", shift: 3, desiredShift: 1, onHoliday: false},
    {name: "Grzegorz", shift: 1, desiredShift: 3, onHoliday: true},
    {name: "Karolina", shift: 2, desiredShift: 1, onHoliday: false},
    {name: "Alina", shift: 3, desiredShift: 2, onHoliday: false},
    {name: "Dorota", shift: 1, desiredShift: 2, onHoliday: true},
    {name: "Jerzy", shift: 2, desiredShift: 3, onHoliday: false},
    {name: "Wieslaw", shift: 5, desiredShift: 3, onHoliday: false}
    ];

// Constructor for adding new employees
function Worker(name,shift,desiredShift,onHoliday){
    this.name = name;
    this.shift = shift;
    this.desiredShift = desiredShift;
    this.onHoliday = onHoliday;
}

// adding new workers to allWorkers method
var addWorkers = function(worker){
    allWorkers.push(worker);
};

// using Constructor and method
var boniek = new Worker("Boniek",3,1,false);
addWorkers(boniek);

var steve = new Worker("Steve",3,1,false);
addWorkers(steve);

// creating empty list in order to store available employees
var availableWorkers = [];

// adding available employees to availableWorkers list
for (var worker = 0; worker < allWorkers.length; worker++){
    if (allWorkers[worker].onHoliday === false){
    availableWorkers.push(allWorkers[worker]);
        }
    }

// creating empty lists for each shift
var shift1 = [];
var shift2 = [];
var shift3 = [];

// assigning available employees to their default shift
for (var worker = 0; worker < availableWorkers.length; worker++){
    if (availableWorkers[worker].shift == 1){
        shift1.push(availableWorkers[worker].name);
        } else if (availableWorkers[worker].shift == 2){
            shift2.push(availableWorkers[worker].name);
        } else if (availableWorkers[worker].shift == 3){
            shift3.push(availableWorkers[worker].name);
        } else {
        // If employee has an invalid shift information the following will be displayed.
            confirm("Invalid -shift- input for " + availableWorkers[worker].name + "\n");
        }
    } 

// printing default shifts
console.log("\nAvailable employees on the first shift: ");
console.log(shift1);
console.log("\nAvailable employees on the second shift: ");
console.log(shift2);
console.log("\nAvailable employees on the third shift: ");
console.log(shift3);

console.log("\n");

// Select employees who want to change their shift for an upcomming week.
for (var worker = 0;  worker<availableWorkers.length; worker++){
    // Checking if the third shift wants to and can change
    if (availableWorkers[worker].shift == 3 && (availableWorkers[worker].desiredShift == 1 || availableWorkers[worker].desiredShift == 2) && shift1.length<10 && shift2.length<10 && shift3.length>4){
        //remove employee from shift3
        var index = shift3.indexOf(availableWorkers[worker].name);
        if(index != -1) {
            shift3.splice(index, 1);
        }
        //add employee to a new shift
        if (availableWorkers[worker].desiredShift == 1){
            shift1.push(availableWorkers[worker].name);
            console.log(availableWorkers[worker].name + " changes shift from 3rd to 1st");
        } else {
            shift2.push(availableWorkers[worker].name);
            console.log(availableWorkers[worker].name + " changes shift from 3rd to 2nd");
        }
    // Checking if the second shift wants to and can change
    } else if (availableWorkers[worker].shift == 2 && (availableWorkers[worker].desiredShift == 1 || availableWorkers[worker].desiredShift == 3) && shift1.length<10 && shift3.length<10 && shift2.length>4){
        //remove employee from shift2
        var index = shift2.indexOf(availableWorkers[worker].name);
        if(index != -1) {
            shift2.splice(index, 1);
        }
        //add employee to new shift
        if (availableWorkers[worker].desiredShift == 1){
            shift1.push(availableWorkers[worker].name);
            console.log(availableWorkers[worker].name + " changes shift from 2nd to 1st");
        } else {
            shift3.push(availableWorkers[worker].name);
            console.log(availableWorkers[worker].name + " changes shift from 2nd to 3rd");
        }
    } else if (availableWorkers[worker].shift == 1 && (availableWorkers[worker].desiredShift == 2 || availableWorkers[worker].desiredShift == 3) && shift2.length<10 && shift3.length<10 && shift1.length>4){
        //remove employee from shift1
        var index = shift1.indexOf(availableWorkers[worker].name);
        if(index != -1) {
            shift1.splice(index, 1);
        }
         //add employee to new shift
        if (availableWorkers[worker].desiredShift == 2){
            shift1.push(availableWorkers[worker].name);
            console.log(availableWorkers[worker].name + " changes shift from 1st to 2nd");
        } else {
            shift3.push(availableWorkers[worker].name);
            console.log(availableWorkers[worker].name + " changes shift from 1st to 3rd");
        }
    } else {
        // do nothing
    }
}
// Printing a workplan
console.log("\n\nFINAL WORKPLAN");
console.log("\nFirst shift:");
console.log(shift1);
console.log("\nSecond shift:");
console.log(shift2);
console.log("\nThird shift:");
console.log(shift3);


