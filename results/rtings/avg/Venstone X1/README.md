# Venstone X1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.4; 23 -2.9; 25 -3.3; 28 -3.9; 31 -4.3; 34 -4.7; 37 -5.1; 41 -5.5; 45 -5.9; 49 -6.3; 54 -6.7; 60 -7.2; 66 -7.6; 72 -8.0; 79 -8.4; 87 -8.9; 96 -9.3; 106 -9.8; 116 -10.3; 128 -10.6; 141 -10.9; 155 -10.9; 170 -10.9; 187 -10.8; 206 -10.6; 227 -10.2; 249 -9.9; 274 -9.8; 302 -9.6; 332 -9.3; 365 -8.7; 402 -7.9; 442 -7.0; 486 -5.9; 535 -4.6; 588 -3.5; 647 -2.6; 712 -1.9; 783 -1.7; 861 -1.1; 947 -0.4; 1042 0.3; 1146 1.0; 1261 2.0; 1387 3.0; 1526 4.3; 1678 5.5; 1846 5.9; 2031 4.9; 2234 2.9; 2457 1.1; 2703 0.8; 2973 0.9; 3270 0.3; 3597 -0.9; 3957 -2.6; 4353 -4.1; 4788 -6.9; 5267 -11.1; 5793 -8.7; 6373 -3.1; 7010 -0.2; 7711 -2.9; 8482 -5.9; 9330 -1.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -2.0; 15026 -4.0; 16529 -6.7; 18182 -7.2; 20000 -0.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Venstone X1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venstone X1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 122 Hz   | 0.37 | -9.7 dB  |
| Peaking | 320 Hz   | 0.98 | -3.9 dB  |
| Peaking | 1734 Hz  | 1.67 | 6.6 dB   |
| Peaking | 5308 Hz  | 3.27 | -11.5 dB |
| Peaking | 17475 Hz | 1.56 | -8.1 dB  |
| Peaking | 29 Hz    | 2.05 | -0.7 dB  |
| Peaking | 5877 Hz  | 6.15 | -1.4 dB  |
| Peaking | 6928 Hz  | 4.52 | 3.7 dB   |
| Peaking | 8471 Hz  | 4.22 | -7.0 dB  |
| Peaking | 9904 Hz  | 1.99 | 2.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Venstone%20X1/Venstone%20X1.png)