(function () {
	  function install(Vue) {
	    Vue.env = document.querySelector('meta[name="env"]').getAttribute('content');
	    Vue.title = document.title;
	    var webUrl = void 0;
	    var apiUrl = void 0;
	    var imgUrl = void 0;
	    if (false) {
	      webUrl = '//v2.ishuhui.me';
	      apiUrl = '//hhzapi.ishuhui.me';
	      imgUrl = ['//pic01.ishuhui.com', '//pic02.ishuhui.com', '//pic03.ishuhui.com'];
	    } else {
	      webUrl = '//v2.ishuhui.com';
	      apiUrl = '//hhzapi.ishuhui.com';
	      imgUrl = ['//pic01.ishuhui.com', '//pic02.ishuhui.com', '//pic03.ishuhui.com'];
	    }
	    Vue.webUrl = webUrl;
	    Vue.imgUrl = imgUrl;

	    var ver = JSON.parse(document.querySelector('meta[name="ver"]').getAttribute('content'));
	    Vue.updateWebVer = function (newVer) {
	      ver = newVer;
	    };

	    Vue.getImgUrl = function (url) {
	      var number = arguments.length <= 1 || arguments[1] === undefined ? imgUrl.length - 1 : arguments[1];
	      var imgVer = arguments.length <= 2 || arguments[2] === undefined ? '' : arguments[2];

	      if (/^(http(s)?:)?\/\//.test(url)) {
	        return url;
	      }
	      number = number % imgUrl.length;
	      url = url.replace(/^\/upload/, imgUrl[number]);
	      return imgVer ? url + '?' + imgVer : url;
	    };

	    Vue.serialize = function (query) {
	      var type = arguments.length <= 1 || arguments[1] === undefined ? '/' : arguments[1];

	      var urlText = '';
	      if ((typeof query === 'undefined' ? 'undefined' : (0, _typeof3.default)(query)) === 'object') {
	        if (query.id) {
	          query.id = parseInt(query.id, 10);
	        }
	        (0, _keys2.default)(query).forEach(function (key) {
	          if (typeof query[key] !== 'undefined' && query[key] !== 'undefined') {
	            if (type === '?') {
	              urlText += '&' + key + '=' + query[key];
	            } else {
	              urlText += '/' + key + '/' + query[key];
	            }
	          }
	        });
	      }
	      return urlText.replace(/^&/, '?');
	    };

	    Vue.processUrl = function (url) {
	      var opt = arguments.length <= 1 || arguments[1] === undefined ? {} : arguments[1];

	      if (url.startsWith('/user')) {
	        url = webUrl + url;
	        return url + Vue.serialize(opt);
	      }
	      opt.ver = ver.web;

	      if (url.startsWith('/article')) {
	        opt.ver = ver.a_conf;
	        if (url.startsWith('/article/post') || url.startsWith('/article/list')) {
	          opt.ver = ver.a_post;
	        }
	      }

	      if (url.startsWith('/cartoon') || url.startsWith('/book')) {
	        opt.ver = ver.c_conf;
	        if (url.startsWith('/cartoon/post') || url.startsWith('/cartoon/book_list')) {
	          opt.ver = ver.c_post;
	        }
	      }

	      if (url.startsWith('/setting')) {
	        opt.ver = ver.set;
	      }
	      url = apiUrl + url;
	      return '' + url + Vue.serialize(opt) + '.json';
	    };

	    function httpError(self, res) {
	      var errMsg = '出错了 错误代码: ' + res.status + ' 错误信息: ' + res.statusText;
	      actions.toast(self.$store, { type: 'error', content: errMsg });
	    }

	    Vue.dataDefault = {
	      errNo: 1,
	      errMsg: '',
	      data: {}
	    };

	    Vue.httpGet = function (url) {
	      var opt = arguments.length <= 1 || arguments[1] === undefined ? {} : arguments[1];
	      var df = arguments.length <= 2 || arguments[2] === undefined ? Vue.dataDefault : arguments[2];
	      var callback = arguments[3];

	      var self = this;
	      url = Vue.processUrl(url, opt);

	      var req = { url: url };
	      if (url.startsWith(webUrl)) {
	        req.credentials = true;
	      }
	      return Vue.http(req).then(function (res) {
	        if (typeof res.data === 'string') {
	          try {
	            res.data = JSON.parse(res.data);
	          } catch (e) {
	            pushErrLog('json', e);
	          }
	        }
	        if (res.data.errNo !== 0 && res.data.errMsg) {
	          actions.toast(self.$store, { type: 'error', content: res.data.errMsg });
	        }
	        if (callback) {
	          callback(res.data);
	        }
	        return res.data;
	      }, function (res) {
	        if (typeof res.data === 'string') {
	          try {
	            res.data = JSON.parse(res.data);
	          } catch (e) {
	            pushErrLog('json', e);
	          }
	        }
	        if (res.data && res.data.errNo === 0) {
	          return res.data;
	        }
	        httpError(self, res);
	        df.errMsg = '数据请求出错 ' + res.status + ' - ' + res.statusText;
	        return df;
	      });
	    };
	    Vue.httpPost = function (url) {
	      var opt = arguments.length <= 1 || arguments[1] === undefined ? {} : arguments[1];
	      var toastData = arguments.length <= 2 || arguments[2] === undefined ? '更新成功' : arguments[2];
	      var callback = arguments[3];

	      var self = this;
	      return Vue.http.post(Vue.processUrl(url), opt, { credentials: true }).then(function (res) {
	        if (typeof res.data === 'string') {
	          try {
	            res.data = JSON.parse(res.data);
	          } catch (e) {
	            pushErrLog('json', e);
	          }
	        }
	        if (toastData !== false) {
	          if (res.data.errNo !== 0) {
	            actions.toast(self.$store, { type: 'error', content: res.data.errMsg });

	            if (res.data.errNo === 101) {
	              actions.setEntry(self.$store, { type: 'login' });
	              actions.logout(self.$store);
	            }
	          } else {
	            if (res.data.data.msg && toastData === '更新成功') {
	              toastData = res.data.data.msg;
	            }
	            actions.toast(self.$store, { type: 'success', content: toastData });
	          }
	        }
	        if (callback) {
	          callback(res.data);
	        }
	        return res.data;
	      }, function (res) {
	        if (typeof res.data === 'string') {
	          try {
	            res.data = JSON.parse(res.data);
	          } catch (e) {
	            pushErrLog('json', e);
	          }
	        }
	        if (res.data && res.data.errNo === 0) {
	          return res.data;
	        }
	        httpError(self, res);
	        var df = Vue.dataDefault;
	        df.errMsg = '数据请求出错 ' + res.status + '  -  ' + res.statusText;
	        return df;
	      });
	    };
	    Vue.httpGet('/setting/get_conf', { option: 'ad-hhz', group: 'all' }).then(function (res) {
	      Vue.ad = res;
	    });
	  }

	  if (( false ? 'undefined' : (0, _typeof3.default)(exports)) === 'object') {
	    module.exports = install;
	  } else if (true) {
	    !(__WEBPACK_AMD_DEFINE_ARRAY__ = [], __WEBPACK_AMD_DEFINE_RESULT__ = function () {
	      return install;
	    }.apply(exports, __WEBPACK_AMD_DEFINE_ARRAY__), __WEBPACK_AMD_DEFINE_RESULT__ !== undefined && (module.exports = __WEBPACK_AMD_DEFINE_RESULT__));
	  } else if (window.Vue) {
	    window.Vue.use(install);
	  }
})();