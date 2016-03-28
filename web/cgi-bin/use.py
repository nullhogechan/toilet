#!/usr/bin/env python
# -*- coding: utf-8 -*-
str = "/var/log/toilet/door_use.log"
f = open(str,"r")
for row in f:
	if int(row) == 0:
		print "Content-type: text/html\n"
		print """
			<!DOCTYPE html>
			<html lang="ja">
			  <head>
			    <meta charset="utf-8"></meta>
			    <meta http-equiv="X-UA-Compatible" content="IE=edge"></meta>
			    <meta content="width=device-width, initial-scale=1" name="viewport"></meta>
			    <title>トイレ状況確認web</title>
			  </head>
			  <body>
			    <div class="container-fluid">
			      <div class="row">
			        <div class="col-sm-12">
			          <div style = "text-align:center">
				    <div style="background:">
				      <img src="../kansha_01.jpg">
			         <h1 style="background-color:#000080" class="text-center" id="iot"><font color="#F8F8FF">現在空いております</font></h1>
                                    </div>
			          </div>
			        </div>
			      </div>
			    </div>
			  </body>
			</html>"""
	else:
		print "Content-type: text/html\n"
		print """
                        <!DOCTYPE html>
                        <html lang="ja">
                          <head>
                            <meta charset="utf-8"></meta>
                            <meta http-equiv="X-UA-Compatible" content="IE=edge"></meta>
                            <meta content="width=device-width, initial-scale=1" name="viewport"></meta>
                            <title>トイレ状況確認web</title>
                          </head>
                          <body>
                            <div class="container-fluid">
                              <div class="row">
                                <div class="col-sm-12">
                                  <div style = "text-align:center">
                                    <div style="background:">
                                      <img src="../rainy.jpg">
                                       <h1 style="background-color:#000080" class="text-center" id="iot"><font color="#F8F8FF">現在使用中です</font></h1>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </body>
                        </html>"""

