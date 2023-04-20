<?php

	$email = $password = "";

	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		$email = test_input($_POST["emailUsuario"]);
		$password = test_input($_POST["password"]);

		// Aquí iría el código para procesar el formulario, como enviar un correo electrónico o guardar los datos en una base de datos

		echo "¡Gracias por enviar el formulario!";
	}


	function test_input($data) {
		$data = trim($data);
		$data = stripslashes($data);
		$data = htmlspecialchars($data);
		return $data;
	}


?>