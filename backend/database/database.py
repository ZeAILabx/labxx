from supabase import create_client, Client
from src.config import Config


def get_supabase() -> Client:
    if not Config.SUPABASE_URL or 'your_supabase' in Config.SUPABASE_URL:
        raise ValueError("Supabase credentials not configured. Please set SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY in backend/.env")
    return create_client(Config.SUPABASE_URL, Config.SUPABASE_SERVICE_ROLE_KEY)


