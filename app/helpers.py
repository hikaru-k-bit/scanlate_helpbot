from app.credentials import connect


async def is_projects():
    """
    :return: bool
    """
    pool = await connect()
    async with pool.acquire() as connection:
        async with connection.cursor() as cursor:
            await cursor.execute("SELECT COUNT(*) FROM projects")

            result = await cursor.fetchone()
            if result[0] > 0:
                return True
            else:
                return False
