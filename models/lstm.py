import torch
import torch.nn as nn
from torch.nn import Parameter
from torch.nn import init
from torch import Tensor
import math

class NaiveLSTM(nn.Module):
    """Naive LSTM like nn.LSTM"""
    def __init__(self, input_size, hidden_size):
        super(NaiveLSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size

        # input gate
        self.w_ii = Parameter(Tensor(hidden_size, input_size))
        self.w_hi = Parameter(Tensor(hidden_size, hidden_size))
        self.b_ii = Parameter(Tensor(hidden_size, 1))
        self.b_hi = Parameter(Tensor(hidden_size, 1))

        # forget gate
        self.w_if = Parameter(Tensor(hidden_size, input_size))
        self.w_hf = Parameter(Tensor(hidden_size, hidden_size))
        self.b_if = Parameter(Tensor(hidden_size, 1))
        self.b_hf = Parameter(Tensor(hidden_size, 1))

        # output gate
        self.w_io = Parameter(Tensor(hidden_size, input_size))
        self.w_ho = Parameter(Tensor(hidden_size, hidden_size))
        self.b_io = Parameter(Tensor(hidden_size, 1))
        self.b_ho = Parameter(Tensor(hidden_size, 1))
        
        # cell
        self.w_ig = Parameter(Tensor(hidden_size, input_size))
        self.w_hg = Parameter(Tensor(hidden_size, hidden_size))
        self.b_ig = Parameter(Tensor(hidden_size, 1))
        self.b_hg = Parameter(Tensor(hidden_size, 1))

        self.reset_weigths()

    def reset_weigths(self):
        """reset weights
        """
        stdv = 1.0 / math.sqrt(self.hidden_size)
        for weight in self.parameters():
            init.uniform_(weight, -stdv, stdv)

    def forward(self, inputs, state):   # inputs[1, 1, 10], state[0] = h[1, 1, 20], state[1] = c[1, 1, 20]
        """
        Args:
            inputs: [1, 1, input_size]          中间那个参数应该就是样本个数, input_size就是特征/属性个数
            state: ([1, 1, hidden_size], [1, 1, hidden_size])
        """
#         seq_size, batch_size, _ = inputs.size()

        if state is None:
            h_t = torch.zeros(1, self.hidden_size).t()
            c_t = torch.zeros(1, self.hidden_size).t()
        else:
            (h, c) = state
            h_t = h.squeeze(0).t()      # [20, 1]
            c_t = c.squeeze(0).t()      # [20, 1]

        hidden_seq = []         # 保存每个输出状态h

        seq_size = 1
        for t in range(seq_size):
            x = inputs[:, t, :].t()         # [10, 1]

            # 下面的(1-4)对应lstm图中从左到右四条分支(lstm图的下半部分)
            # input gate(2)     # [20, 10] @ [10, 1] + [20, 1] + [20, 20] @ [20, 1] + [20, 1] = [20, 1]
            i = torch.sigmoid(self.w_ii @ x + self.b_ii + self.w_hi @ h_t + self.b_hi)

            # forget gate(1)    # [20, 1]
            f = torch.sigmoid(self.w_if @ x + self.b_if + self.w_hf @ h_t + self.b_hf)

            # cell(3)           # [20, 1]
            g = torch.tanh(self.w_ig @ x + self.b_ig + self.w_hg @ h_t + self.b_hg)

            # output gate(4)    # [20, 1]
            o = torch.sigmoid(self.w_io @ x + self.b_io + self.w_ho @ h_t + self.b_ho)
            
            c_next = f * c_t + i * g    # [20, 1]  i * g 就是输入门。整个c_next就是lstm图左半边，到上面那条C操作的加号那里
            h_next = o * torch.tanh(c_next)     # [20, 1]  这就是图中的h_t输出那里
            c_next_t = c_next.t().unsqueeze(0)  # [1, 1, 20]
            h_next_t = h_next.t().unsqueeze(0)  # [1, 1, 20]
            hidden_seq.append(h_next_t)

        hidden_seq = torch.cat(hidden_seq, dim=0)
        return hidden_seq, (h_next_t, c_next_t)

def reset_weigths(model):
    """reset weights
    """
    for weight in model.parameters():
        init.constant_(weight, 0.5)

### test 
inputs = torch.ones(1, 1, 10)
h0 = torch.ones(1, 1, 20)
c0 = torch.ones(1, 1, 20)
print(h0.shape, h0)
print(c0.shape, c0)
print(inputs.shape, inputs)

# test naive_lstm with input_size=10, hidden_size=20
naive_lstm = NaiveLSTM(10, 20)      # 第一个参数是input_size, 第二个参数是hidden_size
reset_weigths(naive_lstm)

output1, (hn1, cn1) = naive_lstm(inputs, (h0, c0))  # inputs[1, 1, 10], h0[1, 1, 20], c0[1, 1, 20]; 
                                                    # 返回的是所有的输出h以及最后一次的h跟c. output1[1, 1, 20], hn1[1, 1, 20], cn1[1, 1, 20]

print(hn1.shape, cn1.shape, output1.shape)
print(hn1)
print(cn1)
print(output1)




# 以下是官方实现
# Use official lstm with input_size=10, hidden_size=20
lstm = nn.LSTM(10, 20)
reset_weigths(lstm)
output2, (hn2, cn2) = lstm(inputs, (h0, c0))
print(hn2.shape, cn2.shape, output2.shape)
print(hn2)
print(cn2)
print(output2)
