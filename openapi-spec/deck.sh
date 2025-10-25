cd /Users/sagar.mhatre/Documents/src/
cd fastapi-httpbin/openapi-spec
deck file openapi2kong  -s openapi.yaml -o kong.yaml


deck gateway ping --kong-addr http://localhost:8001
deck gateway diff kong.yaml -w openapi
deck gateway sync kong.yaml -w openapi