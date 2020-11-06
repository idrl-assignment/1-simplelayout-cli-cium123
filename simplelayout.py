import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description='simplelayout') 
    parser.add_argument('--board_grid', help="Layout_panel_resolution", type=int)
    parser.add_argument('--unit_grid', help="Rectangular_component_resolution", type=int)
    parser.add_argument('--unit_n', help="unit_of_Numbers", type=int)
    parser.add_argument('--positions', type=int,nargs='+', help="position_of_units")
    parser.add_argument('--o', '--outdir', help="content_of_result", type=str)
    parser.add_argument('--filename', help="name_of_file", type=str)
    args = parser.parse_args()

    if args.board_grid % args.unit_grid != 0:
        sys.exit('User exit')
    if args.unit_n != len(args.positions):
        sys.exit('User exit')
    if min(args.positions) < 1 or max(args.positions) > (args.board_grid / args.unit_grid)**2:
        sys.exit('User exit')
    if not os.path.exists(args.outdir):
        os.makedirs(args.outdir)
    filename = args.outdir + '/' + args.file_name
    with open(filename + '.mat', 'w') as _:
        pass
    with open(filename + '.jpg', 'w') as _:
        pass

if __name__ == "__main__":
    main()
