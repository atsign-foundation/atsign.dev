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
  .column {
  float: left;
  width: 50%;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.row {
  display: flex;
}

.column {
  flex: 50%;
}
</style>

<script>
function copyText(){
  navigator.clipboard.writeText('flutter pub global activate at_app');
  // document.getElementById("copyIcon").toggleClass("fas fa-copy fas fa-clipboard");

  // document.getElementById("copyIcon").hasClass("fas fa-copy){
  //   document.getElementById("copyIcon").addClass("fas fa-clipboard").removeClass("fas fa-copy");
  // } else {
  //   document.getElementById("copyIcon").addClass("fas fa-copy").removeClass("fas fa-clipboard");
  // }
  
  /* Alert the copied text */
  alert("Copied text");
}
function copyText2(){
  navigator.clipboard.writeText('at_app create [...options] path/to/your/project');
  /* Alert the copied text */
  alert("Copied text");
}
</script>

Below are two columns, the left side includes steps in setting up an application that utilizes the @platform to send simple data to the right hand side which will display the simple data sent.

<div class="row">
  <div class="column" style="padding-left:15px;">
  <!-- Step 1 -->
  <h3>Create your own data sender app</h3>
  <br>
  <h4> Step 1: Install the command line toolkit (at_app) </h4>
  <pre style="height:40px; width:400px;">
  <div style="margin-left:-15px; margin-top:-50px;">
  <code>flutter pub global activate at_app</code>
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
<pre style="height: 50px; width:400px;">
  <div style="margin-left:-15px; margin-top:-50px;">
  <code>at_app create [...options] </code> 
  <div style="margin-left:-10px; margin-top:-45px;">
  <code> path/to/your/project</code>
  </div>
  </div>
  <div style="margin-top:-160px; margin-left:275px;"title="Copy to clipboard" onclick="copyText2()">
        <i id="copyIcon" class="fas fa-copy"></i>
      </div>
  </pre>
    <!-- End of Step 2 -->

<br>

  <!-- Step 3 -->

<h4> Step 3: Onboard an @sign </h4>

<img src="/Sample_Apps/croppedWT.gif" style="height:600px;">

  <!-- End of Step 3 -->

  </div>
  <!-- End of Steps column -->

  <div class="column" style="position:sticky;">
  <h3>Receive your sent data </h3>
  <b>
  Send notifications to me by following the steps on the left hand side!
  </b>
  <div style="padding-left:25px;">
  <iframe src="https://cconstab.github.io/snackbar/#/" title="Snackbar Code" style="height: 550px; width: 25vw;"></iframe>
  </div>
  </div>
