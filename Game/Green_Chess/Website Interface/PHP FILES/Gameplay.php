<html>
 <body>
  <head>
   <title>
     run
   </title>
  </head>

   <form method="post">

    <input type="submit" value="GO" name="GO">
   </form>
 </body>
</html>

<?php
  if(isset($_POST['GO']))
  {
    shell_exec("python-chess-master\ py chess_gui.py");
    echo"success";
  }
?>