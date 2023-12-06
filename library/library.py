
from fastapi import FastAPI,Request,Form,UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,FileResponse


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return HTMLResponse(content="""
    <h1>Welcome to my site</h1>
    <form action="/submit" method="post">
        <input type="text" name="input_text" required>
        <input type="submit" value="Submit">
    </form>
    """, media_type="text/html")
@app.post("/submit")
def handle_submit(request: Request, input_text: str = Form(...)):
        return HTMLResponse(content="""
        <h1>Welcome to our library</h1>
       <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">

  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="/">Home</a>
      </li>
        <li class="nav-item">
                <a class="nav-link" href="login">Login</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="register">Register</a>
            </li>
     <li class="nav-item dropdown {% if 'store' in request.path %} active {% endif %}">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                   aria-expanded="false">
                    Books
                </a>
                <ul class="dropdown-menu">

                    <li><a class="dropdown-item" href="https://en.wikipedia.org/wiki/ Tools of Titans"> Tools of Titans</a></li>
                    <li><a class="dropdown-item" href="https://en.wikipedia.org/wiki/Rich Dad Poor Dad">Rich Dad Poor Dad</a></li>
                    <li><a class="dropdown-item" href="https://en.wikipedia.org/wiki/ The Labyrinth of Spirits"> The Labyrinth of Spirits</a></li>
                    <li><a class="dropdown-item" href="https://en.wikipedia.org/wiki/ The 7 Habits of Highly Effective People"> The 7 Habits of Highly Effective People</a></li>
                    <li><a class="dropdown-item" href="https://en.wikipedia.org/wiki/The Picture of Dorian Gray">The Picture of Dorian Gray</a></li>



                </ul>
            </li>
        <li class="form-inline my-2 my-lg-0">
                <a class="nav-link" href="logout">Logout</a>
            </li>


    </ul>

  </div>
    </div>
</nav>
        """, media_type="text/html")

@app.get("/")
def home_root():
    return HTMLResponse(content="""
{% extends 'base.html' %}
{% load static %}
{% block content %}
<div>
    <img class="my_image my_image_padding" src="/static/img/ban.png" width="1200px;" height="250px;">
</div><br>


    </form>
<div>
    <h1 class="text-center my_title">College Library</h1>
    <p class="text-center my_title">College library mainly for students. </p>
</div>


{% endblock %}

        """, media_type="text/html")

@app.get("/login")
def login_root():
    return HTMLResponse(content="""
    <h1>Login</h1>
    <style>
body{
   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
* {box-sizing: border-box}
input[type=text], input[type=password] {
   width: 100%;
   font-size: 16px;
    padding: 14px;
   margin: 5px 0 4px 0;
   display: inline-block;
   border: none;
   background: #f1f1f1;
}
label{
   font-size: 15px;
}
input[type=text]:focus, input[type=password]:focus {
   background-color: #ddd;
   outline: dark;
}
hr {
   border: 1px solid #f1f1f1;
   margin-bottom: 25px;
}
.button {
   font-size: 18px;
   font-weight: bold;
   background-color: pink;
   color: white;
   padding: 13px 20px;
   margin: 6px 0;
   border: none;
   cursor: pointer;
   width: 100%;
   opacity: 0.9;
}
.button:hover {
   opacity:1;
}
.button1:hover {
   opacity:1;
}

.formContainer {
   padding-right:400px;
    padding-left: 400px;
    padding-top: 111px;
}
.button1 {
   font-size: 18px;
   font-weight: bold;
   background-color: ash;
   color: white;
    padding: 13px 20px;
   margin: 6px 0;
   border: none;
   cursor: pointer;
   width: 100%;
   opacity: 0.9;
}
.msg{
text-align:center
}

</style>
        <form method="post" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            <br>
            
        
    <li class="nav-item">
           <input class="button" type="button" value="Login"></a><br>
            <p>Don't have an account? <a href="/register/">Register</a></p>

            </li>
            </form>
        """, media_type="text/html")


@app.get("/register")
def register_root():
        return HTMLResponse(content="""
        <h1>Register</h1>
            <style>
body{
   font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
* {box-sizing: border-box}
input[type=text],input[type=email], input[type=password] {
   width: 100%;
   font-size: 16px;
   padding: 10px;
   margin: 5px 0 4px 0;
   display: inline-block;
   border: none;
   background: #f1f1f1;
}
label{
   font-size: 15px;
}
input[type=text]:focus, input[type=password]:focus ,input[type=email]:focus{
   background-color: #ddd;
   outline: none;
}
hr {
   border: 1px solid #f1f1f1;
   margin-bottom: 25px;
}
.button {
   font-size: 18px;
   font-weight: bold;
   background-color: rgb(10, 100, 13);
   color: white;
   padding: 10px 20px;
   margin: 6px 0;
   border: none;
   cursor: pointer;
   width: 100%;
   opacity: 0.9;
}
.button:hover {
   opacity:1;
}
.button1:hover {
   opacity:1;
}

.formContainer {
   padding-right: 360px;
    padding-left: 360px;
    padding-bottom:-400px;
}
.button1 {
   font-size: 18px;
   font-weight: bold;
   background-color: rgb(119, 10, 13);
   color: white;
   padding: 10px 20px;
   margin: 6px 0;
   border: none;
   cursor: pointer;
   width: 100%;
   opacity: 0.9;
}


    </style>
    <form method="post" action="/register">
        <input type="text" name="username" placeholder="Enter Your username"><br>

        <input type="text" name="first_name" placeholder="Enter Your first_name"><br>

        <input type="text" name="last_name" placeholder="Enter Your last_name"><br>

        <input type="email" name="email" placeholder="Enter email"><br>

        <input type="password" name="password" placeholder="Enter Your password"><br>

        <input type="password" name="cpassword" placeholder="Confirm password"><br>
        <li class="nav-item">
          <a href="/login/"> <input class="button" type="button" value="Register"></a><br>

            </li>
        <a href="/"> <input class="button1" type="button" value="Cancel"></a><br>
    </div>
</form>
        
        """, media_type="text/html")






# @app.post("/login")
# def login_root(request: Request, input_text: str = Form(...)):
#     return HTMLResponse(content="""
#      <form action="/login" method="post">
#
#     <div class="formContainer">
#         <h2 style="color:black;text-align:center;padding:10px">Login</h2>

#
#     <input type="text" name="username" placeholder="Enter Your username"><br>
#
#     <input type="password" name="password" placeholder="Enter Your password"><br>
#
#         <li class="nav-item">
#           <a href="/form/"> <input class="button" type="button" value="Login"></a><br>
#             <p>Don't have an account? <a href="/register/">Register</a></p>
#
#             </li>
#
# </div>
# </form>

