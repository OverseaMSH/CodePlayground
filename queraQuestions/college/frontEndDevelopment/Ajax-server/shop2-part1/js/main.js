document.addEventListener("DOMContentLoaded", function () {
	const productList = document.getElementById("product-list");
  
	function formatPrice(price) {
	  return Number(price).toLocaleString() + " تومان";
	}
  
	async function fetchProducts() {
	  try {
		const response = await fetch("http://localhost:3000/products");
		if (!response.ok) {
		  throw new Error("خطا در دریافت اطلاعات از سرور");
		}
  
		const products = await response.json();
  
		productList.innerHTML = "";
  
		products.forEach((product) => {
		  const productHTML = `
			<div class="product col-lg-4 col-md-6 mb-4">
			  <div class="card h-100">
				<a href="#">
				  <img
					class="card-img-top"
					src="${product.image}"
					alt="${product.title}"
				  />
				</a>
				<div class="card-body">
				  <h4 class="card-title">${product.title}</h4>
				  <h5 class="product-price">${formatPrice(product.price)}</h5>
				  <p class="card-text">${product.description}</p>
				</div>
				<div class="card-footer">
				  <button class="btn btn-light add-to-cart" data-product-id="${product.id}">
					افزودن به سبد خرید
				  </button>
				</div>
			  </div>
			</div>
		  `;
		  productList.insertAdjacentHTML("beforeend", productHTML);
		});
	  } catch (error) {
		console.error("خطا:", error);
		productList.innerHTML = `<p class="text-danger">خطایی در دریافت محصولات رخ داد.</p>`;
	  }
	}
  
	fetchProducts();
  });
  