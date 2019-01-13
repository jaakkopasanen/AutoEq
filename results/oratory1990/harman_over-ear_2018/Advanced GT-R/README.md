# Advanced GT-R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.4; 25 4.3; 28 4.0; 31 3.7; 34 3.7; 37 3.7; 41 3.7; 45 3.6; 49 3.5; 54 3.4; 60 3.2; 66 3.0; 72 2.8; 79 2.3; 87 1.9; 96 1.4; 106 1.0; 116 0.7; 128 0.3; 141 -0.0; 155 -0.4; 170 -0.7; 187 -0.9; 206 -1.1; 227 -1.4; 249 -1.4; 274 -1.2; 302 -0.4; 332 1.3; 365 0.9; 402 -0.2; 442 -0.9; 486 -1.5; 535 -1.0; 588 -0.7; 647 0.5; 712 -1.7; 783 -0.9; 861 -0.4; 947 0.0; 1042 0.7; 1146 2.1; 1261 3.9; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 4.2; 2234 2.5; 2457 2.8; 2703 4.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.6; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT-R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT-R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.62 | 4.2 dB  |
| Peaking | 62 Hz    | 1.18 | 2.3 dB  |
| Peaking | 1523 Hz  | 2.05 | 6.6 dB  |
| Peaking | 4298 Hz  | 0.81 | 8.0 dB  |
| Peaking | 8715 Hz  | 0.02 | -1.6 dB |
| Peaking | 347 Hz   | 6.74 | 2.6 dB  |
| Peaking | 4408 Hz  | 4.78 | -1.0 dB |
| Peaking | 6423 Hz  | 2.96 | 3.3 dB  |
| Peaking | 7543 Hz  | 2.67 | -3.3 dB |
| Peaking | 15106 Hz | 2.14 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Advanced%20GT-R/Advanced%20GT-R.png)