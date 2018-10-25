<?php
$fileName2 = $_FILES["fileToUpload2"]["name"]; // The file name
$fileTmpLoc2 = $_FILES["fileToUpload2"]["tmp_name"]; // File in the PHP tmp folder
$fileType2 = $_FILES["fileToUpload2"]["type"]; // The type of file it is
$fileSize2 = $_FILES["fileToUpload2"]["size"]; // File size in bytes
$fileErrorMsg2 = $_FILES["fileToUpload2"]["error"]; // 0 for false... and 1 for true

print_r($fileName2);


if (!$fileTmpLoc2){ // if file not chosen
    echo "ERROR: Please browse for two files before clicking the analyze button.";
    exit();
}

if  (move_uploaded_file($fileTmpLoc2, "./VSIM/$fileName2")) {
    echo "$fileName2 upload is complete";
} else {
    echo "move_uploaded_file failed";
}
?>
