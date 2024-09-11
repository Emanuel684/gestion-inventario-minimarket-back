"""Módulo principal donde se inicia la aplicación."""

# External libraries
import os
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title='Api Reactores', version='1.0.0')

origins = ['http://localhost:4200']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


for root, dirs, files in os.walk('controllers'):
    if '__' not in root:
        path = root.split(os.sep)
        for file in files:
            if '__' not in file:
                file, _ = os.path.splitext(file)
                path_import = f'{".".join(path)}.{file}'
                module = __import__(
                    path_import, globals(), locals(), [f'{file}_controller']
                )
                router = getattr(module, f'{file}_controller')
                app.include_router(router)


if __name__ == '__main__':
    uvicorn.run(app)
