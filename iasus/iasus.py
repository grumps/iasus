# -*- coding: utf-8 -*-
import json

import falcon


class ImageMetaResource(object):

    def on_post(self, req, resp, uid):
        resp.status = falcon.HTTP_201
        data = json.load(req.bounded_stream)
        resp.status = falcon.HTTP_201


api = application = falcon.API()
api.add_route('/api/v1/file/{uid}/meta/', ImageMetaResource())
