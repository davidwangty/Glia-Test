import random
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    excuses = [
        "It was working in my head",
        "I thought I fixed that",
        "Actually, that is a feature",
        "It works on my machine",
    ]

    output = """
<!DOCTYPE HTML>
<html style="height: 100%">
<head>
 <title>Clone of Excuses For Lazy Coders</title>
</head>
<body style="height: 100%; background-color: black">
 <div class="wrapper" style="min-height: 100%; height: auto !important; height: 100%; margin: 0 auto -8em;">
  <center style="color: #333; padding-top: 200px; font-family: Courier; font-size: 24px; font-weight: bold;"><a href="/" rel="nofollow" style="text-decoration: none; color: white;">{excuse}</a></center>
  <div class="push"></div>
 </div>
 <div class="footer">
  <center style="color: white; font-family: Courier; font-size: 11px;">
   <br /><br />&copy; Copyright 2012 - 2015 programmingexcuses.com - All Rights Reserved 
  </center>
 </div>
 </body>
</html>
    """.format(excuse=random.choice(excuses))

    return HttpResponse(output)
