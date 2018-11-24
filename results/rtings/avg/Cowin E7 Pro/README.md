# Cowin E7 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.0; 41 3.2; 45 1.7; 49 0.6; 54 -0.3; 60 -1.4; 66 -2.6; 72 -2.9; 79 -1.9; 87 -1.0; 96 -0.5; 106 -0.3; 116 -0.2; 128 -0.2; 141 -0.0; 155 0.1; 170 0.3; 187 0.6; 206 1.0; 227 1.5; 249 1.8; 274 2.2; 302 2.9; 332 4.1; 365 5.5; 402 6.0; 442 5.6; 486 4.3; 535 3.7; 588 3.8; 647 4.0; 712 3.6; 783 3.4; 861 2.3; 947 0.9; 1042 -0.6; 1146 -2.3; 1261 -4.5; 1387 -6.0; 1526 -6.7; 1678 -6.1; 1846 -3.9; 2031 -2.1; 2234 -0.0; 2457 2.7; 2703 4.5; 2973 5.5; 3270 5.5; 3597 4.9; 3957 3.5; 4353 1.4; 4788 -0.3; 5267 -1.7; 5793 0.0; 6373 -1.4; 7010 -3.0; 7711 -1.8; 8482 -2.0; 9330 -3.7; 10263 -3.9; 11289 -2.2; 12418 -0.9; 13660 -2.9; 15026 -7.1; 16529 -7.4; 18182 -4.8; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-8.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 1.96 | 7.4 dB  |
| Peaking | 497 Hz   | 0.89 | 5.6 dB  |
| Peaking | 1554 Hz  | 1.86 | -8.6 dB |
| Peaking | 3043 Hz  | 1.91 | 7.4 dB  |
| Peaking | 18581 Hz | 0.29 | -5.8 dB |
| Peaking | 71 Hz    | 2.37 | -3.5 dB |
| Peaking | 386 Hz   | 4.66 | 1.8 dB  |
| Peaking | 522 Hz   | 5.79 | -1.8 dB |
| Peaking | 12594 Hz | 2.63 | 7.8 dB  |
| Peaking | 13534 Hz | 1.09 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7%20Pro/Cowin%20E7%20Pro.png)