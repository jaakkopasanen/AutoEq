# Grado GW100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 -1.4; 25 -2.9; 28 -4.8; 31 -6.2; 34 -6.9; 37 -7.2; 41 -7.0; 45 -6.4; 49 -5.8; 54 -5.4; 60 -5.5; 66 -5.8; 72 -5.9; 79 -5.9; 87 -6.0; 96 -6.3; 106 -6.7; 116 -7.2; 128 -7.8; 141 -8.4; 155 -8.9; 170 -9.4; 187 -9.4; 206 -9.1; 227 -8.7; 249 -7.9; 274 -6.9; 302 -6.3; 332 -5.9; 365 -5.3; 402 -5.0; 442 -4.7; 486 -4.4; 535 -4.1; 588 -3.5; 647 -2.9; 712 -2.1; 783 -1.4; 861 -0.8; 947 -0.3; 1042 0.1; 1146 0.2; 1261 -0.1; 1387 -0.6; 1526 -1.7; 1678 -3.3; 1846 -6.9; 2031 -9.7; 2234 -8.9; 2457 -5.5; 2703 -2.7; 2973 -1.3; 3270 -0.6; 3597 -0.8; 3957 -1.1; 4353 0.6; 4788 2.9; 5267 2.3; 5793 3.0; 6373 0.1; 7010 -0.0; 7711 -2.2; 8482 -8.0; 9330 -9.6; 10263 -4.0; 11289 -0.1; 12418 -0.4; 13660 -1.8; 15026 -1.5; 16529 -1.4; 18182 -2.5; 20000 -3.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado GW100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GW100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 38 Hz   |  1.33 | -5.9 dB  |
| Peaking | 182 Hz  |  0.55 | -9.1 dB  |
| Peaking | 2107 Hz |  3.58 | -10.5 dB |
| Peaking | 5438 Hz |  2.72 | 3.8 dB   |
| Peaking | 9045 Hz |  4.09 | -11.0 dB |
| Peaking | 19 Hz   |  2.44 | 2.9 dB   |
| Peaking | 549 Hz  |  2.68 | -1.2 dB  |
| Peaking | 1117 Hz |  1.81 | 1.8 dB   |
| Peaking | 1855 Hz |  8.39 | -1.6 dB  |
| Peaking | 7357 Hz | 11.69 | 1.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Grado%20GW100/Grado%20GW100.png)