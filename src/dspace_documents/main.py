import asyncio
import os
from config import BASE_FOLDER, FILE_FORMAT
from InsertDocument import insertDocument
from InsertContent import insertContent


async def process_pdf_files(base_folder, file_format):

    """Processes PDF files in the given directory by printing their names."""
    for document_name in os.listdir(base_folder):
        if document_name.endswith(file_format) and os.path.isfile(os.path.join(base_folder, document_name)):
            id = await insertDocument(document_name)

            await insertContent(id, document_name, base_folder)

        
asyncio.run(process_pdf_files(base_folder = BASE_FOLDER, file_format = FILE_FORMAT))