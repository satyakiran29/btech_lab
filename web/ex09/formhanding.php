<html>
    <head>
        <title>Form Handling</title>
        </head>
    <body>
        <form action="" method="post">
            Name: <input type="text" name="name" />
            email<input type="text" name="email" />
            <input type="submit" value="Submit" />
            </form>
        <?php   
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
           $name=htmlspecialchars($_POST['name']);
           $email=htmlspecialchars($_POST['email']);
           echo "thank you $name for submitting your email $email";
           
        }
        ?>