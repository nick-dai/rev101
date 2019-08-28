CC=gcc
CFLAGS=-fno-pie -O0 -m32 -fno-stack-protector
SRC=00_function.c 01_return.c 02_local_variables.c 03_calling_convention.c 04_global_variables.c 05_conditional.c 06_loop.c
BIN = $(patsubst %.c,%,$(SRC))

all: $(BIN)

clean:
	rm -f $(BIN)

.PHONY: all clean
