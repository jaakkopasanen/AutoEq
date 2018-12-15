# NAD Viso HP70

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.7; 54 5.0; 60 4.2; 66 3.5; 72 3.0; 79 2.4; 87 1.7; 96 1.0; 106 0.7; 116 0.6; 128 0.9; 141 1.4; 155 1.0; 170 0.2; 187 -0.1; 206 0.1; 227 0.7; 249 1.4; 274 2.2; 302 2.7; 332 2.3; 365 2.1; 402 2.0; 442 1.5; 486 0.8; 535 0.3; 588 0.5; 647 0.3; 712 -0.1; 783 0.4; 861 0.4; 947 0.2; 1042 0.1; 1146 -0.1; 1261 -0.7; 1387 0.2; 1526 1.5; 1678 2.6; 1846 3.0; 2031 3.1; 2234 3.3; 2457 3.0; 2703 2.5; 2973 1.9; 3270 1.0; 3597 -0.7; 3957 -0.3; 4353 -2.8; 4788 -2.5; 5267 -1.2; 5793 -1.2; 6373 -1.8; 7010 -3.0; 7711 -0.8; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.6; 13660 -4.3; 15026 -1.7; 16529 -0.0; 18182 -0.2; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD Viso HP70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD Viso HP70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.69 | 6.7 dB  |
| Peaking | 328 Hz   | 2.31 | 2.6 dB  |
| Peaking | 2320 Hz  | 1.56 | 4.0 dB  |
| Peaking | 4827 Hz  | 1.28 | -2.7 dB |
| Peaking | 13829 Hz | 5.07 | -4.7 dB |
| Peaking | 186 Hz   | 5.31 | -0.4 dB |
| Peaking | 196 Hz   | 5.64 | -0.7 dB |
| Peaking | 1250 Hz  | 5.87 | -1.7 dB |
| Peaking | 4039 Hz  | 0.17 | 0.2 dB  |
| Peaking | 4452 Hz  | 9.11 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/NAD%20Viso%20HP70/NAD%20Viso%20HP70.png)