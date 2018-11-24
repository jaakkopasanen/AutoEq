# SteelSeries Arctis 7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -0.3; 23 -0.5; 25 -0.6; 28 -0.7; 31 -0.7; 34 -0.5; 37 -0.3; 41 -0.2; 45 -0.5; 49 -1.1; 54 -1.8; 60 -2.7; 66 -3.5; 72 -4.0; 79 -4.5; 87 -5.0; 96 -5.3; 106 -5.7; 116 -5.8; 128 -6.0; 141 -6.1; 155 -6.1; 170 -6.0; 187 -5.7; 206 -5.5; 227 -5.4; 249 -5.2; 274 -4.7; 302 -4.3; 332 -4.1; 365 -3.8; 402 -3.6; 442 -3.0; 486 -2.4; 535 -1.8; 588 -1.3; 647 -1.0; 712 -0.3; 783 -0.0; 861 -0.4; 947 -0.3; 1042 0.3; 1146 0.5; 1261 0.1; 1387 -1.2; 1526 -2.3; 1678 -3.7; 1846 -4.5; 2031 -4.3; 2234 -3.6; 2457 -2.9; 2703 -2.0; 2973 -1.5; 3270 -0.7; 3597 -0.7; 3957 0.0; 4353 1.2; 4788 4.1; 5267 1.0; 5793 0.3; 6373 2.0; 7010 2.2; 7711 0.2; 8482 -2.6; 9330 -3.3; 10263 -0.9; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SteelSeries Arctis 7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SteelSeries Arctis 7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 123 Hz  | 0.73 | -5.7 dB |
| Peaking | 293 Hz  | 1.1  | -2.9 dB |
| Peaking | 2048 Hz | 2.03 | -4.9 dB |
| Peaking | 6381 Hz | 0.97 | 2.5 dB  |
| Peaking | 8983 Hz | 3.63 | -5.2 dB |
| Peaking | 43 Hz   | 3.37 | 1.1 dB  |
| Peaking | 1122 Hz | 3.81 | 1.6 dB  |
| Peaking | 3740 Hz | 2.18 | -1.0 dB |
| Peaking | 4845 Hz | 6.67 | 3.7 dB  |
| Peaking | 5533 Hz | 8.54 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/SteelSeries%20Arctis%207/SteelSeries%20Arctis%207.png)