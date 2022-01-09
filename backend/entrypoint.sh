#!/bin/sh

echo "Waiting for mysql..."

while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.1
done

echo "MySQL started"

flask db upgrade
echo "db upgraded"
python gh_robber.py make_shell_context

exec "$@"