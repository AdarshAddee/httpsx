from httpsx.httpsx import *

if len(sys.argv) == 1:
    banner()
    parser.print_help(sys.stderr)
    sys.exit(1)

if arg_file:
    handle_file()

if arg_url:
    handle_url(arg_url)

if arg_output:
        handle_output()

print()


