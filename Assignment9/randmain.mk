randmain: randmain.o randcpuid.o randlibhw.so randlibsw.so
	$(CC) $(CFLAGS) randmain.o randcpuid.o -ldl -Wl,-rpath=$(PWD) -o randmain

randmain.o: randmain.c
	$(CC) $(CFLAGS) -shared-libgcc -c randmain.c -o randmain.o

randcpuid.o: randcpuid.c
	$(CC) $(CFLAGS) -c randcpuid.c -o randcpuid.o

randlibhw.so: randlibhw.o
	$(CC) $(CFLAGS) -shared randlibhw.o -o randlibhw.so

randlibsw.so: randlibsw.o
	$(CC) $(CFLAGS) -shared randlibsw.o -o randlibsw.so

randlibhw.o: randlibhw.c
	$(CC) $(CFLAGS) -c -fPIC randlibhw.c -o randlibhw.o

randlibsw.o: randlibsw.c
	$(CC) $(CFLAGS) -c -fPIC randlibsw.c -o randlibsw.o