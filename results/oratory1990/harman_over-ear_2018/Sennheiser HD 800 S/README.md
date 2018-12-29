# Sennheiser HD 800 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.2; 28 4.8; 31 4.5; 34 4.3; 37 4.0; 41 3.8; 45 3.7; 49 3.6; 54 3.5; 60 3.5; 66 3.2; 72 2.7; 79 2.0; 87 1.3; 96 0.7; 106 0.1; 116 -0.3; 128 -0.7; 141 -0.9; 155 -1.2; 170 -1.5; 187 -1.6; 206 -1.7; 227 -1.7; 249 -1.7; 274 -1.5; 302 -1.3; 332 -1.1; 365 -0.9; 402 -0.8; 442 -0.7; 486 -0.6; 535 -0.4; 588 -0.3; 647 -0.2; 712 -0.1; 783 -0.1; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.6; 1261 1.4; 1387 2.1; 1526 2.4; 1678 2.4; 1846 2.2; 2031 2.3; 2234 2.1; 2457 1.5; 2703 1.0; 2973 1.2; 3270 2.2; 3597 1.9; 3957 0.7; 4353 0.9; 4788 -0.3; 5267 -3.7; 5793 -3.9; 6373 -2.3; 7010 -1.0; 7711 -0.5; 8482 0.0; 9330 0.0; 10263 -0.1; 11289 -5.3; 12418 -7.2; 13660 -5.7; 15026 -4.1; 16529 -5.3; 18182 -7.2; 20000 -7.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 800 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.07 | 5.7 dB  |
| Peaking | 58 Hz    | 2.38 | 2.9 dB  |
| Peaking | 5608 Hz  | 6.76 | -4.7 dB |
| Peaking | 12585 Hz | 3.58 | -6.5 dB |
| Peaking | 18840 Hz | 0.98 | -7.9 dB |
| Peaking | 82 Hz    | 1.98 | 1.1 dB  |
| Peaking | 210 Hz   | 0.67 | -1.9 dB |
| Peaking | 1750 Hz  | 1.55 | 2.7 dB  |
| Peaking | 3429 Hz  | 3.84 | 2.0 dB  |
| Peaking | 14521 Hz | 2.85 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)