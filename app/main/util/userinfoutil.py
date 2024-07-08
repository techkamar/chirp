
def get_user_id(request):
    user_id = request.headers.get("USER_ID")
    return int(user_id)