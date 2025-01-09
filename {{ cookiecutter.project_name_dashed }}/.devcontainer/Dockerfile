# syntax=docker/dockerfile:1

###############################################################################
# Stage 1: Base image 
###############################################################################

ARG PYTHON_VERSION={{ cookiecutter.python_version }}
FROM python:${PYTHON_VERSION} as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git \
        zsh \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

###############################################################################
# Stage 2: Poetry Install 
###############################################################################

FROM base as poetry-installer

ENV POETRY_VIRTUALENVS_IN_PROJECT=false \
    POETRY_NO_INTERACTION=1

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

###############################################################################
# Stage 3: Zsh Configuration 
###############################################################################

FROM poetry-installer as zsh-config

ENV ZSH_CUSTOM=/root/.oh-my-zsh/custom

# Install Oh My Zsh and clone plugins
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended \
    && git clone https://github.com/zsh-users/zsh-autosuggestions.git ${ZSH_CUSTOM}/plugins/zsh-autosuggestions \
    && git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM}/plugins/fast-syntax-highlighting

# Install direnv
RUN curl -sfL https://direnv.net/install.sh | bash

COPY .devcontainer/override.zshrc /tmp/override.zshrc
RUN cat /tmp/override.zshrc >> ~/.zshrc \
    && chsh -s $(which zsh)

###############################################################################
# Stage 4: Development
###############################################################################

FROM zsh-config as development

WORKDIR /workspaces/{{ cookiecutter.project_name_dashed }}

ENV SHELL=/bin/zsh

CMD ["zsh"]