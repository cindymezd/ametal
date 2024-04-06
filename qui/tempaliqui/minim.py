def create_password_new(project_id, username, password):
    """
    Creates a new password for the given username.

    Args:
        project_id (string): Google Cloud project ID (e.g. 'my-project').
        username (string): Username for the user (e.g. 'my-user').
        password (string): New password for the user.

    Returns:
        ApiPassword: Cloud Spanner API password.

    """

    spanner_client = spanner.Client()
    instance = spanner_client.instance(instance_id)
    database = instance.database(database_id)

    database.update_ddl(
        [
            "CREATE USER {} IDENTIFIED BY '{}'".format(username, password),
            "GRANT USAGE ON DATABASE {} TO {}".format(database_id, username),
        ]
    )

    return ApiPassword(username, password)
  
