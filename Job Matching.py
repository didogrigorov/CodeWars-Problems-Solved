def job_matching(candidate, job):
    if candidate == "" or job == "" or candidate['min_salary'] == 0 or job['max_salary'] == 0:
        return "An exception occurred"
    else:
        return candidate['min_salary'] - candidate['min_salary'] * 10//100 <= job['max_salary']