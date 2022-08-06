<?php include 'connect.php';?>
<html>
    <head>
    </head>
    <body>
        <?php
            $movie_id = $_GET['id'];
            $lang = $_GET['lang'];

            $sql = "SELECT * FROM comment WHERE movie_id={$movie_id}";
            $result = $conn->query($sql);

            if($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) { ?>
                    <div style="border: 1px solid black;">
                        <div>
                            <p><?php echo $row['user']; ?></p>
                            <p>
                                <?php
                                    if($lang == 'en') {
                                        echo $row['text'];
                                    } else {
                                        $ch = curl_init();

                                        curl_setopt($ch, CURLOPT_URL, 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b5676fb3-c5f7-41ee-a74d-925d805c4df7/v3/translate?version=2018-05-01');
                                        curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                                        curl_setopt($ch, CURLOPT_POST, 1);
                                        curl_setopt($ch, CURLOPT_POSTFIELDS, "{\"text\": [\"{$row['text']}\"], \"model_id\":\"en-{$lang}\"}");
                                        curl_setopt($ch, CURLOPT_USERPWD, 'apikey' . ':' . 'jvpxmUVt2ZSJfgVWyeljAUFEoyC7COZTEr2TAkG4uAU9');

                                        $headers = array();
                                        $headers[] = 'Content-Type: application/json';
                                        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

                                        $res = curl_exec($ch);
                                        if (curl_errno($ch)) {
                                            echo 'Error:' . curl_error($ch);
                                        }
                                        curl_close($ch);

                                        $res = json_decode($res);
                                        print_r(array_values($res->translations)[0]->translation);
                                    }
                                ?>
                            </p>
                        </div>
                    </div>
            <?php   }
            }
            
            $conn->close();
        ?>
        <div style="margin-top:50px;">
            <p>Enter your comment:</p>
            <form action="get_voice.php" method="post" enctype="multipart/form-data">
                <input name="id" id="id" value=<?php echo $movie_id; ?> type="hidden">
                name:
                <input type="text" name="name" id="name">
                Select voice to upload:
                <input type="file" name="voice" id="voice">
                <input type="submit" value="Upload Voice" name="submit">
            </form>
        </div>
    </body>
</html>