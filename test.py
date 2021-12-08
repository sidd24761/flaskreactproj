try:
    from app import *
    import unittest
except Exception as e:
    print("Some modules are missing {} ".format(e))

class Flasktest(unittest.TestCase):
    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statusCode = response.status_code
        self.assertEqual(statusCode, 200)

if __name__ == "__main__":
    unittest.main()
