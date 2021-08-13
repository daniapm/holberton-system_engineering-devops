# manifest that kills a process named killmenow.
exec { 'test':
  command => 'pkill',
}
