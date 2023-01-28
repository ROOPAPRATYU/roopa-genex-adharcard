const btn = document.querySelector('.push-to-add');
const btn1= document.querySelector('.input2')
let counter = 1;

btn.onclick = e => {
  e.preventDefault();
  
  let repeatingField = document.querySelector('.reapiting');
  
  let newRepeating = document.createElement('selection');
  newRepeating.className = 'repeating';
  
  let repeatingForm = `
      
    <div>
        <h2 class="head1">COMPANY ${1 + counter} DETAILS</h2>
        <div class="rep">
        <div>
        <span class="sp">company name </span>
        <input type="text" name="heading[${1 + counter}]" id="r1" placeholder="enter comapany name" required/>
        </div>
      
      

      <div>
      <span class="sp">joining date </span>
        <input type="date" name="date1[${1 + counter}]" id="r2"  placeholder="joining date" required/>
      
      </div>
      <div>
      <span class="sp">last date </span>
        <input type="date" name="date2[${1 + counter}]" id="r3" placeholder="last date" required />
      </div>
      
      
      
  `;
  
  newRepeating.innerHTML = repeatingForm;
  btn.previousElementSibling.appendChild(newRepeating);
  counter += 1

}

