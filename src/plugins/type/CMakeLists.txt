add_plugin (type
	    SOURCES type.h
		    type.c
		    types.h
		    types.c
	    LINK_ELEKTRA elektra-meta elektra-ease
	    ADD_TEST TEST_README)
