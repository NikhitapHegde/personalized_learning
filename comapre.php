<?php
$servername = "localhost";
$username = "root";
$password = "Poornima16@23";
$dbname = "student";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$username = $_POST['uname'];
$password = $_POST['pword'];

// Validate and sanitize user input
$username = $conn->real_escape_string($username);

$stmt = $conn->prepare("SELECT username, password, first_login FROM users WHERE username = ?");
$stmt->bind_param("s", $username);
$stmt->execute();
$stmt->bind_result($db_username, $db_password, $first_login);
$stmt->fetch();

$new_table_name = "user_" . $username;

if (password_verify($password, $db_password)) {
    if ($first_login == 1) {
        // If it's the user's first login, create a new table

        $create_table_sql = "CREATE TABLE IF NOT EXISTS $new_table_name (
            id INT AUTO_INCREMENT PRIMARY KEY,
            addition VARCHAR(255),
            subtraction VARCHAR(255),
            multiplication VARCHAR(255),
            division VARCHAR(255),
            english VARCHAR(255),
            progress INT DEFAULT 0,
            last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )";

        $stmt->close(); // Close the previous statement here

        if ($conn->query($create_table_sql) === TRUE) {
            echo "User-specific table $new_table_name created successfully.";
            
            // Update 'first_login' to 0 in the details table
            $update_first_login_sql = "UPDATE users SET first_login = 0 WHERE username = ?";
            $stmt_update_first_login = $conn->prepare($update_first_login_sql);
            $stmt_update_first_login->bind_param("s", $username);
            $stmt_update_first_login->execute();
            $stmt_update_first_login->close();
        } else {
            echo "Error creating user-specific table: " . $conn->error;
        }
    } else {
        echo "Welcome back, $db_username!";

        // Display existing table data
        $stmt->close(); // Close the previous statement here

        $select_data_sql = "SELECT * FROM $new_table_name";
        $result = $conn->query($select_data_sql);

        if ($result !== false) {
            if ($result->num_rows > 0) {
                echo "Existing table data:<br>";

                while ($row = $result->fetch_assoc()) {
                    // Output the data as needed
                    echo "ID: " . $row['id'] . "  , Addition:   " . $row['addition'] . ",  Subtraction:   " . $row['subtraction'] ."   Multiplication :   ". $row['multiplication'] . "  ,Division:  " . $row['division'] . "  English:  " . $row['english'] ."  Last updated:  " . $row['last_updated'] . "<br>";
                    // Add more fields as necessary
                }
            } else {
                echo "No data found in the existing table.";
            }

            // Close the result set
            $result->close();
        } else {
            echo "Error executing SELECT query: " . $conn->error;
        }
    }
} else {
    echo "Login failed. Incorrect username or password.";
}

$conn->close();
?>
