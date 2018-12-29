# 1MORE Quad Driver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.4; 28 -0.1; 31 -0.7; 34 -1.3; 37 -1.8; 41 -2.5; 45 -3.0; 49 -3.6; 54 -4.4; 60 -5.0; 66 -5.9; 72 -6.2; 79 -7.0; 87 -7.1; 96 -7.4; 106 -8.0; 116 -8.0; 128 -8.5; 141 -8.4; 155 -8.5; 170 -8.6; 187 -8.6; 206 -8.5; 227 -8.3; 249 -8.1; 274 -7.8; 302 -7.3; 332 -6.8; 365 -6.2; 402 -5.7; 442 -5.2; 486 -4.6; 535 -3.9; 588 -3.2; 647 -2.6; 712 -1.8; 783 -1.1; 861 -0.5; 947 -0.1; 1042 -0.0; 1146 -0.2; 1261 -0.3; 1387 -0.2; 1526 -0.0; 1678 0.3; 1846 0.7; 2031 1.0; 2234 1.2; 2457 1.2; 2703 1.1; 2973 1.4; 3270 1.8; 3597 1.6; 3957 0.4; 4353 -1.0; 4788 -0.5; 5267 1.3; 5793 3.1; 6373 4.8; 7010 1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.7; 12418 -6.9; 13660 -16.5; 15026 -25.6; 16529 -29.4; 18182 -28.2; 20000 -21.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`1MORE Quad Driver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.81 | 4.3 dB   |
| Peaking | 118 Hz   | 0.46 | -7.6 dB  |
| Peaking | 308 Hz   | 0.84 | -3.8 dB  |
| Peaking | 8597 Hz  | 0.29 | 25.8 dB  |
| Peaking | 16679 Hz | 0.33 | -46.6 dB |
| Peaking | 2251 Hz  | 2.5  | 0.8 dB   |
| Peaking | 7771 Hz  | 6.74 | -2.3 dB  |
| Peaking | 8850 Hz  | 4.21 | -2.0 dB  |
| Peaking | 11444 Hz | 2.33 | 5.0 dB   |
| Peaking | 14602 Hz | 3.65 | -6.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)