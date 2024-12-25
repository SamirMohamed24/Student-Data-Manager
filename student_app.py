import psycopg2
from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *

def insert_student_to_db(data, image_data):
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            dbname="postgres",
            user="altoum",
            password="Abosamra10",
            host="pgdatabasetest.postgres.database.azure.com",
            port=5432,
            sslmode="require"
        )

        cursor = connection.cursor()

        # Insert query
        insert_query = """
        INSERT INTO students (name, address, email, phone, certificate, languages, image)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        """

        # Execute the insert query
        cursor.execute(insert_query, (
            data['Student'],
            data['Country'],
            data['Email'],
            data['phone'],
            data['Certi'],
            data['language'],
            psycopg2.Binary(image_data)  # For image data (if any)
        ))

        # Commit the transaction
        connection.commit()
        cursor.close()

        return "Data inserted successfully into the database!"

    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

    finally:
        if connection:
            connection.close()

def App():
    put_html('<center><h3>Students Form</h3></center>').style('background-color:#640D5F; color:gold; padding:25px;')
    put_html('<p>Students Application</p>').style('text-align:center; font-weight:bold;')
    put_html('<center><img src="https://educationusa.state.gov/sites/default/files/styles/content_area_full_width/public/wysiwyg/istock_000058708198_full.jpg?itok=smexSplR" width="1000"></center>')

    try:
        with open("student_image.jpg", "rb") as f:
            put_image(f.read()).style('width:1000px;')
    except FileNotFoundError:
        put_text("Error: student_image.jpg not found.")

    # Collect form data
    data = input_group(
        'Students Information',
        [
            input('Name', name='Student'),
            input('Address', name='Country'),
            input('Email', name='Email'),
            input('Phone number', name='phone', type=NUMBER),
            radio('File format', options=['word', 'excel', 'Powepoint'], name='Certi'),
            checkbox('language', options=['Swedish', 'English','Arabic','French'], inline=True, name='language')
        ]
    )

    # Collect image files
    imgs = file_upload(
        'Upload File',
        accept='image/*',
        multiple=True
    )

    # Get the uploaded image data (if any)
    image_data = None
    if imgs:
        image_data = imgs[0]['content']

    # Insert the data into the PostgreSQL database
    result = insert_student_to_db(data, image_data)

    # Display the result
    put_text(result)

start_server(App, port=1717, debug=True)
