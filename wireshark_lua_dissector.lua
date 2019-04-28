-- BYTES 不限长度，不作转换。
local pf_trasaction_id      = ProtoField.new   ("Transaction ID会话ID", "mydns.trans_id", ftypes.BYTES)
-- uint()将这部分值，转成数值； 后续可用作判断
local mytype = tvbuf:range(1,1):uint()
-- 变为userdata格式
local mytype = tvbuf:range(1,1)   
--  得到 ts 后，可在数值后面，添加注释
    ts = tree:add(pf_trasaction_id, tvbuf:range(0,12))
	ts:append_text(" 这里是注释")
-- 同一个数值内容，可以多次添加treeItem,没有限制。
	tree:add(pf_trasaction_id, tvbuf:range(0,12))
	tree:add(pf_trasaction_id, tvbuf:range(0,12))
-- 以小头的方式转换数值
	ts = tree:add_le(pf_trasaction_id, tvbuf:range(0,2))
	