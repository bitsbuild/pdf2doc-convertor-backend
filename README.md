# 📄 PDF to DOCX Converter API

This is a simple Django REST Framework API that accepts a PDF file, converts it to a DOCX file, and directly returns the converted file for download.  
The conversion is handled using `pdf2docx`.

**Production URL:** [https://pdf-to-docx-cubg.onrender.com](https://pdf-to-docx-cubg.onrender.com)  
**Repository:** [https://github.com/bitsbuild/pdf2doc-convertor-backend.git](https://github.com/bitsbuild/pdf2doc-convertor-backend.git)

---

## 🚀 Features

- Upload a single PDF file.
- Converts the uploaded PDF to DOCX format.
- Deletes any previous files and database records before processing a new file.
- **Directly returns** the converted DOCX as a file response — no media URLs are exposed.
- Production-ready with `DEBUG = False` and strict `ALLOWED_HOSTS`.

---

## ⚙️ Tech Stack

- **Django** `5.2.4`
- **Django REST Framework** `3.16.0`
- **pdf2docx**
- Python `3.x`

---

## 🧩 API Endpoint

### Upload & Convert PDF

**Production URL:**  
`https://pdf-to-docx-cubg.onrender.com/convert/pdf/`

**Method:** `POST`  
**Request Body (multipart/form-data):**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| pdf   | File (PDF) | Yes | The PDF file to convert. |

**Successful Response:**  
Returns the generated `.docx` **directly** as a file download with content type:  
```

application/vnd.openxmlformats-officedocument.wordprocessingml.document

```

---

## 📌 Notes

* Only PDF files are allowed.
* Each request deletes any existing uploaded PDF and generated DOCX.
* All previous database entries are wiped on each request.
* The generated DOCX is streamed directly — no public media files are exposed.
* Production settings are secure with `DEBUG = False` and `ALLOWED_HOSTS` restricted to your Render domain.

---

## ⚠️ Security Considerations

* Uploaded files and output are served only through controlled file responses.
* `MEDIA_ROOT` is used only for temporary file processing.
* Django’s security middleware is fully enabled.

---

## 📃 License

MIT License.

---

**Keep it simple. Upload, convert, download — securely.**
