from django.db import models
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.utils import timezone

from django.contrib.auth import get_user_model
User = get_user_model()


class PreApplicationForm(models.Model):

    class Meta:
        verbose_name = _("Pre-Application Form")
        verbose_name_plural = _("Pre-Application Forms")
        ordering = ["id"]

    history = HistoricalRecords()

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="pre_app_form")

    created = models.DateTimeField(_("Created at"), default=timezone.now)

    # Basic Information

    first_name = models.CharField(_("First Name"), max_length=255)
    middle_name = models.CharField(
        _("Middle Name"), max_length=255, blank=True, null=True)
    last_name = models.CharField(_("Last Name"), max_length=255)
    email = models.EmailField(_("Email"), max_length=255, unique=True)
    phone = models.CharField(_("Phone"), max_length=255)
    desired_level_of_study = models.CharField(
        _("Desired Level of Study"), max_length=255, blank=True, null=True)
    desired_field_of_study = models.CharField(
        _("Desired Field of Study"), max_length=255, blank=True, null=True)
    total_number_of_visa_needed = models.CharField(
        _("Total Number of Visa Needed"), max_length=5, default=1)

    # Personal Information

    date_of_birth = models.DateField(_("Date of Birth"), blank=True, null=True)
    gender = models.CharField(
        _("Gender"), max_length=100, null=True, blank=True)
    marital_status = models.CharField(
        _("Marital Status"), max_length=255, blank=True, null=True)

    # Mailing Address

    address_line_1 = models.CharField(
        _("Address Line 1"), max_length=255, blank=True, null=True)
    address_line_2 = models.CharField(
        _("Address Line 2"), max_length=255, blank=True, null=True)
    city = models.CharField(_("City"), max_length=255, blank=True, null=True)
    state = models.CharField(_("State"), max_length=255, blank=True, null=True)
    zip_code = models.CharField(
        _("Zip Code"), max_length=255, blank=True, null=True)
    country = models.CharField(
        _("Country"), max_length=255, blank=True, null=True)

    # Permanent Address

    perma_address_line_1 = models.CharField(
        _("Address Line 1"), max_length=255, blank=True, null=True)
    perma_address_line_2 = models.CharField(
        _("Address Line 2"), max_length=255, blank=True, null=True)
    perma_city = models.CharField(
        _("City"), max_length=255, blank=True, null=True)
    perma_state = models.CharField(
        _("State"), max_length=255, blank=True, null=True)
    perma_zip_code = models.CharField(
        _("Zip Code"), max_length=255, blank=True, null=True)
    perma_country = models.CharField(
        _("Country"), max_length=255, blank=True, null=True)

    # Passport

    passport_number = models.CharField(
        _("Passport Number"), max_length=255, null=True, blank=True)
    passport_issue_date = models.DateField(
        _("Passport Issue Date"), null=True, blank=True)
    passport_expiry_date = models.DateField(
        _("Passport Expiry Date"), null=True, blank=True)
    passport_issue_country = models.CharField(
        _("Passport Issue Country"), max_length=255, null=True, blank=True)
    city_of_birth = models.CharField(
        _("City of Birth"), max_length=255, null=True, blank=True)
    country_of_birth = models.CharField(
        _("Country of Birth"), max_length=255, null=True, blank=True)

    # Nationality

    nationality = models.CharField(
        _("Nationality"), max_length=255, null=True, blank=True)
    country_of_citizenship = models.CharField(
        _("Country of Citizenship"), max_length=255, null=True, blank=True)
    are_you_citizen_of_more_than_one_country = models.BooleanField(
        _("Are you a citizen of more than one country?"), default=False)
    names_of_countries_of_citizenship = models.CharField(
        _("Names of Countries of Citizenship"), max_length=255, null=True, blank=True)
    are_you_living_in_other_country = models.BooleanField(
        _("Are you living and studying in any other country?"), default=False)
    names_of_countries_living_in = models.CharField(
        _("Names of Countries Living in"), max_length=255, null=True, blank=True)

    # Background Information

    has_applied_for_immigration = models.BooleanField(
        _("Has applicant applied for any type of immigration into any country?"), default=False)
    has_been_refused_Visa = models.BooleanField(
        _("Has applicant Visa refusal for any country?"), default=False)
    has_been_convicted = models.BooleanField(
        _("Has applicant ever been convicted of a criminal offence?"), default=False)

    # Emergency Contact
    emergency_contact_name = models.CharField(
        _("Emergency Contact Name"), max_length=255, null=True, blank=True)
    emergency_contact_phone = models.CharField(
        _("Emergency Contact Phone"), max_length=255, null=True, blank=True)
    emergency_contact_email = models.EmailField(
        _("Emergency Contact Email"), max_length=255, null=True, blank=True)
    emergency_contact_relationship = models.CharField(
        _("Emergency Contact Relationship"), max_length=255, null=True, blank=True)

    # Dependents Information

    dependents = models.JSONField(
        _("Dependents"), null=True, blank=True)

    # Parents' Information

    parents = models.JSONField(
        _("Parents"), null=True, blank=True)

    # Academic Qualifications

    # 2a) Education

    highest_education_level = models.CharField(
        _("Highest Education Level"), max_length=255, null=True, blank=True)
    country_of_education = models.CharField(
        _("Country of Education"), max_length=255, null=True, blank=True)

    # 2b) Grade 10th or equivalent

    grade_10th_or_equivalent = models.JSONField(
        _("Grade 10th or equivalent"), null=True, blank=True)

    grade_10th_subjects = models.JSONField(
        _("Grade 10th Subjects"), null=True, blank=True)

    # 2c) Grade 12th or equivalent

    grade_12th_or_equivalent = models.JSONField(
        _("Grade 12th or equivalent"), null=True, blank=True)

    grade_12th_subjects = models.JSONField(
        _("Grade 12th Subjects"), null=True, blank=True)

    # 2d) Undergraduate Degree

    undergraduate_degree_or_equivalent = models.JSONField(
        _("Undergraduate Degree or equivalent"), null=True, blank=True)

    undergraduate_degree_subjects = models.JSONField(
        _("Undergraduate Degree Subjects"), null=True, blank=True)

    # 2e) Graduate Degree

    graduate_degree_or_equivalent = models.JSONField(
        _("Graduate Degree or equivalent"), null=True, blank=True)

    graduate_degree_subjects = models.JSONField(
        _("Graduate Degree Subjects"), null=True, blank=True)

    # Work Experience

    work_experience = models.JSONField(
        _("Work Experience"), null=True, blank=True)

    # Tests

    english_proficiency = models.CharField(
        _("English Proficiency"), max_length=255, null=True, blank=True)

    english_proficiency_score = models.CharField(
        _("English Proficiency Score"), max_length=255, null=True, blank=True)

    english_proficiency_date_of_examination = models.DateField(
        _("English Proficiency Test Date"), null=True, blank=True)

    english_proficiency_trf_no = models.CharField(
        _("English Proficiency TRF No."), max_length=255, null=True, blank=True)

    english_proficiency_waivers = models.BooleanField(
        _("English Proficiency Waiver?"), default=False)
    english_proficiency_listening = models.CharField(
        _("English Proficiency Listening"), max_length=5, null=True, blank=True)
    english_proficiency_speaking = models.CharField(
        _("English Proficiency Speaking"), max_length=5, null=True, blank=True)
    english_proficiency_reading = models.CharField(
        _("English Proficiency Reading"), max_length=5, null=True, blank=True)
    english_proficiency_writing = models.CharField(
        _("English Proficiency Writing"), max_length=5, null=True, blank=True)

    # 4d) SAT

    sat_score = models.CharField(
        _("SAT Score"), max_length=5, null=True, blank=True)
    sat_date_of_examination = models.DateField(
        _("Date of Examination"), null=True, blank=True)
    sat_ebrw = models.CharField(
        _("SAT EBRW"), max_length=5, null=True, blank=True)
    sat_math = models.CharField(
        _("SAT Math"), max_length=5, null=True, blank=True)
    sat_reading = models.CharField(
        _("SAT Reading"), max_length=5, null=True, blank=True)
    sat_writing = models.CharField(
        _("SAT Writing"), max_length=5, null=True, blank=True)

    # 4e) ACT

    act_score = models.CharField(
        _("ACT Score"), max_length=5, null=True, blank=True)
    act_date_of_examination = models.DateField(
        _("Date of Examination"), null=True, blank=True)
    act_english = models.CharField(
        _("ACT English"), max_length=5, null=True, blank=True)
    act_math = models.CharField(
        _("ACT Math"), max_length=5, null=True, blank=True)
    act_reading = models.CharField(
        _("ACT Reading"), max_length=5, null=True, blank=True)
    act_science = models.CharField(
        _("ACT Science"), max_length=5, null=True, blank=True)
    act_writing = models.CharField(
        _("ACT Writing"), max_length=5, null=True, blank=True)

    # Extracurricular Activities

    eca_specific_achievements = models.JSONField(
        _("Specific Extracurricular Achievements"), null=True, blank=True)

    eca_activities = models.JSONField(
        _("Extracurricular Activities"), null=True, blank=True)

    # Gap Explanation

    has_gap = models.BooleanField(_("Has Gap?"), default=False)
    gap_explanation = models.TextField(
        _("Gap Explanation"), null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
