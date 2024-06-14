<?php
$output = shell_exec('6_1.py'); // Execute the Python script
?>

<!DOCTYPE html>
<html>
<head>
    <title>Python Output</title>
</head>
<body>
    <h1>Python Output</h1>
    <pre>
        <?php echo $output; ?> <!-- Display Python output here -->
    </pre>
</body>
</html>