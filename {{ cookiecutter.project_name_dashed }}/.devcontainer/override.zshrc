# Path to your oh-my-zsh installation
export ZSH="/root/.oh-my-zsh"

# Plugins
plugins=(
  direnv # Loads .envrc files
  git # Adds git command aliases and useful prompt info
  docker  # Provides docker command completion and aliases
  zsh-autosuggestions # Suggests commands based on history
  fast-syntax-highlighting  # Adds syntax highlighting while typing
)

# Load oh-my-zsh with the configured settings
source $ZSH/oh-my-zsh.sh

# Load asdf
. "$HOME/.asdf/asdf.sh"

# Initialize direnv
eval "$(direnv hook zsh)"

# Attempt to activate the Python virtual environment for every session
source /workspaces/{{ cookiecutter.project_name_dashed }}/.venv/bin/activate 2>/dev/null || true
