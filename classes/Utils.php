<?php

class Utils{


    public static function getAllLinesFromCSV($CSV){
        $Result = [];
        while (($Linha = fgetcsv($CSV, 1000, ',')) !== false) {
            for ($i = 0; $i < count($Linha); $i++) {
                if(in_array($Linha[1], ['identifier', 'number', 'color'])){
                    continue;
                }
                $Result[] = $Linha[$i];
            }
        }
        fclose($CSV);

        return $Result;
    }
}