import os
from supabase import create_client
from dotenv import load_dotenv


load_dotenv()


SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")


supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


try:
    response = supabase.table('test-table').insert([{"id": "name"}]).execute()
    if response.data:
        print("Database is working! Retrieved data:")
        print(response.data)
    else:
        print("Database is connected but no data found.")
except Exception as e:
    print("Error connecting to the database:", e)

