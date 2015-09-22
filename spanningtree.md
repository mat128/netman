Cheatsheet
==========

Setting a port in edge mode
---------------------------

**Brocade**
no spanning-tree

**Dell**
spanning-tree disable
spanning-tree portfast (is that even required?)

**Cisco**
spanning-tree bpdufilter enable
spanning-tree bpduguard enable
spanning-tree portfast trunk

**Juniper**
set protocols rstp interface NAME edge
set protocols rstp interface NAME no-root-port


Brocade (5.8.0T185/5.8.0bT183)
=======
    
    spanning-tree           Enable or Disable STP
        protect                 Drop BPDUs received on this interface
            do-disable              Disable the interface if  BPDUs received on this interface
              <cr>
            re-enable               Re-enable the interface that is disabled due to BPDU-GUARD violation
              <cr>
            <cr>
        root-protect            Drop superior BPDUs and trigger warning log message
            <cr>
        <cr>


Dell
====
    
    spanning-tree
        auto-portfast            Allow to move to the forwarding state when BPDU timeout occurs
          <cr>                     Press enter to execute the command.
        cost                     Change an interface's spanning tree path cost.
          <0-200000000>            Change an interface's spanning tree path cost in the range 0-200000000
        disable                  Disable spanning-tree on an interface.
          <cr>                     Press enter to execute the command.
        guard                    Configure a guard for the port.
          loop                     Configure a port for loop guard.
            <cr>                     Press enter to execute the command.
          none                     Disable root and loop guards on a port.
            <cr>                     Press enter to execute the command.
          root                     Configure a port for root guard.
            <cr>                     Press enter to execute the command.
        mst                      Configure a multiple spanning tree instance.
          <0>                      Enter a multiple spanning tree instance identifier.
            external-cost            Specify external pathcost for port used by a MST instance.
              <0-200000000>            Enter an integer in the range of 0 - 200000000.
                <cr>                     Press enter to execute the command.
          <1-15>                   Enter a multiple spanning tree instance identifier.
            cost                     Specify pathcost for port used by a MST instance.
              <0-200000000>            Enter an integer in the range of 0 - 200000000.
                <cr>                     Press enter to execute the command.
            port-priority            Specify priority for port used by a MST instance.
              <priority>               Enter an integer in the range of 0 - 240.
                <cr>                     Press enter to execute the command.
        port-priority            Change an interface's spanning tree priority (in steps of 16)
          <priority>               Change an interface's spanning tree priority (in steps of 16) in the range 0-240
            <cr>                     Press enter to execute the command.
        portfast                 Allow to move directly to the forwarding state when linkup occurs
          <cr>                     Press enter to execute the command.
        tcnguard                 Configure a port for tcn guard.
          <cr>                     Press enter to execute the command.
    


Cisco (WS-C3750G-24TS-1U  12.2(58)SE2           C3750-IPSERVICESK9-M)
=====================================================================
  
    spanning-tree
        bpdufilter     Don't send or receive BPDUs on this interface
          disable  Disable BPDU filtering for this interface
            <cr>
          enable   Enable BPDU filtering for this interface
            <cr>
        bpduguard      Don't accept BPDUs on this interface
          disable  Disable BPDU guard for this interface
            <cr>
          enable   Enable BPDU guard for this interface
            <cr>
        cost           Change an interface's spanning tree port path cost
          <1-200000000>  port path cost
        guard          Change an interface's spanning tree guard mode
          loop  Set guard mode to loop guard on interface
            <cr>
          none  Set guard mode to none
            <cr>
          root  Set guard mode to root guard on interface
            <cr>
        link-type      Specify a link type for spanning tree protocol use
          point-to-point  Consider the interface as point-to-point
            <cr>
          shared          Consider the interface as shared
            <cr>
        mst            Multiple spanning tree
          WORD          MST instance list, example 0,2-4,6,8-12
            cost           Change the interface spanning tree path cost for an instance
              <1-200000000>  Change the interface spanning tree path cost for an instance
                <cr>
            port-priority  Change the spanning tree port priority for an instance
              <0-240>  port priority in increments of 16
                <cr>
          pre-standard  Force pre-standard MST BPDU transmission on port
            <cr>
        port-priority  Change an interface's spanning tree port priority
          <0-240>  port priority in increments of 16
            <cr>
        portfast       Enable an interface to move directly to forwarding on link up
          disable  Disable portfast for this interface
            <cr>
          trunk    Enable portfast on the interface even in trunk mode
            <cr>
          <cr>
        stack-port     Enable stack port
          <cr>
        vlan           VLAN Switch Spanning Tree
          WORD  vlan range, example: 1,3-5,7,9-11
            cost           Change an interface's per VLAN spanning tree path cost
              <1-200000000>  Change an interface's per VLAN spanning tree path cost
                <cr>
            port-priority  Change an interface's spanning tree port priority
              <0-240>  port priority in increments of 16
                <cr>
                

Juniper
=======
    
    set protocols rstp interface xe-0/0/1
        <[Enter]>            Execute this command
        access-trunk         Send/Receive untagged RSTP BPDUs on this interface
          <[Enter]>            Execute this command
      + apply-groups         Groups from which to inherit configuration data
          <value>              Groups from which to inherit configuration data
          [                    Open a set of values
              <value>              Groups from which to inherit configuration data
              ]                    Close the current set
              <[Enter]>            Execute this command
      + apply-groups-except  Don't inherit configuration data from these groups
          <value>              Groups from which to inherit configuration data
          [                    Open a set of values
              <value>              Groups from which to inherit configuration data
              ]                    Close the current set
              <[Enter]>            Execute this command
      > bpdu-timeout-action  Define action on BPDU expiry (Loop Protect)
          <[Enter]>            Execute this command
          alarm                Generate an alarm
            <[Enter]>            Execute this command
        + apply-groups         Groups from which to inherit configuration data
            <value>              Groups from which to inherit configuration data
            [                    Open a set of values
                <value>              Groups from which to inherit configuration data
                ]                    Close the current set
                <[Enter]>            Execute this command
        + apply-groups-except  Don't inherit configuration data from these groups
            <value>              Groups from which to inherit configuration data
            [                    Open a set of values
                <value>              Groups from which to inherit configuration data
                ]                    Close the current set
                <[Enter]>            Execute this command
          block                Block the interface
            <[Enter]>            Execute this command
          |                    Pipe through a command
        cost                 Cost of the interface (1..200000000)
          <cost>               Cost of the interface (1..200000000)
            <[Enter]>            Execute this command
        edge                 Port is an edge port
          <[Enter]>            Execute this command
        mode                 Interface mode (P2P or shared)
          point-to-point       Interface mode is point-to-point
            <[Enter]>            Execute this command
          shared               Interface mode is shared
            <[Enter]>            Execute this command
        no-root-port         Do not allow the interface to become root (Root Protect)
          <[Enter]>            Execute this command
        priority             Interface priority (in increments of 16 - 0,16,..240) (0..255)
          <priority>           Interface priority (in increments of 16 - 0,16,..240) (0..255)
            <[Enter]>            Execute this command
        |                    Pipe through a command
        
        
        