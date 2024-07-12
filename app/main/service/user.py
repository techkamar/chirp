from app.main.util.database import get_local_session
from app.main.orm.user import User
from app.main.orm.post import Post
import uuid
import os
import shutil

db_session = get_local_session()

def create_user(userinfo):
    user = User(username=userinfo.username,password=userinfo.password,display_name = userinfo.display_name)
    db_session.add(user)
    db_session.commit()

    return user.id

def delete_user(user_id):
    # Delete all posts
    db_session.query(Post).filter(Post.user_id==user_id).delete()

    # Delete user
    db_session.query(User).filter(User.id==user_id).delete()

    db_session.commit()
    
    return "Done"

def get_new_image_file_name():
    path = os.getcwd()+"/images"
    filename =  str(uuid.uuid4())+".png"
    return {"path": path, "filename": filename}

def get_single_user(user_id):
    curr_user = db_session.query(User).filter(User.id==user_id).first()

    details = {"display_name": curr_user.display_name, "username": curr_user.username, "display_pic": curr_user.display_pic}

    return details

def get_all_users():
    all_users = []
    
    users = db_session.query(User).all()

    for user in users:
        details = {"id": user.id, "display_name": user.display_name, "username": user.username, "display_pic": user.display_pic}
        all_users.append(details)
    
    return all_users

    return details
def post_user_dp(user_id,file):
    destination_filename_detail = get_new_image_file_name()
    
    if not os.path.exists(destination_filename_detail['path']):
        os.mkdir(destination_filename_detail['path'])

    destination_filename_location = destination_filename_detail['path']+"/"+destination_filename_detail['filename']
    
    with open(destination_filename_location,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    
    # Now update user table
    db_session.query(User).filter(User.id==user_id).update({User.display_pic:destination_filename_detail['filename']})
    db_session.commit()
    
    return "Done"