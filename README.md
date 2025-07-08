# 📄 PDF to DOCX Converter API

This is a simple Django REST Framework API that accepts a PDF file, converts it to a DOCX file, and returns a download link.  
The conversion is handled using `pdf2docx`.

---

## 🚀 Features

- Upload a single PDF file.
- Converts the uploaded PDF to DOCX format.
- Deletes any previous files and database records before processing a new file.
- Returns a download link for the converted DOCX.

---

## ⚙️ Tech Stack

- **Django** `5.2.4`
- **Django REST Framework** `3.16.0`
- **pdf2docx**
- Python `3.x`

---

## 🧩 API Endpoint

### Upload & Convert PDF

**URL:** `/convert/pdf/`  
**Method:** `POST`  
**Request Body (multipart/form-data):**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| pdf   | File (PDF) | Yes | The PDF file to convert. |

**Successful Response:**

```json
{
  "DownloadLink": "http://localhost:8000/media/result.docx"
}
````

---

## 📌 Notes

* Only PDF files are allowed.
* Each request deletes any existing uploaded PDF and generated DOCX.
* All previous database entries are wiped on each request.
* Uploaded files are saved as `file.pdf` and `result.docx` in the `MEDIA_ROOT`.

---

## ⚠️ Security Considerations

* This API automatically removes previous files and database entries.
* Ensure `MEDIA_ROOT` is properly secured in production.
* Use `whitenoise` or proper static file handling when deploying.

---

## 📃 License

MIT License.

---

**Keep it simple. Upload, convert, download.**
