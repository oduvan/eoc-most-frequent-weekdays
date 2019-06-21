requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, ra) {
        var io = new extIO({
            functions: {
                js: 'mostFrequentDays',
                python: 'most_frequent_days'
            },
            multipleArguments: true,
        });
        io.start();
    }
);
