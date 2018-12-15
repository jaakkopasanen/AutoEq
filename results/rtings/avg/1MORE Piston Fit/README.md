# 1MORE Piston Fit

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 5.3; 79 4.3; 87 3.2; 96 2.0; 106 0.8; 116 -0.4; 128 -1.5; 141 -2.5; 155 -3.3; 170 -3.9; 187 -4.4; 206 -4.8; 227 -5.1; 249 -5.3; 274 -5.4; 302 -5.3; 332 -5.2; 365 -5.0; 402 -4.7; 442 -4.3; 486 -3.9; 535 -3.3; 588 -2.5; 647 -1.7; 712 -1.0; 783 -0.4; 861 0.0; 947 0.2; 1042 -0.5; 1146 -1.2; 1261 -1.5; 1387 -1.7; 1526 -1.7; 1678 -2.2; 1846 -3.6; 2031 -4.6; 2234 -4.4; 2457 -2.7; 2703 -0.1; 2973 -3.5; 3270 -6.3; 3597 -7.0; 3957 -7.3; 4353 -8.0; 4788 -8.5; 5267 -9.0; 5793 -7.8; 6373 -5.6; 7010 -2.4; 7711 0.2; 8482 -0.3; 9330 -4.0; 10263 -4.4; 11289 -0.4; 12418 0.0; 13660 -0.3; 15026 -1.8; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Piston Fit GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Piston Fit ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.38 | 7.8 dB  |
| Peaking | 213 Hz  | 0.56 | -7.7 dB |
| Peaking | 3392 Hz | 1.07 | -3.4 dB |
| Peaking | 5049 Hz | 2.03 | -7.6 dB |
| Peaking | 9222 Hz | 3.28 | -2.3 dB |
| Peaking | 17 Hz   | 2.05 | 1.3 dB  |
| Peaking | 889 Hz  | 2.97 | 2.0 dB  |
| Peaking | 2452 Hz | 1.6  | -4.1 dB |
| Peaking | 2698 Hz | 4.97 | 7.8 dB  |
| Peaking | 7876 Hz | 6.04 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/1MORE%20Piston%20Fit/1MORE%20Piston%20Fit.png)