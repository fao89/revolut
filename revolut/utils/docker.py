import os
import psycopg2
import subprocess
import yaml

from dotenv import load_dotenv


def docker_compose_file(docker_setup):
    content = {
        'version': '3.1',
        'volumes': {"postgres-data": None},
        'services': {
            'postgresql': {
                'image': 'postgres',
                'ports': ["5433:5432"],
                'volumes': ["postgres-data:/var/lib/postgresql/data"],
                'environment': [
                    'POSTGRES_PASSWORD={}'.format(
                        docker_setup['POSTGRES_PASS']
                    )
                ]
            }
        }
    }

    with open('/tmp/docker-compose.yml', 'w') as f:
        f.write(yaml.dump(content))
    
    return f.name


def execute(command, success_codes=(0,)):
    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True,
        )
        status = 0
    except subprocess.CalledProcessError as error:
        output = error.output or b''
        status = error.returncode
        command = error.cmd
    output = output.decode('utf-8')
    if status not in success_codes:
        raise Exception(
            'Command %r returned %d: """%s""".' % (command, status, output)
        )
    return output


def start_compose(env_vars):
    compose = docker_compose_file(env_vars)
    compose_up = 'docker-compose -f {} -p "revolut" up --build -d'.format(compose)
    execute(compose_up)
    

if __name__ == "__main__":
    load_dotenv()
    start_compose(os.environ)