# devops-lab

Навчальний проєкт для лабораторних робіт з курсу «Практики DevOps та Cloud-обчислення».

[![CI Workflow](https://github.com/VitaliyKulchytskyy/devops_lab1/actions/workflows/ci.yml/badge.svg)](https://github.com/VitaliyKulchytskyy/devops_lab1/actions/workflows/ci.yml)

## Запуск

```bash
pip install -r requirements.txt
python3 app.py          # http://127.0.0.1:5000
```

## Перевірки

```bash
pip install -r requirements-dev.txt
flake8 .
pytest -v
```

## CI/CD

Workflow `.github/workflows/ci.yml` при кожному push у `main`:
1. встановлює залежності, перевіряє код flake8 і запускає тести pytest;
2. якщо перевірки пройшли — збирає статичну версію сторінки (`build_static.py`)
   і розгортає її на GitHub Pages:
   https://vitaliykulchytskyy.github.io/devops_lab1/
