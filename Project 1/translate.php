<?php
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, 'https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/b5676fb3-c5f7-41ee-a74d-925d805c4df7/v3/translate?version=2018-05-01');
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
    $text = "Hello world.";
    curl_setopt($ch, CURLOPT_POSTFIELDS, "{\"text\": [\"{$text}\"], \"model_id\":\"en-it\"}");
    curl_setopt($ch, CURLOPT_USERPWD, 'apikey' . ':' . 'jvpxmUVt2ZSJfgVWyeljAUFEoyC7COZTEr2TAkG4uAU9');

    $headers = array();
    $headers[] = 'Content-Type: application/json';
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

    $result = curl_exec($ch);
    if (curl_errno($ch)) {
        echo 'Error:' . curl_error($ch);
    }
    curl_close($ch);
    print_r($result);
?>