import functools
import torch
import torch.nn as nn
import torch.nn.functional as F
import models.archs.arch_util as arch_util


class ProxIQANet(nn.Module):
    ''' modified SRResNet'''

    def __init__(self):
        super(ProxIQANet, self).__init__()

        self.conv1 = nn.Sequential([
            nn.Conv2d(6, 16, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2)
        ])

        self.conv2 = nn.Sequential([
            nn.Conv2d(16, 32, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2)
        ])

        self.conv3 = nn.Sequential([
            nn.Conv2d(32, 64, 5, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2)
        ])

        self.fc = nn.Linear(16384, 1)

        # initialization
        arch_util.initialize_weights([self.conv1, self.conv2, self.conv3, self.fc], 0.1)

    def forward(self, x, y):

        concat = torch.stack([x, y], 1)

        out = self.conv1(out)
        out = self.conv2(out)
        out = self.conv3(out)
        out = self.fc(out)

        return out
