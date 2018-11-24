# JBL E50BT

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.0; 23 -0.7; 25 -1.2; 28 -1.9; 31 -2.4; 34 -2.7; 37 -2.8; 41 -2.8; 45 -2.7; 49 -2.7; 54 -2.8; 60 -2.8; 66 -2.8; 72 -2.7; 79 -2.7; 87 -2.7; 96 -2.7; 106 -2.7; 116 -2.8; 128 -2.8; 141 -2.6; 155 -2.4; 170 -2.0; 187 -1.4; 206 -0.5; 227 0.7; 249 2.2; 274 4.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 5.2; 535 4.4; 588 3.5; 647 2.6; 712 1.8; 783 1.0; 861 0.3; 947 0.0; 1042 0.0; 1146 -0.3; 1261 -1.0; 1387 -1.8; 1526 -2.4; 1678 -3.7; 1846 -3.9; 2031 -3.6; 2234 -2.7; 2457 -1.2; 2703 -0.8; 2973 -0.5; 3270 0.4; 3597 2.4; 3957 3.0; 4353 0.9; 4788 0.9; 5267 2.9; 5793 5.7; 6373 5.4; 7010 2.5; 7711 0.2; 8482 -3.4; 9330 -6.8; 10263 -6.5; 11289 -2.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`JBL E50BT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL E50BT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 146 Hz   |  0.27 | -4.3 dB |
| Peaking | 369 Hz   |  0.98 | 10.0 dB |
| Peaking | 1815 Hz  |  2.11 | -4.5 dB |
| Peaking | 6126 Hz  |  2.22 | 6.4 dB  |
| Peaking | 9563 Hz  |  3.11 | -8.7 dB |
| Peaking | 35 Hz    |  2.9  | -0.7 dB |
| Peaking | 293 Hz   | 10.73 | 1.4 dB  |
| Peaking | 3853 Hz  |  5.68 | 3.2 dB  |
| Peaking | 4624 Hz  |  5.65 | -2.1 dB |
| Peaking | 12401 Hz |  6.38 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/JBL%20E50BT/JBL%20E50BT.png)