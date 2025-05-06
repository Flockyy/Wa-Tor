# filename: main.py

from monde import Monde
import argparse


def main():

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Wa-tor simulation")
    parser.add_argument("--height", type=int, default=10, help="Number of rows in the grid")
    parser.add_argument("--width", type=int, default=10, help="Number of columns in the grid")
    parser.add_argument("--chronon", type=int, default=10, help="Number of simulation steps")
    parser.add_argument("--fish", type=int, default=5, help="Number of fish to place in the grid")
    parser.add_argument("--shark", type=int, default=5, help="Number of sharks to place in the grid")
    parser.add_argument("--output", type=str, help="Output file for the simulation results")
    # Parse the arguments
        
    args = parser.parse_args()
    
    monde = Monde(args.height, args.width)

    for _ in range(args.fish):
        # monde.add_fish(Fish())
        pass
    for _ in range(args.shark):
        # monde.add_shark(Shark())
        pass

    for _ in range(args.chronon):
        # monde.update()
        # print(monde)
        if args.output:
            with open(args.output, "a") as f:
                f.write(str(monde) + "\n")
        else:
            print(monde)
    # Print the final state of the grid
    print("Final state of the grid:")
    print(monde)
    # Save the final state to the output file if specified
    if args.output:
        with open(args.output, "a") as f:
            f.write("Final state of the grid:\n")
            f.write(str(monde) + "\n")
            
if __name__ == "__main__":
    main()
    
