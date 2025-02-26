from fasthtml.common import *

app,rt = fast_app()

@rt('/')
def get():
    return Main(
        
    )
    
@rt('/submit')
def post(name : str):
    return f"D {name}"

serve()