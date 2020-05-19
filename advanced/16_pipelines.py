"""Data pipelines allow large amounts of data to be processed without loading into memory at once."""

print("\n############# PULL PIPELINES ##############")
print("\ngenerators can be used for iteration based data pipelines...")


def pipeline_stage_one_a(limit):
    num = 0
    while num <= limit:
        print("stage 1 yield")
        yield num
        num += 1


def pipeline_stage_two(previous_stage_generator):
    for value in previous_stage_generator:
        print("stage 2 yield")
        yield value * value


def pipeline_stage_three(previous_stage_generator):
    for squared_value in previous_stage_generator:
        squared_value += 1
        print("stage 3 yield")
        yield squared_value


print("\ncreate a data pipeline using generators...")
stage1 = pipeline_stage_one_a(limit=10)         # create initial generator - returns generator object, no execution
stage2 = pipeline_stage_two(stage1)             # pass it to the next in the pipeline
stage3 = pipeline_stage_three(stage2)           # pass it to the next in the pipeline

print("use iteration to pull data through pipeline")
for i in stage3:
    print("x^2 + 1 =", i)

print("\nsame can be done using generator comprehensions...")
stage1 = (x for x in range(10))                 # create initial generator
stage2 = (x*x for x in stage1)                  # pass it to the next in the pipeline
stage3 = (x+1 for x in stage2)                  # pass it to the next in the pipeline

# here we use iteration to pull the data through the pipeline from the end
for i in stage3:
    print("x^2 + 1 =", i)


def pipeline_stage_one_b(limit):
    num = 0
    while num <= limit:
        print("stage 1a yield")
        yield f"(x = {num})"
        num += 1


def pipeline_stage_multiplex(previous_stage_generator_a, previous_stage_generator_b):
    for squared_value, value_label in zip(previous_stage_generator_a, previous_stage_generator_b):
        squared_value += 1
        print("stage 3 yield")
        yield f"{squared_value} {value_label}"


print("\nyou can create many-to-one generators in the pipeline with zip...")
stage1a = pipeline_stage_one_a(limit=10)                # create first generator
stage1b = pipeline_stage_one_b(limit=10)                # create second generator
stage2 = pipeline_stage_two(stage1a)                    # pass first to the next in the pipeline
stage3 = pipeline_stage_multiplex(stage2, stage1b)      # pass two generators to the next in the pipeline

for i in stage3:
    print("x^2 + 1 =", i)

print("\n############# PUSH PIPELINES ##############")
# see http://www.dabeaz.com/coroutines/
print("\ncoroutines can be used to create producer-consumer data pipelines...")


def pipeline_producer(next_stage_coroutine, limit):
    num = 0
    _return_value = next_stage_coroutine.send(None)                 # prime the next stage in the pipeline
    while num <= limit:
        print("stage producer send")
        _return_value = next_stage_coroutine.send(num)
        print("return value from producer send =", _return_value)
        num += 1
    next_stage_coroutine.close()


def pipeline_stage_one(next_stage_coroutine):
    _return_value = next_stage_coroutine.send(None)
    while True:
        print("stage 1 yield")
        value = (yield _return_value)                               # yield back up the pipeline
        print("stage 1 send")
        _return_value = next_stage_coroutine.send(value * value)    # send down the pipeline


def pipeline_stage_two(next_stage_coroutine):
    _return_value = next_stage_coroutine.send(None)
    while True:
        print("stage 2 yield")
        value = (yield _return_value)
        print("stage 2 send")
        _return_value = next_stage_coroutine.send(value + 1)


def pipeline_stage_consumer(prefix_string):
    while True:
        print("stage consumer yield")
        value = (yield 'Consumed')
        print(prefix_string, value)


print("\ncreate a data pipeline using coroutines...")
stage_consumer = pipeline_stage_consumer("x^2 + 1 =")
stage2 = pipeline_stage_two(stage_consumer)
stage1 = pipeline_stage_one(stage2)

print("push data data through the pipeline by calling producer")
pipeline_producer(stage1, 10)


def pipeline_stage_broadcaster(next_stage_coroutines):
    for _sink in next_stage_coroutines:
        _sink.send(None)
    while True:
        print("stage broadcast yield")
        value = (yield 'Broadcasting')
        print("stage broadcasting")
        for _sink in next_stage_coroutines:
            _sink.send(value)


print("\ncreate a data pipeline with broadcasting coroutines...")
stage_consumer1 = pipeline_stage_consumer("consumer1: x^2 + 1 =")
stage_consumer2 = pipeline_stage_consumer("consumer2: x^2 + 1 =")
stage_broadcaster = pipeline_stage_broadcaster([stage_consumer1, stage_consumer2])
stage2 = pipeline_stage_two(stage_broadcaster)
stage1 = pipeline_stage_one(stage2)

print("again push data data through the pipeline by calling producer")
pipeline_producer(stage1, 10)
