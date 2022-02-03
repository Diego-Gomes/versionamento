from fastapi import FastAPI
from fastapi_versioning import VersionedFastAPI

import config

app = FastAPI(title="API Example de versionamento")

BASE_PATH_HTTP = "/versionamento" 

API_VERSION = "v1.0.1"

app = config.configurar_rotas(app)

app = VersionedFastAPI(app,
    version_format='{major}',
    prefix_format=f"{BASE_PATH_HTTP}"+"/v{major}",
    description='API Example de versionamento')