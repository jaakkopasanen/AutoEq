# Tin Audio T2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 5.8; 28 5.4; 31 5.0; 34 4.6; 37 4.2; 41 3.8; 45 3.4; 49 3.1; 54 2.7; 60 2.2; 66 1.8; 72 1.4; 79 0.9; 87 0.4; 96 -0.1; 106 -0.6; 116 -1.0; 128 -1.4; 141 -1.8; 155 -2.1; 170 -2.2; 187 -2.3; 206 -2.3; 227 -2.5; 249 -2.7; 274 -2.7; 302 -2.6; 332 -2.4; 365 -2.2; 402 -2.0; 442 -1.9; 486 -1.6; 535 -1.3; 588 -1.0; 647 -0.6; 712 -0.2; 783 0.2; 861 0.6; 947 0.2; 1042 0.3; 1146 0.6; 1261 1.0; 1387 1.6; 1526 2.5; 1678 3.4; 1846 4.3; 2031 5.3; 2234 6.0; 2457 6.0; 2703 5.4; 2973 5.0; 3270 5.0; 3597 5.0; 3957 4.6; 4353 3.6; 4788 1.5; 5267 0.9; 5793 3.8; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.6; 12418 -3.8; 13660 -9.6; 15026 -17.2; 16529 -18.3; 18182 -14.8; 20000 -17.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.72 | 6.0 dB   |
| Peaking | 2772 Hz  | 0.38 | 9.6 dB   |
| Peaking | 3320 Hz  | 0.13 | 5.5 dB   |
| Peaking | 11921 Hz | 0.26 | 34.5 dB  |
| Peaking | 14908 Hz | 0.12 | -49.1 dB |
| Peaking | 179 Hz   | 1.14 | -1.0 dB  |
| Peaking | 1276 Hz  | 1.27 | -4.0 dB  |
| Peaking | 1298 Hz  | 0.54 | 2.9 dB   |
| Peaking | 5743 Hz  | 1.77 | -4.9 dB  |
| Peaking | 6230 Hz  | 4.3  | 7.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Tin%20Audio%20T2/Tin%20Audio%20T2.png)