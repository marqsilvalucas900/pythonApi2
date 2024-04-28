from flask import Flask, url_for

app = Flask(__name__)
app.config["APP_NAME"] = "Meu Blog"




@app.route("/")
def index():
    content_url = url_for("read_content", title="Novidades")
    return (
        f"{app.config['APP_NAME']}"
        f"<a href= '{content_url}'>Novidades de 2022</a>"
        "<hr>"
    )

#app.register_error_handler(404,not_found_page)



@app.route("/<title>")
def read_content(title):
    index_url = url_for("index")
    #print(url_for("index")) #só pode ser imprimido em contexto de aplicação
    return f"<h1>{title}</h1> <a href='{index_url}'>Voltar</a>"

if __name__ == "__main__":
    app.run()