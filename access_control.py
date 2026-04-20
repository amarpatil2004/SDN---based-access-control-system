from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4

log = core.getLogger()

ALLOWED = ["10.0.0.1", "10.0.0.2"]

def _handle_PacketIn(event):
    packet = event.parsed

    # Allow ARP always
    if packet.type == ethernet.ARP_TYPE:
        msg = of.ofp_packet_out()
        msg.data = event.ofp
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)
        return

    ip = packet.find('ipv4')
    if not ip:
        return

    src = str(ip.srcip)
    dst = str(ip.dstip)

    # ✅ ALLOW
    if src in ALLOWED and dst in ALLOWED:
        log.info(f"ALLOW: {src} -> {dst}")

        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_src = src
        msg.match.nw_dst = dst
        msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
        event.connection.send(msg)

    # ❌ BLOCK
    else:
        log.info(f"BLOCK: {src} -> {dst}")

        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_src = src
        # no action → DROP
        event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
