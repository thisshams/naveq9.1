
function colorChange()
{
    var currentPosition = document.getElementById("current").value;
    var destinationPosition = document.getElementById("destination").value;
    if(currentPosition == "")
    {
        alert("Please Select Nearest Room Number.")
        return false;
       
    }
    else if(destinationPosition == "")
    {
        alert("Please Enter Your Destination.")
        return false;
        
    }
    else if(currentPosition==destinationPosition)
    {
        alert("Current and Destination position cannot be same.")
    }
    else
    {
    localStorage.setItem("current", currentPosition);
    localStorage.setItem("destination", destinationPosition);
    

    var gfloor=["Room G01","Room G02","Room G03","Room G04","Room G05","WaterFilter","Room G06","Girls Washroom","Room G07","Room G08","Room G09","Room G10","Room G11","Room G12","Room G13","HOD ME","Room G15","Room G18","Boys Washroom","Room G19","Room G20","Room G21","Room G22","Room G23","Room G24","Second College","Auditorium","Fountain","HOD CE","Room G25","Room G26","Room G27","Room G28","Room G29","Girls Washroom","HOD IT","Room G30","Room G31","Room G32","Room G33","Room G34","Room G35","WaterFilter","Boys Washroom","Room G36","Room G37","Room G38","Room G39","Room G40","Room G41","Room G42"];
    var ffloor=["Room 101","Room 102","Room 103","Room 105b","Room 105","Room 105a","To Stairs1f","Room 106","Room 107","Girls WashRoom1f","Room 108","Room 109","Room 110","Room 111","Room 112","Room 113","To Stairs2f","Room 117a","Room 117","Room 114","Boys WashRoom1f","Room 115","Room 116","Room 118","Room 119","Room 120","To Ground Floor","Room 121","Room 122","Room 123","Room 124","To Stairs3f","Room 124a","Room 125","Room 126","Room 127","Girls WashRoom2f","HOD CS","Room 128","Room 129","Room 130","Room 131","Room 132","Boys WashRoom2f","Room 132","Room 133b","Room 133","Room 133a","To Stairs4f","Room 134","Room 135","Room 136","Stairs To Ground Floor"];
    if ((gfloor.includes(currentPosition)) && (gfloor.includes(destinationPosition))==true)
        {
            window.location.href = 'groundFloorMap';
        }
    else if((ffloor.includes(currentPosition)) && (ffloor.includes(destinationPosition))==true){
            window.location.href = 'firstFloorMap';
        }
    else{
            alert("Route not Found");
        }
    }
   
}
// for calling toMap to give input by touch
function toMap(){
    window.location.href = 'toMap'; 
}
//to call maps
function toGFM(){
    window.location.href='groundFloorTouchMap';
}
function toFFM(){
    window.location.href='firstFloorTouchMap';
}
function toSFM(){
    window.location.href='secondFloorMap';
}
