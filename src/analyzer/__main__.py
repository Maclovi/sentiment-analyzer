if __name__ == "__main__":
    import uvicorn

    from analyzer.bootstrap import setup_configs
    from analyzer.web import create_web

    asgi_conf = setup_configs().asgi
    uvicorn.run(create_web(), host=asgi_conf.host, port=asgi_conf.port)
