import os
path = r"C:\Users\CCrowe\Documents\Modern Software Methodologies\Quiz 2"
folder = os.path.join(path,"Files")
files = os.listdir(folder)
html_path = os.path.join(path,"Study_Sheet.html")
print(os.path.exists(html_path))
html = open(html_path,"w")
html.write("""
<head>
  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.5.2/css/bulma.css">
<script src="https://unpkg.com/masonry-layout@4/dist/masonry.pkgd.js"></script>
<script
  src="https://code.jquery.com/jquery-3.2.1.js"
  integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE="
  crossorigin="anonymous"></script>
<style>
div {
font-size:40%;
}
article {
float:left;
max-width:500px;
max-height:100px;
}
body {
{
  margin: 0px;
  padding: 0px;
  width: 670px; /* width: 7in; */
  height: 900px; /* or height: 9.5in; */
  clear: both;
  background-color: gray;
  page-break-after: always;
}
}
</style>
</head>
<body>
<script>
$('.grid').masonry({
  // options...
  itemSelector: '.grid-item',
  columnWidth: 200
});
</script>
""")
for file_name in files:
    file_path = os.path.join(path,"Files",file_name)
    f =  open(file_path)
    text = """
<article class="message is-dark" style="{3}">
  <div class="message-body" style="{2}">
  <p></p>
   <strong>{0}</strong> -- {1}
  </div>
</article>
""".format(file_name.strip().replace(".txt",""),f.read().strip().replace("-","&#9679;"),"white-space: normal;padding:0px;display: block;","margin:0px;","padding:0px;")
    html.write(text)
html.write("""
</body>
""")
#pre-wrap
