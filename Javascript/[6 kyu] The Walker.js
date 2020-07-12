// see https://www.codewars.com/kata/5b40b666dfb4291ad9000049/solutions/javascript

function solve(a, b, c, alpha, beta, gamma) {
  const ax_coord = Math.cos(alpha*Math.PI/180)*a;
  const ay_coord = Math.sin(alpha*Math.PI/180)*a;
  const by_coord = ay_coord + Math.cos(beta*Math.PI/180)*b;
  const bx_coord = ax_coord - Math.sin(beta*Math.PI/180)*b;
  const cx_coord = bx_coord - Math.cos(gamma*Math.PI/180)*c;
  const cy_coord = by_coord - Math.sin(gamma*Math.PI/180)*c;
  const x = Math.abs(cx_coord);
  const y = Math.abs(cy_coord);
  const distance_co = Math.round(Math.sqrt(x*x + y*y));
  const angle_tco = 180 - 180/Math.PI*Math.atan(y/x);
  const m_angle_tco = (angle_tco - Math.floor(angle_tco))*60;
  const s_angle_tco = (m_angle_tco - Math.floor(m_angle_tco))*60;
  return [distance_co, Math.floor(angle_tco), Math.floor(m_angle_tco), Math.floor(s_angle_tco)]
}