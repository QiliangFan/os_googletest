from test_google import  TestGoogle


def main():
    test_case = TestGoogle()
    test_case.setup_method()
    test_case.test_google_random_pick()
    test_case.teardown_method()


if __name__ == "__main__":
    main()