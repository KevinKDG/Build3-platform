<?php

$target_dir = "uploads/";//locatie map foto's

//error
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
    //databank connecteren
      //$ID = filter_input(INPUT_POST, 'UUID()');
    $CameraName = filter_input(INPUT_POST, 'CameraName');
    $CameraLocation = filter_input(INPUT_POST, 'CameraLocation');
    $ImageLink = filter_input(INPUT_POST, 'ImageLink');



    //waar foto's zich bevinden
    $target_dir = "uploads/";//welke map "voor de foto's

//databank

    //dataconnectie
    $servername = "localhost";
    $username = "admin";
    $password = "password";
    $dbname = "DB1";


    // Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
    // Check connection
    if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
    }


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
die("Connection failed: " . $conn->connect_error);
}
// echo "Connected successfully";
?>
//require_once('db.php');
$sql="SELECT `nummerplaat`, `data` FROM `Platform-build`"

$result = $conn->query($sql);

if ($result->fetch_assoc()){
  while ($row = $result->fetch_assoc()) {
    echo </br>
    echo $row["nummerplaat"]
    echo '<p> '. $row["data"] .'</p>'
  }
}
echo $sql;



?>


<!DOCTYPE html>
<html>
<body>

<svg width="10000" height="10000">
  <rect x="80" y="30" width="800" height="600" style="fill:rgb(148,255,51)" />

  <rect x="80" y="60" width="800" height="130" style="fill:rgb(0,0,255)" />

  <rect x="80" y="250" width="800" height="130" style="fill:rgb(0,0,255)" />

  <rect x="80" y="440" width="800" height="130" style="fill:rgb(0,0,255)" />

  <circle cx="460" cy="125" r="50"  fill="white" />
  <text x="520" y="125" fill="black">90%</text>


  <circle cx="460" cy="320" r="50"  fill="white" />
  <text x="520" y="320" fill="black">90%</text>


  <circle cx="460" cy="500" r="50"  fill="white" />
  <text x="520" y="510" fill="black">90%</text>

</svg>

</body>
</html>
