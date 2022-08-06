<?php include 'connect.php';?>
<html>
    <head>
    </head>
    <body>
        <div>
            <?php   
                $sql = "SELECT * FROM movie";
                $result = $conn->query($sql);

                if($result->num_rows > 0) {
                    while($row = $result->fetch_assoc()) { ?>
                        <div style='display:flex; margin-bottom: 20px;'>
                            <img src=<?php echo $row['image']; ?> style='margin-right: 50px; width: 250px; height: 250px;'/>
                            <div>
                                <p>name : <?php echo $row['name']; ?></p>
                                <p>directorName : <?php echo $row['director_name']; ?></p>
                                <a href=<?php echo "show_movie.php?id={$row['id']}&lang=en"; ?> style="display: block;">show_comments - english<a/>
                                <a href=<?php echo "show_movie.php?id={$row['id']}&lang=it"; ?> style="display: block;">show_comments - italian<a/>
                                <a href=<?php echo "show_movie.php?id={$row['id']}&lang=es"; ?> style="display: block;">show_comments - espanish<a/>
                                <a href=<?php echo "show_movie.php?id={$row['id']}&lang=fr"; ?> style="display: block;">show_comments - 	French<a/>
                            </div>
                        </div>
                <?php    }
                } else {
                    echo "No movie found!";
                }
                $conn->close();
                exit;
            ?>
        </div>
    </body>
</html>