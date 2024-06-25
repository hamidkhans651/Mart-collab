from sqlmodel import Session, select
from fastapi import HTTPException
import stripe
from app.models.order_models import Order
from app.models.payment_models import Payment, AdvancePayment, PaymentForm, RemainingPaymentModel
from app.settings import STRIPE_SECRET_KEY


# stripe.api_key = STRIPE_SECRET_KEY


def create_payment(payment_intent, order, session: Session):
    # Create the payment record for online payment
    payment = Payment(
        payment_intent_id=payment_intent.id,
        is_completed=True,
        order_id=order.order_id,
        total_price=order.total_price,
        payment_status=payment_intent.status,
        payment_method=payment_intent.payment_method_types[0]
    )
    session.add(payment)
    session.commit()
    session.refresh(payment)
    print(f"Payment Details: {payment}")


def read_payment_details(order_id: int, session: Session) -> Payment:
    payment_table = session.exec(select(Payment).where(
        Payment.order_id == order_id)).one_or_none()
    if payment_table is None:
        raise HTTPException(
            status_code=404, detail=f"Payment table not found from this order id: {order_id}")
    return payment_table

