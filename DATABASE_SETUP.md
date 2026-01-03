# Database Setup Guide

## Current Issue
Your Render.com PostgreSQL database connection is failing with SSL errors. This could be because:
1. The database is sleeping (Render.com free tier databases sleep after inactivity)
2. Network/firewall issues
3. SSL configuration problems

## Quick Fix: Use SQLite for Local Development

The app is now configured to use **SQLite by default** for local development. This means:
- ✅ No external database connection needed
- ✅ Works offline
- ✅ Fast and reliable for development
- ✅ Data stored in `local.db` file

Just run your app normally:
```bash
uvicorn ToDoApp.main:app --reload
```

## Using PostgreSQL (Production)

When you're ready to use PostgreSQL (e.g., on Render.com):

1. **Wake up your Render.com database** (if it's sleeping):
   - Go to your Render.com dashboard
   - Find your PostgreSQL database
   - It should wake up automatically when accessed, but may take 30-60 seconds

2. **Set the DATABASE_URL environment variable**:
   ```bash
   export DATABASE_URL="postgresql+psycopg2://fastapi_todo_db_owvq_user:B3wG9HCPImPw8gjsXd5AHBNOAE0KYdu2@dpg-cun6mj3tq21c73edghe0-a.virginia-postgres.render.com/fastapi_todo_db_owvq"
   ```

3. **Or create a `.env` file** (recommended):
   ```bash
   echo 'DATABASE_URL=postgresql+psycopg2://fastapi_todo_db_owvq_user:B3wG9HCPImPw8gjsXd5AHBNOAE0KYdu2@dpg-cun6mj3tq21c73edghe0-a.virginia-postgres.render.com/fastapi_todo_db_owvq' > .env
   ```

   Then install python-dotenv and load it:
   ```bash
   pip install python-dotenv
   ```

## Testing Your Database Connection

Run the test script:
```bash
python3 test_db_connection.py
```

This will test different SSL modes and tell you which one works (if any).

## Troubleshooting Render.com PostgreSQL

1. **Check if database is awake**: Visit your Render.com dashboard
2. **Try the internal connection string**: Render.com provides an internal connection string that might work better
3. **Check firewall rules**: Make sure your IP isn't blocked
4. **Verify credentials**: Double-check username/password in Render.com dashboard

