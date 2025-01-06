ARG PYTHON_VERSION={{ cookiecutter.python_version }}
FROM python:${PYTHON_VERSION}

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_VERSION=1.7.1 \
    ZSH_CUSTOM=/root/.oh-my-zsh/custom

# Install system dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git \
        curl \
        zsh \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

# Install oh-my-zsh
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

# Install zsh plugins
RUN git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM}/plugins/zsh-autosuggestions \
    && git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/fast-syntax-highlighting \
    && git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git ${ZSH_CUSTOM}/plugins/zsh-autocomplete

# Configure zsh
RUN sed -i -e '$aexport ZSH="/root/.oh-my-zsh"' \
       -e '$aplugins=(git docker zsh-autosuggestions fast-syntax-highlighting zsh-autocomplete)' \
       -e '$asource $ZSH/oh-my-zsh.sh' \
       -e '$asource /workspaces/{{ cookiecutter.project_name_dashed }}/.venv/bin/activate 2>/dev/null || true' \
       ~/.zshrc

# Make zsh the default shell
RUN chsh -s $(which zsh)

# Set working directory
WORKDIR /workspaces/{{ cookiecutter.project_name_dashed }}

# Default shell to zsh
ENV SHELL=/bin/zsh
CMD ["zsh"]