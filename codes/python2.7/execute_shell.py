import subprocess


# execute_shell wrap subprocess.Popen, and return returncode, ouput and err
# ignore will ignore returncode
def execute_shell(logger, command, ignore=False):
    p = subprocess.Popen(command,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    output, err = p.communicate()
    if not ignore and p.returncode != 0:
        logger.error(
            'Failed to execute command %s, output %s, error %s, returncode %s'
            % (command, output, err, p.returncode))
    else:
        logger.info(
            'Execute command success: %s, output %s, error %s, returncode %s' %
            (command, output, err, p.returncode))

    return p.returncode, output, err
