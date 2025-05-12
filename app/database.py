from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import DATABASE_URL

# إعداد الاتصال بقاعدة البيانات
engine = create_async_engine(DATABASE_URL, echo=True)

# إعداد الجلسة
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# دالة للحصول على Session
async def get_session():
    async with AsyncSessionLocal() as session:
        yield session
