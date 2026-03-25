from service.test_service import TestService


def main():
    print("--- Project Template Started ---")

    # Initialize service
    app = TestService()

    # Execute
    app.run_process()


if __name__ == "__main__":
    main()
