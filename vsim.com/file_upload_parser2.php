<?php
$fileName1 = $_FILES["fileToUpload1"]["name"]; // The file name
$fileTmpLoc1 = $_FILES["fileToUpload1"]["tmp_name"]; // File in the PHP tmp folder
$fileType1 = $_FILES["fileToUpload1"]["type"]; // The type of file it is
$fileSize1 = $_FILES["fileToUpload1"]["size"]; // File size in bytes
$fileErrorMsg1 = $_FILES["fileToUpload1"]["error"]; // 0 for false... and 1 for true


if (!$fileTmpLoc1) { // if file not chosen
    echo "ERROR: Please browse for two files before clicking the analyze button.";
    exit();
}

if (move_uploaded_file($fileTmpLoc1, "./VSIM/$fileName1")) {
    echo "$fileName1 upload is complete";
} else {
    echo "move_uploaded_file failed";
}
?>
