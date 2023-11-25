# execute pkill on process killmenow
exec { 'kill killmenow':
  command  => 'pkill -9 killmenow',
  provider => 'shell',
}
