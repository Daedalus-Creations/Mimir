import os


def getenv_boolean(var_name, default_value=False):
    result = default_value
    env_value = os.getenv(var_name)
    if env_value is not None:
        result = env_value.upper() in ("TRUE", "1")
    return result


API_V1_STR = "/api"

SECRET_KEY = os.getenvb(b"SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 8  # 60 minutes * 24 hours * 8 days = 8 days

SERVER_NAME = os.getenv("SERVER_NAME")
SERVER_HOST = os.getenv("SERVER_HOST")
BACKEND_CORS_ORIGINS = os.getenv(
    "BACKEND_CORS_ORIGINS"
)  # a string of origins separated by commas, e.g: "http://localhost, http://localhost:4200, http://localhost:3000, http://localhost:8080, http://local.dockertoolbox.tiangolo.com"
PROJECT_NAME = os.getenv("PROJECT_NAME")
SENTRY_DSN = os.getenv("SENTRY_DSN")

POSTGRES_SERVER = os.getenv("POSTGRES_SERVER")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
)

SMTP_TLS = getenv_boolean("SMTP_TLS", True)
SMTP_PORT = None
_SMTP_PORT = os.getenv("SMTP_PORT")
if _SMTP_PORT is not None:
    SMTP_PORT = int(_SMTP_PORT)
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
EMAILS_FROM_EMAIL = os.getenv("EMAILS_FROM_EMAIL")
EMAILS_FROM_NAME = PROJECT_NAME
EMAIL_RESET_TOKEN_EXPIRE_HOURS = 48
EMAIL_TEMPLATES_DIR = "/app/app/email-templates/build"
EMAILS_ENABLED = SMTP_HOST and SMTP_PORT and EMAILS_FROM_EMAIL

FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")

USERS_OPEN_REGISTRATION = getenv_boolean("USERS_OPEN_REGISTRATION")

EMAIL_TEST_USER = "test@example.com"


GOOGLE_CLIENT_ID = "1007436511433-1o329ffhgodf6ipbmgqm99r2kkjsoj9u.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRETS_JSON = "client_secret_1007436511433-1o329ffhgodf6ipbmgqm99r2kkjsoj9u.apps.googleusercontent.com.json"

google_login_javascript_client = f"""<!DOCTYPE html>
<html itemscope itemtype="http://schema.org/Article">
<head>
    <meta charset="UTF-8">
    <meta name="google-signin-client_id" content="{GOOGLE_CLIENT_ID}">
    <title>Google Login</title><script src="https://apis.google.com/js/platform.js" async defer></script>
    <body>
    <div class="g-signin2" data-onsuccess="onSignIn"></div>
    <script>function onSignIn(googleUser) {{

  var id_token = googleUser.getAuthResponse().id_token;
    var xhr = new XMLHttpRequest();
xhr.open('POST', '{SERVER_NAME}{API_V1_STR}/login/access-token'); 
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
xhr.setRequestHeader('X-Google-OAuth2-Type', 'client');
xhr.onload = function() {{
   console.log('Signed in as: ' + xhr.responseText);
}};
xhr.send(id_token);
}}</script>
<div><br></div>
<a href="#" onclick="signOut();">Sign out</a>
<script>
  function signOut() {{
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {{
      console.log('User signed out.');
    }});
  }}
</script>
</body>
</html>"""