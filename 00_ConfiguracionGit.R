# Configuración y Conexión con Github

# Carga librería para uso de git
library(usethis)
# Activar Git
use_git()
# Activar GitHub
use_github()
# Activar Token
library(gitcreds)
gitcreds_set()

# Generar Token de conexión
create_github_token()
"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"
# Registrar Token de Conexión
library(credentials)
set_github_pat()