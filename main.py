from starlite import Starlite, get


@get("/")
async def index() -> dict[str, str]:
    return {"hello": "Artemii"}


app = Starlite(route_handlers=[index])
