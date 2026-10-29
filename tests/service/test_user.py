from app.services.auth_service import create_user, get_user_by_email, get_user_by_id, change_password
from app.auth.security import verify_password


# def test_create_user(db_connection):
#     email = "te33st43b6ing@gmail.com"
#     password = "cowenconew3$"

#     user = create_user(email, password)

#     # Verify the returned user
#     assert user is not None
#     assert user.id is not None
#     assert user.email == email

#     # Verify the user was persisted in the database
#     cursor = db_connection.cursor()

#     cursor.execute(
#         """
#         SELECT id, email, password_hash
#         FROM users
#         WHERE email = ?
#         """,
#         (email,),
#     )

#     db_user = cursor.fetchone()

#     assert db_user is not None
#     assert db_user["id"] == user.id
#     assert db_user["email"] == email

#     # Verify the password was hashed correctly
#     assert db_user["password_hash"] != password
#     assert verify_password(password, db_user["password_hash"])


# def test_get_user_by_id():
#     email = "tes52t_user_id@example.com"
#     password = "TestPassword123!"

#     created_user = create_user(email, password)

#     user = get_user_by_id(created_user.id)

#     assert user is not None
#     assert user["id"] == created_user.id
#     assert user["email"] == email


# def test_get_user_by_email():
#     email = "t6e1st_user_email@example.com"
#     password = "TestPassword123!"

#     created_user = create_user(email, password)

#     user = get_user_by_email(email)

#     assert user is not None
#     assert user["id"] == created_user.id
#     assert user["email"] == email


# def test_get_nonexistent_user_by_id():
#     user = get_user_by_id(999999)

#     assert user is None


def test_change_password(test_auth_db, db_connection):
    email = "change_password123@example.com"
    old_password = "OldPassword123!"
    new_password = "NewPassword456!"

    user = create_user(email, old_password)

    change_password(user.id, old_password, new_password)

    cursor = db_connection.cursor()
    cursor.execute(
        """
        SELECT password_hash
        FROM users
        WHERE id = ?
        """,
        (user.id,)
    )
    db_user = cursor.fetchone()

    assert db_user is not None
    assert db_user["password_hash"] != old_password
    assert verify_password(new_password, db_user["password_hash"])
    assert not verify_password(old_password, db_user["password_hash"])





# Password Changes
# [ ] A user can change their password with valid input.
# [ ] The new password is stored as a hash.
# [ ] The new password can be verified successfully.
# [ ] The old password no longer matches the updated hash.
# [ ] An incorrect current password prevents the change, if your application requires current-password verification.


# | Test                                                | Service test | Endpoint test |
# | --------------------------------------------------- | :----------: | :-----------: |
# | A user can change their password with valid input   |       ✅      |       ✅       |
# | The new password is stored as a hash                |       ✅      |       —       |
# | The new password can be verified successfully       |       ✅      |       —       |
# | The old password no longer matches the updated hash |       ✅      |       —       |
# | An incorrect current password prevents the change   |       ✅      |       ✅       |

