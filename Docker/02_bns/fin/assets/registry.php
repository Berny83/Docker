<?php
	echo "Hello World";
	$a_bool = true;
	echo "String: $a_bool";
	echo "<br />";
	echo PHP_VERSION;
	echo 'String: $a_bool';
	echo "<br />";

	$arr = array(1, 2, 3, 4);
	foreach ($arr as $value) {
		$value = $value * 2;
		print("$value\n");
	}
	echo "<br />";

	$array = array(array(12, 4.46, "steam"), array("Example"), array(45, "strong"));

	for ($i = 0; $i < count($array); $i++) {
		for ($j = 0; $j < count($array[$i]); $j++) {
			echo $array[$i][$j]." | ";
		}
		echo "<br />";
	}
?>
