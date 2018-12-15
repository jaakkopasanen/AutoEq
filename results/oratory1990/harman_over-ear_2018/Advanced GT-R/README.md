# Advanced GT-R

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.7; 96 4.7; 106 3.9; 116 3.0; 128 2.2; 141 1.4; 155 0.6; 170 -0.0; 187 -0.6; 206 -1.1; 227 -1.4; 249 -1.4; 274 -1.2; 302 -0.4; 332 1.3; 365 0.9; 402 -0.2; 442 -0.9; 486 -1.5; 535 -1.0; 588 -0.7; 647 0.5; 712 -1.7; 783 -0.9; 861 -0.4; 947 0.0; 1042 0.7; 1146 2.1; 1261 3.9; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 4.2; 2234 2.5; 2457 2.8; 2703 4.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -1.6; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced GT-R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced GT-R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 64 Hz    | 0.17 | 6.9 dB  |
| Peaking | 195 Hz   | 0.96 | -6.3 dB |
| Peaking | 770 Hz   | 0.63 | -3.0 dB |
| Peaking | 1507 Hz  | 1.72 | 7.0 dB  |
| Peaking | 4231 Hz  | 1.07 | 6.7 dB  |
| Peaking | 483 Hz   | 7.78 | -1.3 dB |
| Peaking | 2388 Hz  | 6.25 | -1.6 dB |
| Peaking | 2904 Hz  | 4.4  | 2.2 dB  |
| Peaking | 6099 Hz  | 4.89 | 3.3 dB  |
| Peaking | 21559 Hz | 0.05 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Advanced%20GT-R/Advanced%20GT-R.png)