from StopWatch import StopWatch
watch = StopWatch()

watch.start()

def sumNum():
    counter = 1
    for number in range(100000 - 1):
        counter += number + 2
    print(counter)

sumNum()

watch.stop()
print(watch.getElapsedTime())