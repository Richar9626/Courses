import pytest
from unittest.mock import patch  # Change random choice in my test
import sys
import os

from order_processing import OrderProcessing


@pytest.fixture
def order_system():
    """
    Fixture to provide an instance of the OrderProcessing class for testing.
    """
    return OrderProcessing()

#classes were needed in unitesting, keeping that for reusability
class TestOrderProcessing:
    def test_create_order(self, order_system):
        """
        Test the creation of an order in the order system.

        Verifies that the `create_order` method correctly creates an order with 
        the specified ID and amount, and sets the initial status to "pending".
        """
        order = order_system.create_order(101, 50)
        assert order["amount"] == 50
        assert order["status"] == "pending"

    @pytest.mark.parametrize("order_id, amount, expected_exception", [
        (102, 100, None),
        (102, -50, ValueError),
        (102, 0, ValueError)
    ])

    def test_create_order_scenarios(self, order_system, order_id, amount, expected_exception):
        """
        Test multiple scenarios for the `create_order` method.

        Verifies that valid inputs create an order successfully, while invalid 
        inputs raise the expected exceptions.
        """
        if expected_exception:
            with pytest.raises(expected_exception):
                order_system.create_order(order_id, amount)
        else:
            order = order_system.create_order(order_id, amount)
            assert order["amount"] == amount


    def test_get_order_status(self, order_system):
        """
        Test the retrieval of an order's status.

        Verifies that the correct status is returned for existing orders, and 
        "not found" is returned for non-existent orders.
        """
        order = order_system.create_order(101, 50)
        order_status = order_system.get_order_status(101)
        order_status_fail = order_system.get_order_status(200)
        assert order_status == "pending"
        assert order_status_fail == "not found"

    @pytest.mark.skip(reason="Payment processing is slow, skipping for now")
    def test_process_payment(self, order_system):
        """
        Test the payment processing function.

        Skipped intentionally. Verifies that the function returns either True 
        or False, as payment outcomes are randomized.
        """
        order_system.create_order(104, 200)  # Create an order
        assert order_system.process_payment(104) in [True, False]  # Payment can be successful or failed

    @pytest.mark.slow  # Marked as a slow test, useful for running only when needed
    def test_slow_payment_processing(self, order_system):
        """
        Test the actual payment processing flow.

        Verifies that the payment status changes to either "paid" or "failed" 
        after processing.
        """
        order_system.create_order(105, 150)  # Create an order
        result = order_system.process_payment(105)  # Process payment
        assert result in [True, False]  # Ensure result is either True or False
        assert order_system.get_order_status(105) in ["paid", "failed"]  # Order should have updated status

    def test_mocked_payment_processing(self, order_system):
        """
        Test payment processing with a mocked random.choice function.

        Mocks the payment outcome to always return True (successful payment) 
        and verifies that the order status is updated correctly.
        """
        order_system.create_order(106, 300)  # Create an order

        # Patch the random.choice function to always return True (force successful payment)
        with patch("order_processing.random.choice", return_value=True):  
            assert order_system.process_payment(106) is True  # Payment should succeed
            assert order_system.get_order_status(106) == "paid"  # Order status should be updated to "paid"