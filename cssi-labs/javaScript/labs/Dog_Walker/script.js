// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Task 1
let dogName1 = "Steve";
let dogType1 = "beagle";

// Complete Task 1 Below



let dogName2 = "Joe";
let dogType2 = "bulldog";

// Complete Task 2 Below



let dogName = "Lola";
let dogType = "poodle";

// Complete Task 3 Below

console.log(`i will walk ${dogName1} today at 12 pm`)

if(dogType2 === 'corgi'){
  console.log(`i will walk ${dogName2} today at 12pm`)
}else {
  console.log(`i will walk ${dogName2} today at 1pm`)
}

if (dogType2 === 'corgi' || 'beagle'){
  console.log(`i will walk ${dogName2} today at 12pm`);



}else if (dogType2 === 'bulldog') {
  console.log(`i will walk ${dogName2} today at 1pm`)
} else {
  console.log(`i will walk ${dogName2} today at 2pm`)
}
