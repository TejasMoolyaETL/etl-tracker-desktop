class SessionManager:
    token = None
    user_code = None
    role = None

    @classmethod
    def set_session(cls, token, user_code, role):
        cls.token = token
        cls.user_code = user_code
        cls.role = role

    @classmethod
    def clear(cls):
        cls.token = None
        cls.user_code = None
        cls.role = None

    @classmethod
    def is_admin(cls):
        return cls.role == "ADMIN"

    @classmethod
    def is_super_admin(cls):
        return cls.role == "SUPER_ADMIN"

    @classmethod
    def is_user(cls):
        return cls.role == "USER"
    
    @classmethod
    def get_token(cls):
        return cls.token
