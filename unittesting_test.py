import reading_from_file

def test_happypath():
    """Test Case for happy path: valid file name with data in it"""
    actual_result = reading_from_file.file_test("testfile.txt", "r")
    expected_result = ['edcba']
    assert actual_result[1] == expected_result


def test_invalidfilemode():
    """Test Case for invalid file mode i.e 'write' mode here"""
    actual_result = reading_from_file.file_test("testfile.txt", "w")
    expected_result = "Check file options"
    assert actual_result == expected_result


def test_invalidfilename():
    """Test Case for invalid file name"""
    actual_result = reading_from_file.file_test("invalidfilename.txt", "r")
    expected_result = "invalid file name"
    assert expected_result in actual_result


def test_nosuchfile_exists():
    """Test Case for non-existant file name"""
    actual_result = reading_from_file.file_test("", "r")
    expected_result = "File doesnot exist"
    assert expected_result in actual_result

def test_invalidfilepath():
    """Test Case for invalid file path"""
    actual_result = reading_from_file.file_test("C:/", "r")
    expected_result = "invalid file path"
    assert expected_result in actual_result