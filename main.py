def main() -> None:
    __síkidom__ = input('Írjon be egy t betűt ha egy téglalap kerületét és területét szeretné kiszámolni, viszont ha egy kör területét és kerületét szeretné kiszámolni írjon be egy k betűt: ')
    kerület: float = 0
    terület: float = 0
    pí = 3.14
    if __síkidom__ == "t":
        a_oldal = float(input('Kérem adja meg a téglalap a oldalának az értékét: '))
        b_oldal = float(input('Kérem adja meg a téglalap b oldalának az értékét: '))
        kerület = kerület + (2 * a_oldal + 2 * b_oldal)
        terület = terület + (a_oldal * b_oldal)
        print(f'A választott síkidom területe: {kerület}')
        print(f'A választott síkidom területe: {terület}')
    elif __síkidom__ == "k":
        sugár = float(input('Kérem adja meg a kör sugarának az értékét: '))
        kerület = kerület + (2 * sugár * pí)
        terület = terület + (pí * sugár ** 2)
        print(f'A választott síkidom területe: {kerület}')
        print(f'A választott síkidom területe: {terület}')
    else:
        print('Kérem a "t" és "k" betűk közül válasszon!')


if __name__ == "__main__":
    main()
