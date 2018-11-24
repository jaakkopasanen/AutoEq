# HyperX Cloud Flight

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.9; 28 0.4; 31 0.0; 34 -0.2; 37 -0.5; 41 -0.8; 45 -1.1; 49 -1.4; 54 -1.7; 60 -1.8; 66 -1.9; 72 -2.0; 79 -2.0; 87 -2.0; 96 -2.2; 106 -2.3; 116 -2.3; 128 -2.2; 141 -1.9; 155 -1.6; 170 -1.1; 187 -0.6; 206 0.1; 227 1.0; 249 1.9; 274 2.8; 302 3.8; 332 4.6; 365 5.4; 402 6.0; 442 5.5; 486 4.6; 535 3.5; 588 2.5; 647 2.3; 712 1.5; 783 -0.5; 861 -0.6; 947 -0.4; 1042 0.5; 1146 1.4; 1261 2.4; 1387 1.6; 1526 0.4; 1678 0.0; 1846 -0.2; 2031 -0.3; 2234 0.8; 2457 2.2; 2703 2.8; 2973 2.4; 3270 3.4; 3597 2.7; 3957 1.5; 4353 -0.8; 4788 -1.2; 5267 1.8; 5793 5.2; 6373 4.5; 7010 1.5; 7711 -1.4; 8482 -4.4; 9330 -6.1; 10263 -3.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Flight GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Flight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.7  | -2.7 dB |
| Peaking | 387 Hz  | 1.39 | 6.4 dB  |
| Peaking | 3064 Hz | 2.75 | 3.3 dB  |
| Peaking | 6107 Hz | 5.17 | 6.3 dB  |
| Peaking | 9147 Hz | 3.86 | -6.9 dB |
| Peaking | 20 Hz   | 2.22 | 2.1 dB  |
| Peaking | 889 Hz  | 2.35 | -3.8 dB |
| Peaking | 1395 Hz | 0.88 | 4.4 dB  |
| Peaking | 1761 Hz | 1.79 | -4.3 dB |
| Peaking | 4568 Hz | 7.86 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/HyperX%20Cloud%20Flight/HyperX%20Cloud%20Flight.png)