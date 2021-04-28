/*
export const CountEvent = async function (events) {
  let header = new Set(["all"]);
  let result = new Object();
  console.log("hi");
  console.log(events);
  await events.forEach((e) => {
    header.add(e.agent);
    if (e.agent in Object.keys(result)) {
    } else {
      result[e.agent] = new Object();
      result[e.agent][e.time] = 1;
    }
  });
  console.log(header);
};
*/
