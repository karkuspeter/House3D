# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import tqdm
import cv2

from House3D import objrender, Environment, load_config


if __name__ == '__main__':
    api = objrender.RenderAPI(w=600, h=450, device=0)
    cfg = load_config('config.json')
    cfg['prefix'] = cfg['prefix'] + './house_single_A/'
    print cfg['prefix']

    env = Environment(api, '06f7826572be27f205e701783960416e', cfg) #'0a96348d9c8acf673d3da07b6316e671' '07d1d46444ca33d50fbcb5dc12d7c103', cfg)  #'06f7826572be27f205e701783960416e'  00065ecbdd7300d35ef4328ffe871505
    # single_A: 06f7826572be27f205e701783960416e

    # fourcc = cv2.VideoWriter_fourcc(*'X264')
    # writer = cv2.VideoWriter('out.avi', fourcc, 30, (1200, 900))
    for t in tqdm.trange(1000):
        if t % 1000 == 0:
            env.reset()
        mat = env.debug_render()

        print (env.info['grid'], env.info['yaw'])

        # writer.write(mat)
        cv2.imshow("aaa", mat)
        key = cv2.waitKey(0)
        if not env.keyboard_control(key):
            break
    # writer.release()
