.PHONY: all

all: build_and_move

build_and_move:
	@echo "[pythonchess] Building the Stockfish binary."
	@cd lib/stockfish/src && make -j build COMP=clang
	@echo "[pythonchess] Moving the binary to bin/"
	@cp lib/stockfish/src/stockfish bin/stockfish

check_path_bin_exists:
	@echo "[pythonchess] Checking if bin/ exists."
	@if [ ! -d "bin/" ]; then mkdir -p bin; fi

# todo: add a check to verify is the stockfish code is already downloaded

# todo: add a check to verify if the stockfish binary is already built

# todo: add a check to verify if the stockfish binary is already moved to bin/

clean:
	@echo "[pythonchess] Cleaning up..."
	@cd lib/src && make clean
