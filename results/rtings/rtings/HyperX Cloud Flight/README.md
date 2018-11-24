# HyperX Cloud Flight

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.7; 28 0.2; 31 -0.0; 34 -0.2; 37 -0.4; 41 -0.6; 45 -0.9; 49 -1.1; 54 -1.3; 60 -1.5; 66 -1.8; 72 -2.0; 79 -2.2; 87 -2.4; 96 -2.6; 106 -2.8; 116 -2.8; 128 -2.8; 141 -2.5; 155 -2.2; 170 -1.8; 187 -1.2; 206 -0.4; 227 0.5; 249 1.3; 274 2.1; 302 3.0; 332 3.7; 365 4.3; 402 4.9; 442 4.4; 486 3.4; 535 2.3; 588 1.4; 647 1.2; 712 0.6; 783 -1.0; 861 -0.8; 947 -0.5; 1042 0.4; 1146 1.2; 1261 2.2; 1387 1.6; 1526 0.8; 1678 0.4; 1846 -0.2; 2031 -0.8; 2234 0.4; 2457 1.7; 2703 2.2; 2973 1.4; 3270 1.5; 3597 0.6; 3957 0.3; 4353 -0.8; 4788 -1.0; 5267 1.4; 5793 3.8; 6373 1.9; 7010 -1.0; 7711 -2.5; 8482 -4.8; 9330 -7.6; 10263 -6.6; 11289 -2.0; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Flight GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Flight ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 0.82 | -3.2 dB |
| Peaking | 379 Hz   | 1.49 | 5.3 dB  |
| Peaking | 5921 Hz  | 5.26 | 5.0 dB  |
| Peaking | 9686 Hz  | 2.42 | -9.2 dB |
| Peaking | 11903 Hz | 2.23 | 2.7 dB  |
| Peaking | 19 Hz    | 2.04 | 1.9 dB  |
| Peaking | 833 Hz   | 4.26 | -1.9 dB |
| Peaking | 1281 Hz  | 5.21 | 2.2 dB  |
| Peaking | 2793 Hz  | 3.55 | 2.2 dB  |
| Peaking | 4625 Hz  | 8.6  | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/HyperX%20Cloud%20Flight/HyperX%20Cloud%20Flight.png)