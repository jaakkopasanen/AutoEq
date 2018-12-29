# Sennheiser HD 820

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.5; 23 -1.8; 25 -2.1; 28 -2.5; 31 -2.7; 34 -3.0; 37 -3.2; 41 -3.4; 45 -3.6; 49 -3.7; 54 -3.6; 60 -3.3; 66 -2.4; 72 -0.2; 79 1.7; 87 0.0; 96 -2.8; 106 -4.3; 116 -5.2; 128 -5.4; 141 -5.2; 155 -5.3; 170 -4.7; 187 -3.5; 206 -1.2; 227 1.8; 249 5.5; 274 6.0; 302 6.0; 332 6.0; 365 5.4; 402 4.1; 442 3.1; 486 2.6; 535 2.0; 588 1.7; 647 1.5; 712 1.3; 783 1.0; 861 0.4; 947 0.1; 1042 0.1; 1146 0.5; 1261 1.4; 1387 2.3; 1526 3.0; 1678 3.5; 1846 3.7; 2031 3.7; 2234 3.6; 2457 2.7; 2703 1.9; 2973 2.4; 3270 4.6; 3597 6.0; 3957 6.0; 4353 5.8; 4788 1.4; 5267 0.7; 5793 3.2; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 1.48 | -3.7 dB |
| Peaking | 159 Hz  | 1.31 | -8.2 dB |
| Peaking | 289 Hz  | 1.29 | 8.8 dB  |
| Peaking | 1844 Hz | 2.17 | 3.5 dB  |
| Peaking | 3871 Hz | 2.13 | 6.0 dB  |
| Peaking | 60 Hz   | 3    | -2.1 dB |
| Peaking | 80 Hz   | 4.11 | 4.5 dB  |
| Peaking | 108 Hz  | 4.14 | -2.0 dB |
| Peaking | 5023 Hz | 8.75 | -3.1 dB |
| Peaking | 6347 Hz | 5.27 | 3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)