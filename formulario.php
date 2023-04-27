<?php

$emailUsuario = $_POST['emailUsuario'];
$password = $_POST['password'];

if ($emailUsuario === 'emailUsuario' && $password === 'password') {
  header('Location: index.php');
} else {
  echo 'El nombre de usuario o la contraseña son incorrectos.';
}

?>
