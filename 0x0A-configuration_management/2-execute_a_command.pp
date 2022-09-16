# kill a service
exec { 'kill':
  command  => '/bin/pkill killmenow'
}
