<!doctype html>
<?php
if (isset($_POST["Login"])){
$user = $_POST["username"];
$pass = $_POST["password"];
if($user=="parent"&&pass=="parent"){
header( 'Location: parent_home.php' );
}
echo("error");
}
?>
<html>
<head>
    <meta charset="utf-8">
<title>Login Form </title>
    
    <style>
    body{
    margin: 0;
    padding: 0;
    background: url(music.jpg);
    background-size: cover;
    background-position: center;
    font-family: sans-serif;
}

.loginbox{
    width: 320px;
    height: 420px;
    background: #000;
    color: #fff;
    top: 50%;
    left: 50%;
    position: absolute;
    transform: translate(-50%,-50%);
    box-sizing: border-box;
    padding: 70px 30px;
}

.avatar{
    width: 100px;
    height: 100px;
    border-radius: 50%;
    position: absolute;
    top: -50px;
    left: calc(50% - 50px);
}

h1{
    margin: 0;
    padding: 0 0 20px;
    text-align: center;
    font-size: 22px;
}

.loginbox p{
    margin: 0;
    padding: 0;
    font-weight: bold;
}

.loginbox input{
    width: 100%;
    margin-bottom: 20px;
}

.loginbox input[type="text"], input[type="password"]
{
    border: none;
    border-bottom: 1px solid #fff;
    background: transparent;
    outline: none;
    height: 40px;
    color: #fff;
    font-size: 16px;
}
.loginbox input[type="submit"]
{
    border: none;
    outline: none;
    height: 40px;
    background: #fb2525;
    color: #fff;
    font-size: 18px;
    border-radius: 20px;
}
.loginbox input[type="submit"]:hover
{
    cursor: pointer;
    background: #ffc107;
    color: #000;
}
.loginbox a{
    text-decoration: none;
    font-size: 12px;
    line-height: 20px;
    color: darkgrey;
}

.loginbox a:hover
{
    color: #ffc107;
}
        .form button{
            font-family: "Robto",sans-serif;
            text-transform: uppercase;
            outline: 0;
            background: #fb2525;
            width:100%;
            border: 0;
            padding: 15px;
            color: #FFFFFF;
            font-size: 14px;
            cursor: pointer;
        }
    
        ////////      
        nav{
         width:100%;
            background: #FFFFFF;
            height: 80px;
            margin-top: 0px;
            
        }
        
        ul{
            list-style:none;
            padding: 0;
            margin: 0 0 0 475px;
        }
        li{
            float: left;
    
        }
        
       nav a{
            display: block;
            text-decoration: none;
            font-size: 20px;
            text-align: center;
            padding:  15px 15px;
            font-family: Arial;
            font-weight:bold; 
        }
        a:hover{
           
            transition: 0.6s;
            opacity: 0.5;
        }
        .logo img{
            position: absolute;
            margin-top: 10px;
            margin-left: 10px;
        }
        
    </style> 
    
    </head>
 
    
   
    
    
<body>
    
          <div class ="logo"><a href ="#"><img src ="logo.png"></a>
        </div> 
        
    <nav>
        <ul>
            <li><a href ="#"><h1>PINELAND MUSIC SCHOOL</h1></a></li>
    <li><a href ="about.html">About us</a></li>
    <li><a href ="contact.html">contact</a></li>
    
    
        </ul>
        </nav>
    
    <div class="loginbox">
    <img src="avatar.png" class="avatar">
        
        <h1>Login Here</h1>
        <form>
            <p>Username:</p>
            <input type="text" name="username" placeholder="Enter Username">
                
            <p>Password</p>
            <input type="password" name="password" placeholder="Enter Password">
               

            <input type="submit"  name="Login" value="Login">
    
        <a href="#">forgot password?</a><br>
            Not Registered?<a href="signup.html"><input type="button" value="REGISTER" /</a></form></div>

</body>
</html>