<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"] ?? '';
    $telefono = $_POST["telefono"] ?? '';
    $email = $_POST["email"] ?? '';
    $cedula = $_POST["cedula"] ?? '';

    if (!empty($nombre) && !empty($email) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $to = $email;
        $subject = "¡Bienvenido a Origen Special! Tus beneficios como Asociado te esperan";

        $message = "
        <html>
        <head>
          <title>Bienvenido a Origen Special</title>
          <style>
            body { font-family: 'Poppins', sans-serif; background-color: #f4f4f4; color: #333; margin: 0; padding: 0; }
            .container { max-width: 600px; margin: 20px auto; background-color: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
            .header { background-color: #141519; padding: 20px; text-align: center; }
            .header img { max-width: 150px; }
            .content { padding: 30px; }
            .content h1 { color: #E58D57; font-size: 24px; margin-bottom: 20px; }
            .content p { line-height: 1.6; margin-bottom: 20px; }
            .coupon { background-color: #f9f9f9; border: 2px dashed #E58D57; padding: 20px; text-align: center; border-radius: 8px; margin: 30px 0; font-size: 20px; font-weight: bold; color: #E58D57; }
            .btn { display: inline-block; background-color: #E58D57; color: #fff; padding: 15px 30px; text-decoration: none; border-radius: 50px; font-weight: bold; margin-top: 20px; }
            .footer { background-color: #f4f4f4; padding: 20px; text-align: center; font-size: 12px; color: #777; }
          </style>
        </head>
        <body>
          <div class='container'>
            <div class='header'>
              <img src='https://mercacol.com.co/wp-content/uploads/2026/03/LOGO-ORIGEN-08.png' alt='Origen Special'>
            </div>
            <div class='content'>
              <h1>¡Hola, $nombre!</h1>
              <p>Tu registro como caficultor asociado ha sido exitoso. Nos complace darte la bienvenida a nuestra alianza, donde tu Cédula Cafetera tiene más valor que nunca.</p>
              <p>Como asociado, tienes acceso a beneficios exclusivos, descuentos especiales y acumulación de puntos en todas tus compras en nuestra tienda.</p>
              <div class='coupon'>
                CUPÓN: ASOCIADO15
              </div>
              <p>Haz clic en el siguiente botón para reclamar tu descuento en tu próxima compra y comenzar a disfrutar de tus beneficios.</p>
              <div style='text-align: center;'>
                <a href='https://mercacol.com.co' class='btn'>Reclamar Descuento Ahora</a>
              </div>
            </div>
            <div class='footer'>
              <p>&copy; 2024 Origen Special | Mercacol. Todos los derechos reservados.</p>
              <p>Has recibido este correo porque te has registrado como asociado en nuestra demostración en vivo.</p>
            </div>
          </div>
        </body>
        </html>
        ";

        // Always set content-type when sending HTML email
        $headers = "MIME-Version: 1.0" . "\r\n";
        $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

        // More headers
        $headers .= 'From: Origen Special <asociados@mercacol.com.co>' . "\r\n";
        $headers .= 'Reply-To: asociados@mercacol.com.co' . "\r\n";

        mail($to, $subject, $message, $headers);
        echo "Correo enviado exitosamente.";
    } else {
        echo "Datos inválidos.";
    }
} else {
    echo "Método no permitido.";
}
?>