# HiFiMan Ananda

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.2; 28 3.8; 31 3.5; 34 3.2; 37 3.0; 41 2.7; 45 2.4; 49 2.2; 54 1.9; 60 1.6; 66 1.3; 72 1.1; 79 0.9; 87 0.7; 96 0.5; 106 0.1; 116 -0.2; 128 -0.5; 141 -0.7; 155 -1.0; 170 -1.2; 187 -1.3; 206 -1.2; 227 -1.3; 249 -1.2; 274 -1.1; 302 -0.7; 332 -0.0; 365 -0.4; 402 -1.3; 442 -1.7; 486 -1.7; 535 -1.8; 588 -2.1; 647 -0.8; 712 0.6; 783 0.8; 861 0.1; 947 -0.6; 1042 0.6; 1146 2.4; 1261 2.1; 1387 1.6; 1526 2.6; 1678 3.2; 1846 2.2; 2031 1.2; 2234 0.9; 2457 -0.4; 2703 -0.7; 2973 -1.8; 3270 -1.1; 3597 -0.6; 3957 -0.1; 4353 -0.1; 4788 1.3; 5267 4.1; 5793 4.8; 6373 -1.0; 7010 -1.7; 7711 -1.9; 8482 -3.2; 9330 -1.2; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.2; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMan Ananda GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMan Ananda ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.33 | 5.1 dB  |
| Peaking | 1263 Hz  | 0.84 | 3.2 dB  |
| Peaking | 1492 Hz  | 0.11 | -2.3 dB |
| Peaking | 1719 Hz  | 2.41 | 2.6 dB  |
| Peaking | 5487 Hz  | 5.2  | 7.5 dB  |
| Peaking | 336 Hz   | 6.6  | 1.6 dB  |
| Peaking | 3948 Hz  | 5.53 | 1.0 dB  |
| Peaking | 8934 Hz  | 2.64 | -3.5 dB |
| Peaking | 9732 Hz  | 3.84 | 3.2 dB  |
| Peaking | 12428 Hz | 1.94 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/HiFiMan%20Ananda/HiFiMan%20Ananda.png)