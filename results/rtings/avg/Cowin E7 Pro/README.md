# Cowin E7 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.9; 37 5.0; 41 3.2; 45 1.7; 49 0.6; 54 -0.3; 60 -1.4; 66 -2.6; 72 -2.9; 79 -1.9; 87 -1.0; 96 -0.5; 106 -0.3; 116 -0.2; 128 -0.2; 141 -0.0; 155 0.1; 170 0.3; 187 0.6; 206 1.0; 227 1.5; 249 1.8; 274 2.2; 302 2.9; 332 4.1; 365 5.5; 402 6.0; 442 5.6; 486 4.3; 535 3.7; 588 3.8; 647 4.0; 712 3.6; 783 3.4; 861 2.3; 947 0.9; 1042 -0.6; 1146 -2.3; 1261 -4.5; 1387 -6.0; 1526 -6.7; 1678 -6.1; 1846 -3.9; 2031 -2.1; 2234 -0.0; 2457 2.7; 2703 4.5; 2973 5.5; 3270 5.5; 3597 4.9; 3957 3.5; 4353 1.4; 4788 -0.3; 5267 -1.7; 5793 0.1; 6373 -1.4; 7010 -3.3; 7711 -2.8; 8482 -3.5; 9330 -5.0; 10263 -4.4; 11289 -2.1; 12418 -0.8; 13660 -2.9; 15026 -7.1; 16529 -7.4; 18182 -4.8; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cowin E7 Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cowin E7 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 2    | 7.6 dB  |
| Peaking | 497 Hz   | 0.88 | 5.6 dB  |
| Peaking | 1541 Hz  | 1.82 | -8.8 dB |
| Peaking | 3114 Hz  | 1.66 | 7.9 dB  |
| Peaking | 20977 Hz | 0.09 | -5.4 dB |
| Peaking | 38 Hz    | 3.16 | 2.7 dB  |
| Peaking | 69 Hz    | 1.84 | -3.3 dB |
| Peaking | 381 Hz   | 7.18 | 1.8 dB  |
| Peaking | 12636 Hz | 2.51 | 8.8 dB  |
| Peaking | 13598 Hz | 1.05 | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Cowin%20E7%20Pro/Cowin%20E7%20Pro.png)