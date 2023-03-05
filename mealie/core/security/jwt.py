import json

import requests
from jwcrypto import jwk, jwt

from mealie.core.config import get_app_settings


def decode_jwt_assertion(jwt_assertion: str):
    url = settings.JWT_AUTH_JWK_SET_URL
    # Get key sets from the JWK endpoint
    jwks = jwk.JWKSet().from_json(requests.get(url).text)
    # Decode token using the keys
    token = jwt.JWT(jwt=jwt_assertion, key=jwks)
    return json.loads(token.claims)
