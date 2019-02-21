try:
    import uwsgi
except ImportError:
    print('Failed to load python module uwsgi')
    # print('Periodic faiss index updates isn\'t enabled')


def hello_file(num):
    print "file has been modified !!!"


uwsgi.register_signal(17, "worker", hello_file)
uwsgi.add_file_monitor(17, "/media/chenhao/study/code/mycode/test-faiss/modify.file")
