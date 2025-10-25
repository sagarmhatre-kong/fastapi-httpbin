#
# All requests
#

from fastapi import APIRouter
from fastapi import FastAPI, Header, Request, Response, Query, Body
from typing import Optional

from . import PrettyJSONResponse

router = APIRouter()


@router.get("/cookies", summary = "Show current cookies in the browser.",
    response_class=PrettyJSONResponse)
async def get(request: Request, response: Response):

    retval = {}
    for key, value in request.cookies.items():
        response.set_cookie(key = key, value = value)

    retval = {"message": f"{len(request.cookies)} cookies seen in request."}
    retval["cookies"] = request.cookies

    return(retval)


@router.put("/cookies", summary = "Set one or more cookies.",
    response_class=PrettyJSONResponse)
async def put(request: Request, response: Response, 
    cookies: Optional[dict] = Body(
        example = '{"cookie1": "value1", "cookie2": "value2", "cookie3": "value3"}'
    )):

    retval = {}
    for key, value in cookies.items():
        response.set_cookie(key = key, value = value)

    retval = {"message": f"{len(cookies)} {'cookie' if len(cookies) == 1 else 'cookies'} set in response."}
    retval["cookies"] = request.cookies

    return(retval)


@router.delete("/cookies", summary = "Delete one or more cookies.",
    response_class=PrettyJSONResponse)
async def delete(request: Request, response: Response, cookies: Optional[list] = Body(
    example = '["cookie1", "cookie2", "cookie3"]'
    )):

    retval = {}
    num_deleted = 0

    for key in cookies:
        if key in request.cookies:
            response.delete_cookie(key = key)
            num_deleted += 1

    retval = {"message": f"{num_deleted} {'cookie' if num_deleted == 1 else 'cookies'} deleted."}

    return(retval)




