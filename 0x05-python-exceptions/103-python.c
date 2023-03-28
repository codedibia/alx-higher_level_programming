#include <stdio.h>
#include <stdlib.h>

void print_python_list(PyObject *p)
{
	int size, i;
	const char *type;
	PyObject *item;

	if (!PyList_Check(p)) {
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}

	size = PyList_Size(p);
	type = (p->ob_type)->tp_name;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	printf("[*] Elements of the Python List:\n");

	for (i = 0; i < size; i++) {
		item = PyList_GetItem(p, i);
		type = (item->ob_type)->tp_name;
		printf("Element %d: %s\n", i, type);
		fflush(stdout);
	}
}


void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;
	const char *type;

	if (!PyBytes_Check(p)) {
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}

	size = PyBytes_Size(p);
	type = (p->ob_type)->tp_name;

	printf("[.] bytes object info\n");
	printf("  [+] size: %ld\n", size);
	printf("  [+] trying string: %s\n", PyBytes_AsString(p));

	if (size > 10) {
		size = 10;
	}

	str = PyBytes_AsString(p);

	printf("  [+] first %ld bytes: ", size);

	for (i = 0; i < size; i++) {
		printf("%02x", (unsigned char)str[i]);

		if (i == size - 1) {
			printf("\n");
		} else {
			printf(" ");
		}
	}

	fflush(stdout);
}void print_python_float(PyObject *p)
{
	char *str;
	const char *type;

	if (!PyFloat_Check(p)) {
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
		return;
	}

	type = (p->ob_type)->tp_name;

	printf("[.] float object info\n");
	printf("  [+] value: %s\n", PyOS_double_to_string(PyFloat_AsDouble(p), 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
	fflush(stdout);
}
