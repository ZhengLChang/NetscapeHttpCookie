import re
import logging
import time
import traceback

def http_cookie_2_netscape_cookie(cookie_str, dump_to_file_path="./youtubeCookie.file"):
    try:
        cookie_str = cookie_str if isinstance(cookie_str, str) else str(cookie_str, 'utf-8')
        cookie_arr = cookie_str.split(";")
        cookie_arr = [cookie.strip() for cookie in cookie_arr]
        if not dump_to_file_path:
            logging.warning(f"[http_cookie_2_netscape_cookie] dump_to_file_path empty, please check....")
        key_value_Reg = re.compile(r"(.*?)=(.*)")
        dump_str = "# Netscape HTTP Cookie File\n"
        dump_str += f"# update time: {int(time.time())}\n"
        for cookie in cookie_arr:
            key_value_arr = key_value_Reg.findall(cookie)
            if not key_value_arr or not len(key_value_arr) > 0:
                continue
            key = key_value_arr[0][0]
            value = key_value_arr[0][1]
            dump_str += f".youtube.com\tTRUE\t/\tTRUE\t0\t{key}\t{value}\n"

        with open(dump_to_file_path, "w") as f:
            f.write(dump_str)
    except Exception as err:
        logging.error(f"[http_cookie_2_netscape_cookie] {traceback.format_exc()}")




if __name__ == "__main__":
    http_cookie_2_netscape_cookie("VISITOR_INFO1_LIVE=6G5kqNpso-0; CONSENT=YES+US.zh-CN+20161213-01-0; PREF=al=zh-CN; YSC=uGnNdE7-jII")
