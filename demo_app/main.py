"""Simple entry point that exercises the demo modules safely.

All calls are guarded so the script can be run without errors even if
environment variables are missing.
"""

if __name__ == "__main__":
    from .core import get_user_data, process_all_users, helper
    from .utils import hash_password, read_file_safely, dummy_s3_upload, long_running_task

    # Example usage – feel free to uncomment any line you want to test.
    # print(get_user_data(42))                     # requires a demo.db with a users table
    # process_all_users()
    # print(helper(7, 5))
    # print(hash_password("mysecret"))
    # try:
    #     print(read_file_safely("README.md"))
    # except Exception as e:
    #     print(f"Read error: {e}")
    # dummy_s3_upload(b"hello world")
    # long_running_task()