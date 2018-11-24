# AKG Q701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.4; 34 4.0; 37 3.6; 41 3.3; 45 3.0; 49 2.7; 54 2.4; 60 2.1; 66 1.7; 72 1.4; 79 0.9; 87 0.4; 96 -0.0; 106 -0.5; 116 -0.9; 128 -1.4; 141 -1.7; 155 -2.0; 170 -2.1; 187 -2.3; 206 -2.3; 227 -2.2; 249 -2.3; 274 -2.3; 302 -2.3; 332 -2.3; 365 -2.4; 402 -2.4; 442 -2.3; 486 -1.9; 535 -1.3; 588 -0.7; 647 -0.8; 712 -0.5; 783 -0.1; 861 0.0; 947 -0.1; 1042 0.0; 1146 -0.1; 1261 -0.5; 1387 -0.9; 1526 -1.8; 1678 -3.3; 1846 -4.8; 2031 -5.9; 2234 -6.4; 2457 -5.3; 2703 -4.4; 2973 -3.1; 3270 -1.7; 3597 -2.3; 3957 -2.8; 4353 -3.1; 4788 -2.8; 5267 -3.3; 5793 -4.8; 6373 -7.8; 7010 -7.2; 7711 -6.0; 8482 -5.7; 9330 -2.5; 10263 0.0; 11289 -1.5; 12418 -2.5; 13660 -0.0; 15026 0.0; 16529 -2.3; 18182 -7.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG Q701 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.03 | 6.0 dB  |
| Peaking | 2196 Hz  | 1.94 | -6.3 dB |
| Peaking | 6472 Hz  | 2.26 | -1.8 dB |
| Peaking | 6992 Hz  | 1.89 | -5.9 dB |
| Peaking | 18971 Hz | 1.92 | -9.2 dB |
| Peaking | 64 Hz    | 0.76 | 3.4 dB  |
| Peaking | 224 Hz   | 0.16 | -3.2 dB |
| Peaking | 943 Hz   | 0.81 | 2.9 dB  |
| Peaking | 15441 Hz | 2.9  | 2.1 dB  |
| Peaking | 17444 Hz | 4.54 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20Q701/AKG%20Q701.png)