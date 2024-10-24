from utils.load_csv import load
import matplotlib.pyplot as plt
import argparse


def main():

    #try "Astronomy" and "Defense Against the Dark Arts"
    parser = argparse.ArgumentParser(description="Process a CSV file and choose 2 courses.")
    parser.add_argument('path', type=str, help='Path to the CSV file')
    parser.add_argument('course1', type=str, help='Course1')
    parser.add_argument('course2', type=str, help='Course2')
    args = parser.parse_args()

    try:
        df = load(args.path)
        if df is None:
            return
        if not df['Hogwarts House'].dropna().empty:
            houses = df['Hogwarts House'].unique()
        else:
            raise ValueError("Houses have not been attributed yet.")

        if args.course1 not in df.columns or args.course2 not in df.columns:
            raise ValueError(f"One or both courses do not exist.")
        
        colors = {'Gryffindor': '#FF0000', 'Hufflepuff': '#FFFF00', 'Ravenclaw': '#0000FF', 'Slytherin': '#00FF00'}
        fig, ax = plt.subplots(figsize=(10, 6))

        for house in houses:
            house_data = df[df['Hogwarts House'] == house]
            x = house_data[args.course1]
            y = house_data[args.course2]
            ax.scatter(x, y, label=house, color=colors.get(house, '#000000'), alpha=0.5)

        ax.set_xlabel(args.course1)
        ax.set_ylabel(args.course2)
        ax.set_title(f'Scatter plot of "{args.course1}" vs "{args.course2}"', pad=20, fontweight='bold')
        ax.legend(title='House')

        plt.show()

    except KeyboardInterrupt:
        print(" Keyboard interrupt detected.")
        return

    except Exception as e:
        print(type(e).__name__ + ":", e)
        return


if __name__ == "__main__":
    main()

