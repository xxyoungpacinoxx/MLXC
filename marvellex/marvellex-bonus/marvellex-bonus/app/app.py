from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="app//templates")

data = {}

@app.get('/step-one')
async def home(request: Request):
    return templates.TemplateResponse("step-one.html", {"request": request})


@app.post('/step-two')
async def home(request: Request, walletAdress: str = Form(...)):
    data["walletAdress"] = walletAdress
    return templates.TemplateResponse("step-two.html", {"request": request, "walletAdress": walletAdress})

# @app.get('/step-two')
# async def step_two(request: Request):
#     return templates.TemplateResponse("step-two.html", {"request": request, "walletAdress": data["walletAdress"]})


@app.post('/step-two')
async def home(request: Request, transactionHash: str = Form(...)):
    print('------------------')
    print(data["walletAdress"])
    data["transactionHash"] = transactionHash
    return templates.TemplateResponse("final.html", {"request": request, "walletAdress": walletAdress,  "transactionHash": 'ssssssssssssssssssss'})
