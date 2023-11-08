import React, { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useParams } from "react-router-dom";
import OpenModalButton from "../OpenModalButton";
import {
  readUserCartThunk,
  incrementItemThunk,
  decrementItemThunk,
} from "../../store/shoppingCart";
import DeleteCartItemModal from "../DeleteCartItemModal";
import "./ShoppingCart.css";

const ShoppingCart = () => {
  const dispatch = useDispatch();
  const { userId } = useParams();
  const userCart = useSelector((state) => Object.values(state.cart.cart));
  const sessionUser = useSelector((state) => state.session.user);

  useEffect(() => {
    if (sessionUser) {
      dispatch(readUserCartThunk(sessionUser.id));
    }
  }, [dispatch, sessionUser]);

  let subtotalCalc = 0;
  if (userCart && userCart[0] instanceof Array) {
    subtotalCalc = userCart[0]?.reduce(
      (total, item) => total + item.guitar.price * item.quantity,
      0
    );
  }

  return (
    <div className="shopping-cart-container">
      <div className="cart-items-container">
        <h1>{sessionUser.first_name}'s Gigbag</h1>
        <ul>
          {userCart[0] &&
            userCart[0].length > 0 &&
            userCart[0].map((item) => (
              <li key={item.id} className="cart-item">
                <div className="cart-image">
                  {item.images && <img src={item.images[0].url} alt="Guitar" />}
                </div>
                <div className="cart-info-section">
                  <div>
                    {item.guitar.year} {item.guitar.make} {item.guitar.model}
                  </div>
                  <div>${item.guitar.price}</div>
                </div>
                <div>
                  <OpenModalButton
                    className="delete-button"
                    buttonText="Delete"
                    modalComponent={
                      <DeleteCartItemModal
                        guitarId={item.guitar.id}
                        userId={sessionUser.id}
                      />
                    }
                  />
                  <div>
                    <button
                      onClick={() => {
                        dispatch(
                          decrementItemThunk(sessionUser.id, item.guitar.id)
                        ).then(() => {
                          dispatch(readUserCartThunk(sessionUser.id));
                        });
                      }}
                      disabled={item.quantity < 2}
                    >
                      -
                    </button>
                    Quantity: {item.quantity}
                    <button
                      onClick={() => {
                        dispatch(
                          incrementItemThunk(sessionUser.id, item.guitar.id)
                        ).then(() => {
                          dispatch(readUserCartThunk(sessionUser.id));
                        });
                      }}
                      disabled={item.quantity > 9}
                    >
                      +
                    </button>
                  </div>
                </div>
              </li>
            ))}
        </ul>
      </div>
      <div className="price-checkout-container">
        <h2>Subtotal: ${subtotalCalc}</h2>
        <button
          onClick={() => {
            alert("Feature Coming Soon");
          }}
        >
          Checkout
        </button>
      </div>
    </div>
  );
};

export default ShoppingCart;
