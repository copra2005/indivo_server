from base import report_content_to_test_docs

_TEST_PROCEDURES = [
    """
<Models xmlns="http://indivo.org/vocab/xml/documents#">
    <Model name="Procedure">
        <Field name="date">2011-02-15T12:00:00Z</Field>
        <Field name="notes">Went great!</Field>
        <Field name="name_title">Appendectomy</Field>
        <Field name="name_code_title">Appendectomy</Field>
        <Field name="name_code_system">http://purl.bioontology.org/ontology/SNOMEDCT/</Field>
        <Field name="name_code_identifier">80146002</Field>
        <Field name="status_title">Complete</Field>
        <Field name="status_code_title">Complete</Field>
        <Field name="status_code_system">http://purl.bioontology.org/ontology/SNOMEDCT/</Field>
        <Field name="status_code_identifier">385658003</Field>
        <Field name="provider_dea_number">325555555</Field>
        <Field name="provider_npi_number">5235235</Field>
        <Field name="provider_email">joshua.mandel@fake.emailserver.com</Field>
        <Field name="provider_name_given">Josuha</Field>
        <Field name="provider_name_family">Mandel</Field>
        <Field name="provider_tel_1_type">w</Field>
        <Field name="provider_tel_1_number">1-235-947-3452</Field>
        <Field name="provider_tel_1_preferred_p">True</Field>
    </Model>
</Models>
""",

"""
<Models xmlns="http://indivo.org/vocab/xml/documents#">
    <Model name="Procedure">
        <Field name="date">2011-05-15T12:00:00Z</Field>
        <Field name="notes">Went OK</Field>
        <Field name="name_title">Appendectomy</Field>
        <Field name="name_code_title">Appendectomy</Field>
        <Field name="name_code_system">http://purl.bioontology.org/ontology/SNOMEDCT/</Field>
        <Field name="name_code_identifier">80146002</Field>
        <Field name="status_title">Complete</Field>
        <Field name="status_code_title">Complete</Field>
        <Field name="status_code_system">http://purl.bioontology.org/ontology/SNOMEDCT/</Field>
        <Field name="status_code_identifier">385658003</Field>
        <Field name="provider_dea_number">325555555</Field>
        <Field name="provider_npi_number">5235235</Field>
        <Field name="provider_email">joshua.mandel@fake.emailserver.com</Field>
        <Field name="provider_name_given">Josuha</Field>
        <Field name="provider_name_family">Mandel</Field>
        <Field name="provider_tel_1_type">w</Field>
        <Field name="provider_tel_1_number">1-235-947-3452</Field>
        <Field name="provider_tel_1_preferred_p">True</Field>
    </Model>
</Models>
""",
]

TEST_PROCEDURES = report_content_to_test_docs(_TEST_PROCEDURES)
