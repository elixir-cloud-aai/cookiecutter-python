export ZSH="/root/.oh-my-zsh"
plugins=(
  git
  docker
  zsh-autosuggestions
  fast-syntax-highlighting
  zsh-autocomplete
)
source $ZSH/oh-my-zsh.sh
source /workspaces/{{ cookiecutter.project_name_dashed }}/.venv/bin/activate 2>/dev/null || true