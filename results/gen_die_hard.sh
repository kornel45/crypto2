#/bin/bash

script_name="gen_die_hard.sh"

for f in *; do
  if [ "$f" != "${script_name}" ]; then
    a="_result"
    echo "dieharder -a -f $f > $f$a"
    dieharder -a -f $f > $f$"_result"
  fi

  
done

