<?php include 'connect.php';?>
<?php
    $movie_id = $_POST['id'];
    $user = $_POST['name'];
    $movie_name = $_FILES['voice']['name'];

    $array = explode('.', $movie_name);
    $extension = end($array);

    $target_file = basename($_FILES["voice"]["name"]);
    move_uploaded_file($_FILES["voice"]["tmp_name"], $target_file);
    
    $file = file_get_contents($movie_name);
    $url = 'https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/a9448389-8650-4e83-8290-79a68b2b3c89/v1/recognize';
    $model = 'en-US_BroadbandModel';
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url . '?model=' . $model);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $file);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_USERPWD, 'apikey' . ':' . 'RTCLeytnFIJM8NFHlYVMuerc_YxIQSrfVEuOf_RXoywT');
    $headers = array();
    $headers[] = "Content-Type: audio/{$extension}";
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Error:' . curl_error($ch);
    }
    curl_close($ch);
    $res = json_decode($result);
    $text = array_values(array_values($res->results)[0]->alternatives)[0]->transcript;

    print_r($text);
    echo '<br/>';

    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, 'https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/bbd61956-bbb6-47e8-94dd-c4fe9831540c/v1/analyze?version=2019-07-12');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt($ch, CURLOPT_POSTFIELDS, "{\n  \"text\": \"{$text}\",\n  \"features\": {\n    \"sentiment\": {\n      \"targets\": []\n    },\n    \"keywords\": {\n      \"emotion\": true\n    }\n  }\n}");
    curl_setopt($ch, CURLOPT_USERPWD, 'apikey' . ':' . '9TDeN9zmIaxViMDHssXlZxHCzM7X_KRHGKU5b80b9SWA');

    $headers = array();
    $headers[] = 'Content-Type: application/json';
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Error:' . curl_error($ch);
    }
    curl_close($ch);
 
    $res = json_decode($result);
    print_r($result);
    $text_array = $res->keywords;
    
    $is_anger = false;

    foreach($text_array as $item) {
        $emotion = $item->emotion;
        print_r($emotion);
        echo '<br/>';
        $anger = $emotion->anger;
        print_r($anger);
        if ($anger > 0.5) {
            $is_anger = true;
        }
    }
    
    if (!$is_anger) {
        
        $sql = "INSERT INTO `comment` (`movie_id`, `text`, `user`) VALUES ('$movie_id', '$text', '$user')";

        if ($conn->query($sql) === TRUE) {
            echo "New record created successfully";
        } else {
            echo "Error: " . $sql . "<br>" . $conn->error;
        }
    }
?>