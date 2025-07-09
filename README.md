# 🧠 MedicalAIChatbot

Chatbot hỗ trợ tư vấn y tế sơ bộ, gợi ý bác sĩ và hỗ trợ đặt lịch khám.

---

## 🚀 Cài đặt và chạy

### 1. Clone project từ GitHub:

```bash
git clone https://github.com/Bravery23/MedicalAIChatbot.git
cd MedicalAIChatbot
```

### 2. Tạo môi trường ảo (virtual environment):

```bash
python -m venv .venv
```

### 3. Kích hoạt môi trường ảo:

* **Windows:**

```bash
.venv\Scripts\activate
```

* **macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

---

## 🧪 Huấn luyện và chạy chatbot

### Train mô hình:

```bash
rasa train
```

### Chạy giao diện dòng lệnh:

```bash
rasa shell
```

---

## 📁 Cấu trúc thư mục chính

```
MedicalAIChatbot/
├— data/             # Dữ liệu huấn luyện NLU
├— domain.yml        # Định nghĩa intents, entities, slots, actions
├— config.yml        # Pipeline và policy
├— rules.yml         # Luật hội thoại
├— stories.yml       # Các đoạn hội thoại mẫu
├— actions.py        # Tuỳ chỉnh hành động (nếu có)
├— requirements.txt  # Danh sách thư viện
├— .gitignore        # Loại trừ file không cần thiết
└— README.md         # File hướng dẫn này
```

---

## 👥 Làm việc nhóm (Git)

### Pull code mới nhất:

```bash
git pull
```

### Commit thay đổi:

```bash
git add .
git commit -m "Mô tả thay đổi"
git push
```

---

## ✅ Yêu cầu hệ thống

* Python <= 3.10
* pip
* Git

---
