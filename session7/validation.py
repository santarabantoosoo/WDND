import json
from jose import jwt
from urllib.request import urlopen

AUTH0_DOMAIN = 'DOMAIN_HERE'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'API_AUDIENCE_HERE'


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9UQjV5SW1zcXotNHlBcU1uQjFpQyJ9.eyJpc3MiOiJodHRwczovL3RlbmFudDkyLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMDcxMTQ0NDk5MTM2NzE4MTQ1NCIsImF1ZCI6WyJpbWFnZSIsImh0dHBzOi8vdGVuYW50OTIuZXUuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTU5OTg5OTU5MCwiZXhwIjoxNTk5OTA2NzkwLCJhenAiOiJxajlqbzEzVWZRbHhhNkY3cFFrYVJYRkdnNUZzZUpqUSIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwifQ.D3-zRcoYZNFw8d21Hg7H9KbAikw__OqJkW0-cBb532ohbN3gWlWC-OhilhGlyWcOg63n6XEeCXe3-QWLxvNPFQWW1QS1XtNQjTxjhIBdli64jgPUFGamAOM5EQpvffjtdYnsdltK1uCIFW-Uyn_bmlKFTF9kRiVzpolDqgqZh0wb3BowcIp2qlqGrQYkVqUEHUQZGzwljBjh1j8aY4v_L5JkNKnzUPIG032kgE0jYlNZd-0UpYNTuZsIepKu2YyHudnALe6HOXQCaYPHk2dQ3SO4AzSgNye4W7Q3Y7hs40kaSC74HwfOQM1OyYwLnlIwr73uhpVY4v5RQxdWN593bA'

# Auth Header


def verify_decode_jwt(token):
    # GET THE PUBLIC KEY FROM AUTH0
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())

    # GET THE DATA IN THE HEADER
    unverified_header = jwt.get_unverified_header(token)

    # CHOOSE OUR KEY
    rsa_key = {}
    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed.'
        }, 401)

    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }

    # Finally, verify!!!
    if rsa_key:
        try:
            # USE THE KEY TO VALIDATE THE JWT
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload

        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)

        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
    raise AuthError({
        'code': 'invalid_header',
                'description': 'Unable to find the appropriate key.'
    }, 400)


verify_decode_jwt(token)
