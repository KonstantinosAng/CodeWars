// see https://www.codewars.com/kata/52685f7382004e774f0001f7/solutions/javascript

function humanReadable(seconds) {
  var hours = Math.floor(seconds/3600);
  var minutes = Math.floor((seconds - hours*3600)/60);
  var secs = Math.floor(seconds - minutes*60 - hours*3600);
  var _hours = "";
  var _minutes = "";
  var _secs = "";
  if (hours.toString().length < 2) {_hours = "0"}
  if (minutes.toString().length < 2) {_minutes = "0"}
  if (secs.toString().length < 2) {_secs = "0"}
  return `${_hours}${hours}:${_minutes}${minutes}:${_secs}${secs}` 
}