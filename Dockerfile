# This was taken from the Python devcontainer example from Microsoft
# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
FROM ghcr.io/astral-sh/uv:bookworm

WORKDIR /home
COPY . .
EXPOSE 8000
RUN uv run flet run

CMD [ "/bin/ls", "-l" ]
