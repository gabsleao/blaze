<?php 
require_once __DIR__ . '/classes/Utils.php';
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Predict</title>
    <!-- CSS do Bootstrap -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        /* Estilize o botão centralizado */
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
    <div class="centered-button mt-4">
        <button class="btn btn-primary" onclick="atualizaCsv();">Atualizar</button>
    </div>
    
    <?php
        if(file_exists('./dados.csv')){
            $CSV = fopen('./dados.csv', 'r');
        }
    ?>
    <div class="container mt-4">
        <h2>Dados</h2>
        <table class="table table-bordered">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Identifier</th>
                    <th>Number</th>
                    <th>Color</th>
                </tr>
            </thead>
            <tbody>
                <?php
                if(isset($CSV)){
                    $AllLines = Utils::getAllLinesFromCSV($CSV);
                    foreach($AllLines as $Line){
                        echo $Line;
                    }
                }
                ?>
            </tbody>
        </table>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
</body>
</html>

<script>
    function atualizaCsv(){
        $.post("./run_script.php", function( data ) {
            window.location.reload();
        });
    }
</script>