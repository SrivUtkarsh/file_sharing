from models.db_models import FileMetadata
def create_file(db, filename, object_key, owner_id, file_size, content_type):
    file = FileMetadata(
        filename=filename,
        object_key=object_key,
        owner_id=owner_id,
        file_size=file_size,
        content_type=content_type
    )
    db.add(file)
    db.commit()
    db.refresh(file)
    return file
def get_user_files(db, owner_id):
    return db.query(FileMetadata).filter(
        FileMetadata.owner_id == owner_id
    ).all()
def get_file(db, file_id, owner_id):
    return db.query(FileMetadata).filter(
        FileMetadata.id == file_id,
        FileMetadata.owner_id == owner_id
    ).first()
def delete_file_metadata(db, file):
    db.delete(file)
    db.commit()