import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def healthcheck(self) -> str:
        return "OK"
