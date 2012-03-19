""" Indivo Document Processing. """

from django.conf import settings
import os
import functools
from lxml import etree

REGISTERED_SCHEMAS = {}

SCHEMA_NAME = 'schema'
SCHEMA_EXTENSIONS = ['.xsd']

TRANSFORM_NAME = 'transform'
TRANSFORM_EXTENSIONS = ['.xsl', '.xslt', '.py']

XSD_NS = 'http://www.w3.org/2001/XMLSchema'

class IndivoSchemaDir(object):
    def __init__(self, dir_path):
        self.dir_path = dir_path

        if not os.path.isdir(dir_path):
            self.schema_filename = None
            self.schema_ext = None
            self.transform_filename = None
            self.transform_ext = None
            return

        # Find a schema
        self.schema_filename, self.schema_ext = self.detect_file(SCHEMA_NAME, SCHEMA_EXTENSIONS)
        
        # Find a transform
        self.transform_filename, self.transform_ext = self.detect_file(TRANSFORM_NAME, TRANSFORM_EXTENSIONS)

    def is_valid(self):
        return self.schema_filename and self.schema_ext and self.transform_filename and self.transform_ext

    def detect_file(self, filebase, valid_extensions):
        for ext in valid_extensions:
            filename = filebase + ext
            path = os.path.join(self.dir_path, filename)
            if os.path.isfile(path):
                return (filebase, ext)
        return (None, None)

    def get_full_schema_path(self):
        try:
            return os.path.join(self.dir_path, self.schema_filename + self.schema_ext)
        except TypeError:
            return None

    def get_full_transform_path(self):
        try:
            return os.path.join(self.dir_path, self.transform_filename + self.transform_ext)
        except TypeError:
            return None

class IndivoSchemaLoader(object):

    def __init__(self, top):
        self.top = top

    def import_schemas(self):
        for schema_name, schema_etree, transform_func in self.discover_schema_dirs():
            self.register_schema(schema_name, schema_etree, transform_func)
    
    @classmethod
    def detect_schema_dir(cls, dir_path):
        """ Detects whether a directory is a properly-formatted datamodel.

        This is true if:
        
        * It contains a schema file (schema.xsd)

        * It contains a transform file of an appropriate type (transform.[xsl|xslt|py])

        *dir_path* must be an absolute path for this to work. Returns an instance of 
        IndivoSchemaDir

        """
        return IndivoSchemaDir(dir_path)

    @classmethod
    def register_schema(cls, schema_qn, validation_func, transformation_func):
        if REGISTERED_SCHEMAS.has_key(schema_qn):
            raise ValueError("The schema %s already exists: please choose a different name for your schema"%schema_qn)
        REGISTERED_SCHEMAS[schema_qn] = (validation_func, transformation_func)

    def discover_schema_dirs(self):
        for (dirpath, dirnames, filenames) in os.walk(self.top):
            schema_dir = self.detect_schema_dir(dirpath)
            if schema_dir.is_valid():
                dirnames = [] # we found a schema dir: don't look in subdirectories for others

                # Get the FQNs for top-level elements that we can validate with the schema
                if schema_dir.schema_ext == '.xsd':
                    fqn_handler = self._get_fqns_from_xsd

                fqns = fqn_handler(schema_dir)

                # Get the validation func
                if schema_dir.schema_ext == '.xsd':
                    validation_handler = self._get_validation_func_from_xsd
                    
                validation_func = validation_handler(schema_dir)

                # Get the transformation func
                if schema_dir.transform_ext == '.py':
                    handler = self._get_transform_func_from_py
                elif schema_dir.transform_ext.startswith('.xsl'):
                    transform_handler = self._get_transform_func_from_xslt

                transformation_func = transform_handler(schema_dir)
                
                # make sure to yield a separate entry for each top-level fqn
                for fqn in fqns:
                    yield (fqn, validation_func, transformation_func)

    def _get_fqns_from_xsd(self, schema_dir):
        fqns = []
        with open(schema_dir.get_full_schema_path(), 'r') as schema_file:
            schema = etree.parse(schema_file).getroot()

        target_ns = schema.get('targetNamespace')
        for el in schema.findall("{%s}element"%XSD_NS):
            fqns.append("%s%s"% (target_ns, el.get('name')))

        return fqns

    def _get_validation_func_from_xsd(self, schema_dir):
        with open(schema_dir.get_full_schema_path(), 'r') as schema_file:
            schema = etree.XMLSchema(etree.parse(schema_file))

        return schema.assertValid

    def _get_transform_func_from_py(self, schema_dir):
#        with open(schema_dir.get_full_transform_path(), 'r') as transform_file:
        # TODO
        pass

    def _get_transform_func_from_xslt(self, schema_dir):
        with open(schema_dir.get_full_transform_path(), 'r') as transform_file:
            return etree.XSLT(etree.parse(transform_file))

# get the core schemas
loader = IndivoSchemaLoader(settings.CORE_SCHEMA_LOC)
loader.import_schemas()

# get the contributed schemas
loader.top = settings.CONTRIB_SCHEMA_LOC
loader.import_schemas()
