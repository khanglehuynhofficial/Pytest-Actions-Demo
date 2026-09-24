import demo

def test_password_valid():
    assert demo.validate_secure_password("Admin@123") is True
    assert demo.validate_secure_password("P@ssword1234") is True

def test_password_length_boundaries():
    assert demo.validate_secure_password("Ab@1234") is False
    assert demo.validate_secure_password("A" * 16 + "b@123") is False

def test_password_invalid_components():
    assert demo.validate_secure_password("admin@123") is False
    assert demo.validate_secure_password("Admin1234") is False
    assert demo.validate_secure_password("Admin @123") is False

