from dikshantprogress import TimedProgressBar

print("Running 3 second progress bar:")
bar = TimedProgressBar(total=30)
bar.run_for(3)