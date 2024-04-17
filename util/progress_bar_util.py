def print_progress_bar(iteration, total):
    percent = "{0:.1f}".format(100 * (iteration / float(total)))
    filled_length = int(50 * iteration // total)
    bar = "█" * filled_length + "-" * (50 - filled_length)
    print(f"\r |{bar}| {percent}%")
