class AdminRouter(object):
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'auth_db'
        database.
        """
        if app_label in ['admin', 'auth', 'contenttypes', 'sessions']:
            return db == 'default'
        elif app_label == 'blog':
            return  db == 'blog'
        return None