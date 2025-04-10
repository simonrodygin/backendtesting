#!/bin/bash

check_url() {
  local url=$1
  local expected_status=${2:-200}
  echo "Проверка $url на статус $expected_status"

  for i in {1..10}; do
    status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$status" -eq "$expected_status" ]; then
      echo "$url доступен (статус $status)"
      return 0
    else
      echo "Ожидание $url... (текущий статус: $status, попытка $i)"
      sleep 2
    fi
  done

  echo "$url недоступен или неверный статус"
  return 1
}

check_url http://127.0.0.1:8000/docs#/ 200 || exit 1
check_url http://127.0.0.1:8001/docs#/  200 || exit 1