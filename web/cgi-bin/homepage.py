#!/usr/bin/env python
# -*- coding: utf-8 -*-
html_body="""
<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8"></meta>
    <meta http-equiv="X-UA-Compatible" content="IE=edge"></meta>
    <meta content="width=device-width, initial-scale=1" name="viewport"></meta>
    <title>トイレ状況確認web</title>
    <!-- Bootstrap CDN -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.c
ss">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme
.min.css">
  </head>
  <body>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <div style = "text-align:center">
            <h1 style="background-color:#000080" class="text-center" id="iot"><font color="#F8F8
FF">Intelligence Business Solutions</font></h1>
            <h1 style="background-color:#000080"class="text-center" id="hello"><font color="#F8F
8FF">Internet Of Toilet!!</font></h1>
    <form action="use.py" >
    <span style="text-align: center"><input type="submit" value="1番扉使用状況" /></span
>
    <span style="text-align: center"><input type="submit" value="2番扉使用状況" /></span
>
    </form>
    <img src="../toilet.jpg" style="width:auto;height:300px;" />
        </div>
      </div>
    </div>
  </body>
</html>"""

print html_body
