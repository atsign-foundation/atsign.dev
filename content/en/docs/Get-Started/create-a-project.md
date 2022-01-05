---
title: "Try your own @platform project"
SEOtitle: "Try an @platform (at_platform or AtPlatform) project"
linkTitle: "Try the @platform"
Description: "Seeing the @platform in action with the Snackbar application"
content: "What to do after creating your own @sign"
weight: 1
date: 2021-12-12
---

<style>
  .receiver{
  height: 550px; 
  width: 25vw;
}

@media only screen and (min-width: 600px){
.content{
  row-gap:20px;
  display:grid;
  grid-template-areas:"header header" "left right";
  grid-template-columns:1fr 1fr;
}
.header{
  grid-area:header;
}

.left{
  grid-area:left;
}

.right{
  grid-area:right;
  position: -webkit-sticky;
  position: sticky;
  top: 4em;
  align-self:start;
}
}

@media only screen and (max-width: 600px){
  .receiver{
  height: 550px; 
  width: 100%;
}
}

</style>

<div class="content">

 <div class="header">
 Below are two columns, the left side includes steps in setting up an application that utilizes the @platform to send simple data to the right hand side which will display the simple data sent.
 </div>

 <div class="right">
  <div>
  <center>
  <h3>Receiver </h3>
  
  <iframe src="https://cconstab.github.io/snackbar/#/" title="Snackbar Code" class="receiver"></iframe>
  
  </center>
  </div>

 </div>

 <div class="left">
<!-- Step 1 -->
  <h3>Create your own data sender app</h3>
  <br>
  <h4> Step 1: Install the command line toolkit (at_app) </h4>
  <pre style="height:40px; width:400px;overflow:hidden;">
  <div style="margin-left:-15px; margin-top:-50px;">
  <code style="overflow:hidden;">flutter pub global activate at_app</code>
  </div>
  <div style="margin-top:-105px; margin-left:275px;"title="Copy to clipboard" onclick="copyText()">
        <i id="copyIcon" class="fas fa-copy"></i>
      </div>
  </pre>
  <!-- End of Step 1 -->

  <br>

  <!-- Step 2 -->

<h4> Step 2: Create the project </h4>
Using code format (Read more on at_app <a href="https://pub.dev/packages/at_app/example" target=_blank>here</a>):
<pre style="height: 40px; width:400px; overflow:hidden;">
  <div style="margin-left:-15px; margin-top:-50px;">
  <code> at_app create -d snackbar_sender ... </code>
  <!-- </div> -->
  </div>
  
  <div style="margin-top:-125px; margin-left:275px;"title="Copy to clipboard" onclick="copyText2()">
        <i id="copyIcon2" class="fas fa-copy"></i>
      </div>
  </pre>
   <b> Note: </b>  Replace "..." with the folder you wish to create your project in.
   <br>
    <!-- End of Step 2 -->

<br>

  <!-- Step 3 -->

<h4> Step 3: Onboard an @sign </h4>
Watch the GIF below to see how to get a free @sign within the app itself! If you'd like to purchase an @sign or would simply like to create and receive any type of @sign on the website, feel free to go to <a href="https://my.atsign.com/go">atsign.com</a>.
<br></br>

<img src="/Sample_Apps/croppedWT.gif" style="height:600px;">

  <!-- End of Step 3 -->

  <!-- Step 4 -->

<br></br>

  <h4>Step 4: Send a snack! </h4>
  Enter an @sign that will receive the sent snack. Be sure that it is the same @sign that you have entered in the receiver on the right hand side of this screen! 
  </div>
  <!-- End of Steps column -->

</div>

<script>
function copyText(){
  navigator.clipboard.writeText('flutter pub global activate at_app');
  toggleIcon("copyIcon");
  window.setTimeOut(() => toggleIcon("copyIcon"), 500);

}
function copyText2(){
  navigator.clipboard.writeText('at_app create -d snackbar_sender ...');
  toggleIcon("copyIcon2");
}

function toggleIcon(className){
  let el = document.getElementById(className);
  el.classList.toggle("fa-copy");
  el.classList.toggle("fa-check");
}
</script>
