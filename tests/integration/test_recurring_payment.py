import pytest
import time

from .base_integration_test import BaseIntegrationTest
from tests.sampleresponse.recurring_payment import recurring_payment_response


class TestRecurringPayment(BaseIntegrationTest):
    @pytest.fixture
    def RecurringPayment(self, xendit_instance):
        return xendit_instance.RecurringPayment

    def test_create_recurring_payment_return_correct_keys(self, RecurringPayment):
        recurring_payment = RecurringPayment.create_recurring_payment(
            external_id=f"recurring_{int(time.time())}",
            payer_email="test@x.co",
            description="Test Curring Payment",
            amount=100000,
            interval="MONTH",
            interval_count=1,
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            recurring_payment, recurring_payment_response()
        )

    def test_get_recurring_payment_return_correct_keys(self, RecurringPayment):
        recurring_payment = RecurringPayment.get_recurring_payment(
            id="5f059f3bfe20a578a49d8072",
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            recurring_payment, recurring_payment_response()
        )

    def test_edit_recurring_payment_return_correct_keys(self, RecurringPayment):
        recurring_payment = RecurringPayment.edit_recurring_payment(
            id="5f059f3bfe20a578a49d8072", interval_count=2
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            recurring_payment, recurring_payment_response()
        )

    def test_stop_recurring_payment_return_correct_keys(self, RecurringPayment):
        recurring_payment = RecurringPayment.create_recurring_payment(
            external_id=f"recurring_{int(time.time())}",
            payer_email="test@x.co",
            description="Test Curring Payment",
            amount=100000,
            interval="MONTH",
            interval_count=1,
        )

        recurring_payment = RecurringPayment.stop_recurring_payment(
            id=recurring_payment.id
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            recurring_payment, recurring_payment_response()
        )

    def test_pause_and_resume_recurring_payment_return_correct_keys(
        self, RecurringPayment
    ):
        recurring_payment = RecurringPayment.pause_recurring_payment(
            id="5f059f3bfe20a578a49d8072",
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            recurring_payment, recurring_payment_response()
        )

        recurring_payment = RecurringPayment.resume_recurring_payment(
            id="5f059f3bfe20a578a49d8072",
        )

        self.assert_returned_object_has_same_key_as_sample_response(
            recurring_payment, recurring_payment_response()
        )
