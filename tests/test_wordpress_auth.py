from minisite.services.wordpress import verify_hash


def test_wordpress_auth():
    password = "hello"
    hash = "$P$HiHUzCfIIUCbpI2Nveg824FXf8y4Yn."
    assert verify_hash(password, hash), "Passwords do not match"
