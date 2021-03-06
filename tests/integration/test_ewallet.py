import pytest
import time
import xendit

from .base_integration_test import BaseIntegrationTest

from xendit import EWalletType

from tests.sampleresponse.ewallet import ovo_payment_response
from tests.sampleresponse.ewallet import ovo_payment_status_response
from tests.sampleresponse.ewallet import dana_payment_response
from tests.sampleresponse.ewallet import dana_payment_status_response
from tests.sampleresponse.ewallet import linkaja_payment_response
from tests.sampleresponse.ewallet import linkaja_payment_status_completed_response
from tests.sampleresponse.ewallet import linkaja_payment_status_expired_response


class TestEWallet(BaseIntegrationTest):
    @pytest.fixture
    def EWallet(self, xendit_instance):
        return xendit_instance.EWallet

    def test_create_ovo_payment_return_correct_keys(self, EWallet):
        ovo_payment = EWallet.create_ovo_payment(
            external_id=f"ovo-ewallet-testing-id-{int(time.time())}",
            amount="80001",
            phone="08123123123",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ovo_payment, ovo_payment_response()
        )

    def test_create_dana_payment_return_correct_keys(self, EWallet):
        dana_payment = EWallet.create_dana_payment(
            external_id=f"dana-ewallet-test-{time.time()}",
            amount="1001",
            callback_url="https://my-shop.com/callbacks",
            redirect_url="https://my-shop.com/home",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            dana_payment, dana_payment_response()
        )

    def test_create_linkaja_payment_return_correct_keys(self, EWallet):
        # Object Creation Test
        items = []
        item = xendit.EWallet.helper_create_linkaja_item(
            id="123123", name="Phone Case", price=100000, quantity=1
        )
        items.append(item)

        linkaja_payment = EWallet.create_linkaja_payment(
            external_id=f"linkaja-ewallet-test-{time.time()}",
            phone="089911111111",
            amount=300000,
            items=items,
            callback_url="https://my-shop.com/callbacks",
            redirect_url="https://xendit.co/",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            linkaja_payment, linkaja_payment_response()
        )

        # Dictionary Creation Test
        linkaja_payment = EWallet.create_linkaja_payment(
            external_id=f"linkaja-ewallet-test-{time.time()}",
            phone="089911111111",
            amount=300000,
            items=[
                {"id": "123123", "name": "Phone Case", "price": 100000, "quantity": 1}
            ],
            callback_url="https://my-shop.com/callbacks",
            redirect_url="https://xendit.co/",
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            linkaja_payment, linkaja_payment_response()
        )

    def test_get_ovo_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            external_id="ovo-ewallet-testing-id-1234", ewallet_type=EWalletType.OVO,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, ovo_payment_status_response()
        )

    def test_get_dana_payment_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            external_id="dana-ewallet-test-1234", ewallet_type=EWalletType.DANA,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, dana_payment_status_response()
        )

    def test_get_completed_linkaja_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            external_id="linkaja-ewallet-test-1234", ewallet_type=EWalletType.LINKAJA,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, linkaja_payment_status_completed_response()
        )

    def test_get_failed_linkaja_payment_status_return_correct_keys(self, EWallet):
        ewallet = EWallet.get_payment_status(
            external_id="linkaja-ewallet-test-123", ewallet_type=EWalletType.LINKAJA,
        )
        self.assert_returned_object_has_same_key_as_sample_response(
            ewallet, linkaja_payment_status_expired_response()
        )
