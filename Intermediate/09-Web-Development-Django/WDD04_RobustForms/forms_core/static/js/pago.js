document.addEventListener('DOMContentLoaded', () => {
    const cardVisual = document.getElementById('creditCardVisual');
    const cardTypeIcon = document.getElementById('cardTypeIcon');

    const inputs = {
        name: { input: document.getElementById('id_titular'), display: document.getElementById('displayName'), default: 'NOMBRE COMPLETO' },
        number: { input: document.getElementById('id_numero_tarjeta'), display: document.getElementById('displayNumber'), default: '**** **** **** ****' },
        expiry: { input: document.getElementById('id_fecha_expiracion'), display: document.getElementById('displayExpiry'), default: 'MM/AA' },
        cvv: { input: document.getElementById('id_cvv'), display: document.getElementById('displayCVV'), default: '***' }
    };

    const updateDisplay = (key) => {
        const val = inputs[key].input.value.trim();
        inputs[key].display.innerText = val !== '' ? val : inputs[key].default;
    };

    inputs.name.input.addEventListener('input', () => updateDisplay('name'));

    inputs.number.input.addEventListener('input', (e) => {
        let val = e.target.value.replace(/\D/g, '');
        let valFormateado = val.match(/.{1,4}/g)?.join(' ') || '';
        e.target.value = valFormateado; 
        
        updateDisplay('number'); 

        if (val.startsWith('4')) {
            cardTypeIcon.className = 'bi bi-credit-card-2-front card-type-icon text-info';
        } else if (val.startsWith('5')) {
            cardTypeIcon.className = 'bi bi-credit-card-2-front card-type-icon text-warning';
        } else {
            cardTypeIcon.className = 'bi bi-credit-card-2-front card-type-icon';
        }
    });

    inputs.expiry.input.addEventListener('input', (e) => {
        let val = e.target.value.replace(/\D/g, '');
        if (val.length >= 2) {
            e.target.value = val.slice(0, 2) + '/' + val.slice(2, 4);
        } else {
            e.target.value = val;
        }
        updateDisplay('expiry');
    });

    inputs.cvv.input.addEventListener('input', () => updateDisplay('cvv'));

    inputs.cvv.input.addEventListener('focus', () => cardVisual.classList.add('flipped'));
    inputs.cvv.input.addEventListener('blur', () => cardVisual.classList.remove('flipped'));

    Object.keys(inputs).forEach(updateDisplay);

    
    const montoInput = document.getElementById('id_monto');
    const btnAmountDisplay = document.getElementById('btnAmountDisplay');

    if (montoInput && btnAmountDisplay) {
        montoInput.addEventListener('input', (e) => {
            const valor = parseFloat(e.target.value);
            if (!isNaN(valor)) {
                btnAmountDisplay.innerText = `$ ${valor.toFixed(2)}`;
            } else {
                btnAmountDisplay.innerText = `$ 0.00`;
            }
        });
    }
});