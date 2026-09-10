FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates && rm -rf /var/lib/apt/lists/*
WORKDIR /opt/engineering
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY . .
ARG REPO_PILOT_EXTRAS="minimal"
ARG REPO_PILOT_INSTALL_MODE="static"
RUN case "$REPO_PILOT_EXTRAS" in minimal|cgc|sourcegraph|all) ;; *) exit 2 ;; esac; \
    case "$REPO_PILOT_INSTALL_MODE" in static|editable) ;; *) exit 2 ;; esac; \
    target="."; if [ "$REPO_PILOT_EXTRAS" != minimal ]; then target=".[$REPO_PILOT_EXTRAS]"; fi; \
    if [ "$REPO_PILOT_INSTALL_MODE" = editable ]; then \
      python -m pip install --no-cache-dir --editable "$target"; \
    else python -m pip install --no-cache-dir "$target"; fi
ARG SPEC_KIT_REF=""
RUN if [ -n "$SPEC_KIT_REF" ]; then \
      python setup_tooling.py --mode venv --speckit-ref "$SPEC_KIT_REF" --export-record /opt/engineering/toolchain.json --apply; \
    else \
      python -c "import toolchains; toolchains.write_record('toolchain.json', toolchains.resolve_selection())"; \
    fi
RUN chmod 644 /opt/engineering/toolchain.json
ENTRYPOINT ["python", "/opt/engineering/docker_install.py"]
CMD ["--help"]
