// const Utils = require('../utils/index.js')
// import {Utils} from '../utils/index.js'

const Utils = require('../utils/index');

var p = new Promise((res,rej)=>{
	let a = 4;
	res(a);
});

p.then((a)=>{
	a = 9;
	console.log(a);
}).then((a)=>{
	a = 14;
	console.log(a);
});

var params = {
	'iteraciones'	: 5000,
	'mating_length'	: 50,
	'n_population'	: 50,
	'n_selected'	: 4,
	'p_cross'		: 0.8,
	'p_mut'			: 0.1,
	'blx_a'			: 0.5,
}

function f(x,y){
	return -Math.cos(x) * Math.cos(y) * Math.exp(-((x - Math.PI) ** 2) - ((y - Math.PI) ** 2))
}

var population = Utils.create_random_matrix(-10,10,[params.n_population,2], false)
// console.table(population);

for (let iter = 0; iter < params.iteraciones; iter++) {
	let apptitudes = new Array(params.n_population);
	population.map(([x,y], i)=>{
		apptitudes[i]=f(x,y);
		// state[i].push(f(x,y));
	});
	// console.table(population.combine_columns(apptitudes));

	// Creation of mating pool
	var mates_selected = Utils.create_random_matrix(0,params.n_population-1, [params.mating_length,2]);
	// console.table(mates_selected);
	var mating_pool = new Array(params.mating_length);

	mates_selected.map(([p1,p2],i)=>{
		// console.log(apptitudes[p1], apptitudes[p2])
		let winner = Math.min(apptitudes[p1], apptitudes[p2]);
		console.log("Ganador:", winner, apptitudes[p1], apptitudes[p2]);
		let index  = apptitudes.indexOf(winner);
		mating_pool[i] = index;
	});
	// population = []
	// console.table(mates_selected.combine_columns(mating_pool));

	// Reproduction phase
	var couples = Utils.create_random_matrix(0,params.mating_length-1, [params.mating_length,2]);
	// console.table(couples);
	var new_population = new Array(params.n_population);
	couples.map(([m1,m2],i)=>{
		if (Math.random() < params.p_cross ){
			let [idp1,idp2] = [mating_pool[m1], mating_pool[m2]]
			console.log("Padres:\t",population[idp1],population[idp2], idp1, idp2)
			let child = Utils.blx_cross(population[idp1],population[idp2],params.blx_a);
			console.log("Cross:\t",child,i);
			new_population[i] = child;
		}
		if (Math.random() < params.p_mut){
			console.log("Mutacion:\t",new_population[i]);
			Utils.uniform_mut(new_population[i])
		}
	});
	population = new_population;

	// console.table(population)
	
}
console.table(population)



// mating_pool = create_random_matrix()
// console.table(mating_pool);