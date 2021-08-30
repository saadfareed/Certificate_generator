<h1 align="center">How you make this code feasible for your Template?</h1>
<br>
<p>
1:copy your template of certificate in the same directory where you find Template.jpeg.
</p>
<br>
<p>
2:Make sure you name it Template.jpeg if you don't then you have to change im = Image.open(r'Template.jpg') to im = Image.open(r'name of your template with extension')
</p>
<br>
<p>
3:if you want to change font you have to first download font <a href="https://www.1001fonts.com/signature-fonts.html?page=2">Download Font from here!</a>

</p>
<br>
<p>
4: Which font do you change if you want to change font used for attendees name you should change fon = ImageFont.truetype("arial.ttf", 60) to 
  fon = ImageFont.truetype("font you want to use", size of font)
</p>
<br>
<p>
5: And if you want to change font used for Signatures you should change fox = ImageFont.truetype("PWSignaturetwo.ttf", 50) to 
  fox = ImageFont.truetype("font you want to use", size of font)
</p>
<hr>
<h2 align="center">Next Steps are How you Run the code?</h2>
<h3>Dependencies Installation:</h3>
<p>
  1;install python3 (I am using python 3.7.6)
  </P>
  <p>
  2;pip install pandas
  </p>
  <p>
  3:pip install os
  </p>
  <p>
  4:pip install PIL
  </p>
  <br>
<h3>Run code:</h3>
<p>python Certificate_Generator.py</p>
<hr>
<h2>Output:</h2>
