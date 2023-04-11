<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
	$emailUsuario = $_POST["emailUsuario"];
	$password = $_POST["password"];

	// Aquí iría el código para procesar el formulario, como enviar un correo electrónico o guardar los datos en una base de datos

	echo "¡Gracias por enviar el formulario!";
}
?>