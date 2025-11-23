import logging

def calculate_average(list):
    logging.debug("Star calculating average")
    logging.debug("List: %s", list)

    sum = sum(list)
    average = sum/len(list)
    logging.info("Finshed calculating average: %.2f", average)

    if average > 100:
        logging.error("Average value unusually high: %.2f", average)
    elif average < 0:
        logging.warning("Negative average: %.2f", average)

    return average

def main():
    logging.basicConfig(filename = 'app.log',
        level=logging.DEBUG,
        format = '%(asctime)s - %(Levelname) - %(message)s'
    )

    list = [5, 10, 15, 20, -99]
    logging.debug("Starting program")
    result = calculate_average(list)
    logging.info("Average result: %.2f", result)

if __name__ == "__main__":
    main()


   


