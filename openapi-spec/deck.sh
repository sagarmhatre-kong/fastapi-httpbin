
# Change directory to the OpenAPI spec folder
cd fastapi-httpbin/openapi-spec

# Convert the OpenAPI specification (openapi.yaml) to Kong configuration (kong.yaml)
deck file openapi2kong -s openapi.yaml -o kong.yaml

# This script interacts with a Kong API Gateway using the 'deck' CLI tool.
# 1. Checks connectivity to the Kong Gateway at the specified address.
deck gateway ping --kong-addr http://localhost:8001
# 2. Shows the difference between the current gateway configuration and 'kong.yaml' using the 'openapi' workspace.
deck gateway diff kong.yaml -w openapi
# 3. Synchronizes the gateway configuration with 'kong.yaml' in the 'openapi' workspace.
deck gateway sync kong.yaml -w openapi