<?php

$emailUsuario = $_POST['emailUsuario'];
$password = $_POST['password'];

// Comprobar si el usuario y la contraseña son correctos
if ($emailUsuario === 'emailUsuario' && $password === 'password') {
  // Si son correctos, redirigir al usuario a la página de inicio
  header('Location: index.php');
  exit;
} else {
  // Si no son correctos, mostrar un mensaje de error
  echo 'El nombre de usuario o la contraseña son incorrectos.';
}

?>
