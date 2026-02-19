FROM python:3.12.12-trixie

ARG QUARTO_VERSION=1.8.27

RUN wget https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.deb && \
    apt install ./quarto-${QUARTO_VERSION}-linux-amd64.deb && \
    rm -rf quarto-${QUARTO_VERSION}-linux-amd64.deb

COPY build/entrypoint /entrypoint

RUN chmod +x /entrypoint/init.py

RUN  pip3 install --upgrade pip \
  && pip3 install -r /entrypoint/requirements.txt

RUN pip3 install git+https://github.com/yk/patch-torch-save

RUN adduser jupyter --home /home/jupyter --disabled-password --quiet

USER jupyter

WORKDIR /home/jupyter

CMD ["/entrypoint/init.py", "lab", "--no-browser", "--disable-notebook-app-token", "--allow-root", "--ip='*'"]
