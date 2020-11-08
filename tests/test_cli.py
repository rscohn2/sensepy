from rocohome import cli


class MockArgs:
    dry_run = False


mock_args = MockArgs()


def test_db_start():
    cli.args = mock_args
    cli.db.up()
    cli.db.down()
