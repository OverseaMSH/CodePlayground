import React, { useEffect } from 'react';
import { isIOS } from 'react-device-detect';
import './styles.scss';

import cardsInfo from '../../constants/cardsInfo';

function OrderCardRenderer({ order }) {
  return (
    <div className={'cardContainer'}>
      <span className={'icon'}>
        {order.enableImg ? (
          <img
            src={order.isActive ? order.enableImg : order.disableImg}
            className={'cardImg'}
            alt="loading"
          />
        ) : (
          <order.icon isActive={order.isActive} />
        )}
      </span>
      <span className={'text'}>
        <div className={'title'}>
          <span>{order.title}</span>
        </div>
        <div className={'description'}>
          <span>{order.description}</span>
        </div>
      </span>
    </div>
  );
}

export default function OrderSlider({ orderStatus }) {
  useEffect(() => {
    let elmnt = document.getElementById('card_true');
    if (elmnt) elmnt.scrollIntoView({ behavior: 'smooth', inline: 'center' });

    // question: implement cards update on changing states
  }, [orderStatus]);

  const keys = Object.keys(cardsInfo);
  const currentKey = keys[orderStatus];

  if (cardsInfo.pending === cardsInfo[Object.keys(cardsInfo)[orderStatus]]) {
    cardsInfo.pending.isActive = true
  }
  if (cardsInfo.sending === cardsInfo[Object.keys(cardsInfo)[orderStatus]]) {
    cardsInfo.sending.isActive = true
  }
  if (cardsInfo.delivering === cardsInfo[Object.keys(cardsInfo)[orderStatus]]) {
    cardsInfo.delivering.isActive = true
  }
  if (cardsInfo.delivered === cardsInfo[Object.keys(cardsInfo)[orderStatus]]) {
    cardsInfo.delivered.isActive = true
  }

  const setCurrentCard = (orderStatus) => {
    switch (orderStatus) {
      case 0:
        return (
          <div
            className={'card'}
            id={cardsInfo.pending.isActive ? 'card_true' : ''}
          >
            <OrderCardRenderer order={cardsInfo.pending} />
          </div>
        );
      case 1:
        return (
          <div
            className={'card'}
            id={cardsInfo.sending.isActive ? 'card_true' : ''}
          >
            <OrderCardRenderer order={cardsInfo.sending} />
          </div>
        );
      case 2:
        return (
          <div
            className={'card'}
            id={cardsInfo.delivering.isActive ? 'card_true' : ''}
          >
            <OrderCardRenderer order={cardsInfo.delivering} />
          </div>
        );
      case 3:
        return (
          <div
            className={'card'}
            id={cardsInfo.delivered.isActive ? 'card_true' : ''}
          >
            <OrderCardRenderer order={cardsInfo.delivered} />
          </div>
        );
      default:
        return null;
    }
  };

  const currentCard = setCurrentCard(orderStatus);
  return (
    <div
      id="order_slider"
      className={'orderSlider'}
      onTouchStart={() => {
        if (isIOS) {
          document.ontouchmove = event => {
            event.stopPropagation();
          };
        }
      }}
      onTouchEnd={() => {
        if (isIOS) {
          document.ontouchmove = event => {
            event.preventDefault();
          };
        }
      }}
    >
      {keys.map((key, index) => {
        const cardInfo = cardsInfo[key];
        const isActive = index === orderStatus;

        return (
          <div
            key={key}
            className={'card'}
            id={isActive ? 'card_true' : ''}
          >
            <OrderCardRenderer order={{ ...cardInfo, isActive }} />
          </div>
        );
      })}

    </div>
  );
}
