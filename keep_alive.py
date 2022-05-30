from flask import Flask, render_template
from threading import Thread

app = Flask('')

DuckHTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <title>&#128994; Duckbot - status</title>

  <body class="d-flex h-100 text-center text-white bg-dark">
    
<div style="padding-top: 200px!important;" class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
  <header class="mb-auto">
    <div>
      <h3 style="padding: 20px;" class="mb-0">Duckbot <span class="badge bg-success">Online</span></h3>
      <nav class="nav nav-masthead justify-content-center float-md-end">
      </nav>
    </div>
  </header>

<img style="width: 200px; height: 200px; display:flex; justify-content:center;" src="https://giffiles.alphacoders.com/208/208354.gif" class="img-thumbnail mx-auto" alt="Responsive image">

  <main class="px-3">
    <h1>Thanks for checking up on Duckbot ! :)</h1>
    <p class="lead blockquote">“Ducks are one of the smallest types of waterfowl…often the most colorful.”</p>
  </main>

  <footer class="mt-auto text-white-50">
    <p>Duckbot made by <a target="_blank" href="https://github.com/cyberwizard-v" class="text-white">@Cyberwizard-V</a></p>
  </footer>
</div>
</body>
</head>
</html>

"""

@app.route('/')
def main():
  return DuckHTML

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
