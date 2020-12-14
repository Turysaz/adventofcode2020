
cd py
echo "test python solutions"
for file in *.py; do
    name=${file%.*}
    diff "../results/$name.txt" <(python $file) > /dev/null
    if [ $? != 0 ]; then
        echo "FAIL: $name"
    else
        echo "okay: $name"
    fi
done
