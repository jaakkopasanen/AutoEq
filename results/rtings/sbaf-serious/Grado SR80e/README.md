# Grado SR80e

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.8; 34 5.3; 37 4.5; 41 3.5; 45 2.6; 49 1.9; 54 1.2; 60 0.6; 66 0.1; 72 -0.1; 79 -0.3; 87 -0.5; 96 -0.7; 106 -0.9; 116 -1.0; 128 -1.1; 141 -1.1; 155 -1.0; 170 -0.9; 187 -0.9; 206 -0.8; 227 -0.6; 249 -0.4; 274 -0.2; 302 -0.2; 332 -0.2; 365 0.1; 402 0.0; 442 0.0; 486 0.1; 535 0.1; 588 0.2; 647 0.3; 712 0.4; 783 0.3; 861 0.2; 947 0.1; 1042 0.0; 1146 0.1; 1261 -0.1; 1387 -0.9; 1526 -2.0; 1678 -3.3; 1846 -6.8; 2031 -8.9; 2234 -7.6; 2457 -5.8; 2703 -4.0; 2973 -2.0; 3270 -0.4; 3597 -0.6; 3957 -3.1; 4353 -2.1; 4788 0.8; 5267 0.8; 5793 0.9; 6373 -1.4; 7010 -4.0; 7711 -4.4; 8482 -7.2; 9330 -8.6; 10263 -3.0; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado SR80e GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR80e ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 1.43 | 6.8 dB   |
| Peaking | 2112 Hz | 2.69 | -9.3 dB  |
| Peaking | 7267 Hz | 3.97 | -4.0 dB  |
| Peaking | 8618 Hz | 0.93 | 2.8 dB   |
| Peaking | 9059 Hz | 3.56 | -11.4 dB |
| Peaking | 40 Hz   | 2.44 | 1.0 dB   |
| Peaking | 121 Hz  | 0.78 | -1.3 dB  |
| Peaking | 884 Hz  | 0.98 | 0.8 dB   |
| Peaking | 4142 Hz | 8.01 | -4.0 dB  |
| Peaking | 5095 Hz | 3.68 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Grado%20SR80e/Grado%20SR80e.png)