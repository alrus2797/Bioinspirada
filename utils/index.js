class Utils{
	static getRndNumber(min, max, is_int = true) {
		let random_part = Math.random() * (max + 1 - min);
		return ((is_int) ? Math.floor(random_part) : random_part) + min;
	}

	static create_random_matrix(min, max, shape, get_int = true){
		let a = [];
		let [rows, cols] = shape
		for (let i = 0; i < rows; i++) {
			let c = [];
			for (let j = 0; j < cols; j++) {
				c.push(Utils.getRndNumber(min, max, get_int));
			}
			a.push(c);
		}
		return a;
	}

	static blx_cross(c1, c2, alpha){
		let beta = Utils.getRndNumber(alpha, alpha + 1);
		beta = 1.262
		return c1.map((c,i)=>{
			return c + beta * (c2[i] - c);
		});
	}

	static uniform_mut(c1){
		let pos = Utils.getRndNumber(0,c1.length-1);
		c1[pos] = Utils.getRndNumber(-10,10, false);
		return c1;
	}
}

Number.prototype.toFixedSpecial = function(n) {
	var str = this.toFixed(n);
	if (str.indexOf('e+') === -1)
		return str;

	// if number is in scientific notation, pick (b)ase and (p)ower
	str = str.replace('.', '').split('e+').reduce(function(p, b) {
		return p + Array(b - p.length + 2).join(0);
	});

	if (n > 0)
		str += '.' + Array(n + 1).join(0);

	return str;
};

Array.prototype.sample = function(){
	return this[Math.floor(Math.random()*this.length)];
	}

Array.prototype.pop_sample = function(){
	let val = this.sample();
	return this[Math.floor(Math.random()*this.length)];
	}

Array.prototype.combine_columns = function(arr2){
	return this.map((row,i) => {
		return Array.isArray(row) ? row.concat(arr2[i]) : [row].concat(arr2[i]);
	});
}


module.exports = Utils;

// exports.Utils = Utils;
// exports.Number.prototype.toFixedSpecial = Number.prototype.toFixedSpecial;