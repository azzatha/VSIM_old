<!doctype html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang=""> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8" lang=""> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9" lang=""> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang=""> <!--<![endif]-->
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
        <title>VSIM Tool</title>
        <meta name="description" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="apple-touch-icon" href="apple-touch-icon.png">
        <link rel="stylesheet" href="fonts/stylesheet.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">
        <link rel="stylesheet" href="css/bootstrap.min.css">
        <!--        <link rel="stylesheet" href="assets/css/bootstrap-theme.min.css">-->
        <link rel="stylesheet" href="css/customicon.css">
        <link rel="stylesheet" href="css/linearicons.css">
        <link rel="stylesheet" href="css/animate.css">

        <!--For Plugins external css-->
        <link rel="stylesheet" href="css/plugins.css" />
        <!--Theme custom css -->
        <link rel="stylesheet" href="css/style.css">
        <!--Theme Responsive css-->
        <link rel="stylesheet" href="css/responsive.css" />
        <script src="js/vendor/modernizr-2.8.3-respond-1.4.2.min.js"></script>
    </head>
    <body>
    <?php
    #phpinfo();
   	#$target_dir = "./VSIM/";
    
    chdir('./VSIM/');
    if ($_FILES['fileToUpload1']['name']== "" ||  $_FILES['fileToUpload2']['name']== "")  {
        	echo("Please select two files to upload");
        	echo($_FILES['fileToUpload1']['name']);
        	echo($_FILES['fileToUpload2']['name']);
    }

    else {
       # $target_file= $target_dir . basename($_FILES["fileToUpload"]["name"]);
       $fileName1= $_FILES["fileToUpload1"]["name"];
 	   $fileName2= $_FILES["fileToUpload2"]["name"];
       $childNum= $_POST['childNum'];
       #print_r($fileName2);
       

       #$url= 'http://10.254.145.133/task2result.html?file='.$fileName1.'-'.$fileName2.'.json';
       #$link= "<a href=$url > http://10.254.145.133/task2result.html?file=$fileName1-$fileName2.json </a>";

       $unique_name = md5('file='.$fileName1.'-'.$fileName2.'.json'. time());
             
       $link='http://10.254.145.133/task2result.html?'.$unique_name;

       $alink='http://10.254.145.133/task2result.html?file='.$fileName1.'-'.$fileName2.".json";
      
       }
       
    ?>
        <!--[if lt IE 8]>
            <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
        <![endif]-->
		<div class='preloader'><div class='loaded'>&nbsp;</div></div>
        <header id="header" class="navbar-fixed-top">
            <div class="container">
                <div class="main_menu wow fadeInDown" data-wow-duration="2s">	
                    <nav class="navbar navbar-default">
                        <div class="container-fluid">
                            <!-- Brand and toggle get grouped for better mobile display -->
                            <div class="navbar-header">
                                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                                    <span class="sr-only">Toggle navigation</span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                    <span class="icon-bar"></span>
                                </button>
                                <a class="navbar-brand our_logo" href="#">VSIM</a>
                                <div class="call_us">
                                    <i class="fa fa-phone"></i>
                                   +966 533 422 088
                                </div>	  
                            </div>

                            <!-- Collect the nav links, forms, and other content for toggling -->
                            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">

                                <ul class="nav navbar-nav navbar-right">
                                    <li class="homeLink"><a href="index.html">HOme</a></li>
                                    <li><a href="example.html">Example</a></li>
                                    <li><a href="contact.html">Contact</a></li>
                                    <!-- <li><a href="#" style="background:#6FB048;color:#fff;border-radius:2px;padding:5px 10px;margin-top:10px;">Get Stared</a></li> -->
                                </ul>
                            </div><!-- /.navbar-collapse -->
                        </div><!-- /.container-fluid -->
                    </nav>

                </div>
            </div>
        </header>
        <!--Home page style-->

        <!-- Sections -->
        <section id="bener" class="">
            <div class="bener_overlay">
                <div class="container">
                    <div class="bener_content">
                        <h1 > Welcome to VSIM</h1>
                        <p>Visualization and Simulation of the Human Genome Diseases</p>
                        <br />
                    </div>
                </div> <!-- /container -->
            </div>
        </section>
        
        <section id="our_features_waiting">
            <div class="container">
                <div class="features_top text-center">
                    <h2 class="title_border">Your file successfully uploaded... </h2>
                    <div class="separator"></div>
                    <p id="waitpage">You will be redirected to result page in a few seconds if your file is small!
                        <br> <br>Please copy the link below to view status or results later.
                        <br> <br>  
                        <!-- <textarea id="linktext" class="js-copytextarea"><?php echo $link; ?></textarea> -->
                                                                  
                        <a id="myLink" href="<?php echo $alink; ?>"> <?php echo $link; ?></a> 				
                        <br><br>
                       <!-- <button onclick="myFunction()">Copy link</button>-->
                       <!-- <button id="linkbuton" class="js-textareacopybtn" style="vertical-align:top;">Copy Link</button>-->
                    </p>
                </div>
            </div>
        </section>
        
        <script type="text/javascript" >
           function myFunction() {
           var copyText = document.getElementById("myLink");
           copyText.select();
           document.execCommand("copy");
           alert("Copied the text: " + copyText.value);
          }
        </script>
        
        <!--Footer-->
        <footer id="footer">
            <div class="container">			
                <div class="row">
                </div>
                <div class="footer_bottom">
                    <div class="row">
						<div class="col-md-6 col-sm-6 col-xs-12">
							<div class="single_footer_bottom">
							   <p class="wow zoomIn" data-wow-duration="1s">Made with <i class="fa fa-heart"></i> </p>
							</div>
						</div>
					</div>
                </div><!-- End footer bottom -->
            </div>
        </footer>

        <script src="js/vendor/jquery-1.11.2.min.js"></script>
        <script src="js/vendor/bootstrap.min.js"></script>
        <script src="js/jquery.easing.1.3.js"></script>
        <script src="js/wow.min.js"></script>
        <script src="js/plugins.js"></script>
        <script src="js/main.js"></script>
        
        <?php
        # phpinfo();        
        $command= ('./task2.sh '. $fileName1." ".$fileName2." ".$childNum);  
        $str2= exec($command . " > /dev/null &"); 
        #file_put_contents("task2log.txt", $str2);   
        ?>
      
    </body>
</html>
