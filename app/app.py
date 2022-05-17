import shutil
import argparse

AWS_PROFILE_SRC_DIR = f'/Users/adas/codebase/personal/projects/aws-cli-manager/app/test-directory/source'
AWS_PROFILE_TGT_DIR = f'/Users/adas/codebase/personal/projects/aws-cli-manager/app/test-directory/target'

def activate_profile(profile_name):
    shutil.copy(
        f'{AWS_PROFILE_SRC_DIR}/{profile_name}/config', 
        f'{AWS_PROFILE_TGT_DIR}'
    )

    shutil.copy(
        f'{AWS_PROFILE_SRC_DIR}/{profile_name}/credentials', 
        f'{AWS_PROFILE_TGT_DIR}'
    )


def main():
    
    # Create the parser
    parser = argparse.ArgumentParser()

    # Add an argument
    parser.add_argument('--profile', type=str, required=True)

    # Parse the argument
    args = parser.parse_args()
    profile_name = args.profile

    activate_profile(profile_name)
    
    # Print "Hello" + the user input argument
    print('Hello,', args.profile)


if __name__ == "__main__":
    main()