# from flask import Flask, render_template, send_file, request, redirect, url_for, send_from_directory
# import os
# import openpyxl
# from datetime import datetime

# app = Flask(__name__)

# # Path to the CV file (ensure it exists inside the static folder)
# CV_FILE_PATH = "static/CV,CL.docx"

# # Path to the Excel file
# EXCEL_FILE_PATH = 'form_data_message.xlsx'

# # Initialize Excel if it doesn't exist
# if not os.path.exists(EXCEL_FILE_PATH):
#     workbook = openpyxl.Workbook()
#     sheet = workbook.active
#     sheet.append(["Name", "Email", "Message", "Date"])
#     workbook.save(EXCEL_FILE_PATH)

# @app.route('/')
# def home():
#     return render_template('index.html')

# # ✅ Serve index.html inside portfolio_two folder
# @app.route('/portfolio_two')
# def portfolio_two():
#     return send_from_directory(os.path.abspath('portfolio_two'), 'index.html')

# # ✅ Serve static files inside portfolio_two (like images, CSS, JS)
# @app.route('/portfolio_two/<path:filename>')
# def portfolio_two_static(filename):
#     return send_from_directory('portfolio_two', filename)

# @app.route('/download')
# def download_cv():
#     if os.path.exists(CV_FILE_PATH):
#         return send_file(
#             CV_FILE_PATH,
#             as_attachment=True,
#             download_name="lethean_seourn_cv.docx",
#             mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#         )
#     else:
#         return "Error: CV file not found.", 404

# @app.route('/submit', methods=['POST'])
# def submit_form():
#     name = request.form.get('name')
#     email = request.form.get('email')
#     message = request.form.get('message')

#     if not all([name, email, message]):
#         return "Error: All fields are required.", 400

#     contact_date = datetime.now().strftime('%Y-%m-%d')
#     store_data_in_excel(name, email, message, contact_date)

#     return redirect(url_for('home'))

# def store_data_in_excel(name, email, message, contact_date):
#     workbook = openpyxl.load_workbook(EXCEL_FILE_PATH)
#     sheet = workbook.active
#     sheet.append([name, email, message, contact_date])
#     workbook.save(EXCEL_FILE_PATH)

# if __name__ == '__main__':
#     app.run(debug=True)
