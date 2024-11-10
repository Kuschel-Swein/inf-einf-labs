import check50
import check50.c

TASK = 3

check = check50.import_checks('../')


@check50.check()
def exists():
    check.exists()


@check50.check(exists)
def compiles():
    check.compiles()


@check50.check(compiles)
def accepts_arguments():
    check.accepts_arguments()


@check50.check(compiles)
def accepts_passwords():
    check.passwords(task=TASK, should_be_valid=True, include_arguments=True)


@check50.check(compiles)
def rejects_passwords():
    check.passwords(task=TASK, should_be_valid=False, include_arguments=True)
