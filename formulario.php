<?php

$emailUsuario = $_POST['emailUsuario'];
$password = $_POST['password'];

if ($emailUsuario === 'emailUsuario' && $password === 'password') {
  header('Location: index.html');
} else {
  echo 'El nombre de usuario o la contraseña son incorrectos.';
}

?>
