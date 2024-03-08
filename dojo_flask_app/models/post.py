from dojo_flask_app.config.mysqlconnection import connectToMySQL
from .user import User

class Post:
    def __init__(self,data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.user_id = data['user_id']
        self.user = data['user']
    
    
    @classmethod
    def save(cls,data):
        query = """INSERT INTO posts(content, user_id)
                VALUE(%(content)s, %(user_id)s);
        """
        return connectToMySQL("dojo_wall_db").query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = """ DELETE FROM posts WHERE id = %(id)s
        """
        return connectToMySQL("dojo_wall_db").query_db(query,data)
    
    @classmethod
    def get_all_post(cls):
        query = """SELECT * FROM posts 
                LEFT JOIN users on posts.user_id = users.id
                """
        results = connectToMySQL('dojo_wall_db').query_db(query)
        user_with_post= []
        for row in results:
            user_data= User({
                "id": row["user_id"],
                "first_name": row["first_name"],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                "created_at": row["created_at"],
                "updated_at": row['updated_at']
                })
            
            post_data = Post({
                "id": row["id"],
                "content": row["content"],
                "created_at": row["created_at"],
                "updated_at": row['updated_at'],
                "user" : user_data
            })
            user_with_post.append(post_data)
        return user_with_post