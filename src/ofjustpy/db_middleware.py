from starlette.requests import Request
from sqlalchemy.ext.asyncio import async_sessionmaker, async_scoped_session

# via https://medium.com/@lironbenyeda/fastapi-sqlalchemy-and-parallel-queries-walk-into-a-bar-86dfe40aa878
from asyncio import current_task

# see Using Thread-Local Scope with Web Applications
# in https://docs.sqlalchemy.org/en/20/orm/contextual.html#

class DBSessionMiddleware:
    def __init__(self, app, db_async_engine=None):
        self.app = app
        self.db_session_factory =  async_sessionmaker(db_async_engine, expire_on_commit=False)
        # scopefunc is required -- not really sure why
        self.scoped_session = async_scoped_session(self.db_session_factory, scopefunc=current_task)
    async def __call__(self, scope, receive, send):
        print ("DBSessionMiddleware called ")
        if scope["type"] == "http":  # Ensure we're only handling HTTP requests
            request = Request(scope, receive, send)
            # Create an async session for the request
            # Q: why we don't need async_scoped session?
            # async with async_scoped_session(self.db_session_factory)() as session:
            async with self.scoped_session() as session:
                request.state.db_session = session
                # Call the next middleware or the route handler
                try:
                    await self.app(scope, receive, send)
                    await session.commit()
                except Exception as e:
                    await session.rollback()  # Rollback in case of error
                    print("ohh hell !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", e)
                finally:
                    # scroped sessions are removed
                    # scoped will get cleaned up automatically
                    pass
        else:
            # If not HTTP, just pass through
            await self.app(scope, receive, send)

            
