# kill a service
exec { 'kill':
  command  => 'pkill killmenow'
}
