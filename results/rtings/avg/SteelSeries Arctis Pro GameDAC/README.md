# SteelSeries Arctis Pro GameDAC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.1; 25 -4.0; 28 -3.8; 31 -3.4; 34 -2.8; 37 -2.1; 41 -1.2; 45 -0.6; 49 -0.2; 54 -0.2; 60 -0.3; 66 -0.5; 72 -0.6; 79 -0.8; 87 -1.0; 96 -1.2; 106 -1.3; 116 -1.4; 128 -1.4; 141 -1.6; 155 -1.7; 170 -1.7; 187 -1.6; 206 -1.6; 227 -1.7; 249 -2.0; 274 -2.3; 302 -2.6; 332 -2.8; 365 -3.0; 402 -3.1; 442 -3.2; 486 -3.2; 535 -3.2; 588 -3.0; 647 -2.8; 712 -1.9; 783 -0.9; 861 -1.0; 947 -0.4; 1042 0.1; 1146 0.4; 1261 0.8; 1387 1.4; 1526 1.9; 1678 0.1; 1846 -0.8; 2031 -1.0; 2234 -0.5; 2457 0.2; 2703 -0.0; 2973 0.6; 3270 3.4; 3597 6.0; 3957 5.5; 4353 0.4; 4788 -2.6; 5267 -3.2; 5793 -3.7; 6373 -4.2; 7010 -3.3; 7711 -2.0; 8482 -0.2; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -2.6; 13660 -4.6; 15026 -3.4; 16529 -2.3; 18182 -1.0; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis Pro GameDAC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis Pro GameDAC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.22 | -4.4 dB |
| Peaking | 374 Hz   | 0.75 | -3.2 dB |
| Peaking | 3716 Hz  | 4.06 | 8.1 dB  |
| Peaking | 5679 Hz  | 1.92 | -4.8 dB |
| Peaking | 14285 Hz | 2.46 | -4.6 dB |
| Peaking | 120 Hz   | 2.3  | -0.8 dB |
| Peaking | 606 Hz   | 3.95 | -1.1 dB |
| Peaking | 1542 Hz  | 1.95 | 4.0 dB  |
| Peaking | 1832 Hz  | 2.2  | -3.4 dB |
| Peaking | 10117 Hz | 3.31 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SteelSeries%20Arctis%20Pro%20GameDAC/SteelSeries%20Arctis%20Pro%20GameDAC.png)