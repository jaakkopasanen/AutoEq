# Tin Audio T2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.8; 96 4.8; 106 3.7; 116 2.7; 128 1.7; 141 0.8; 155 0.0; 170 -0.7; 187 -1.3; 206 -1.8; 227 -2.3; 249 -2.7; 274 -2.7; 302 -2.6; 332 -2.4; 365 -2.2; 402 -2.0; 442 -1.9; 486 -1.6; 535 -1.3; 588 -1.0; 647 -0.6; 712 -0.2; 783 0.2; 861 0.6; 947 0.2; 1042 0.3; 1146 0.6; 1261 1.0; 1387 1.6; 1526 2.5; 1678 3.4; 1846 4.3; 2031 5.3; 2234 6.0; 2457 6.0; 2703 5.4; 2973 5.0; 3270 5.0; 3597 5.0; 3957 4.6; 4353 3.6; 4788 1.5; 5267 0.9; 5793 3.8; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.6; 12418 -3.8; 13660 -9.6; 15026 -17.2; 16529 -18.3; 18182 -14.8; 20000 -17.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 49 Hz    | 0.42 | 7.4 dB   |
| Peaking | 2292 Hz  | 0.2  | 11.5 dB  |
| Peaking | 3234 Hz  | 0.3  | 14.8 dB  |
| Peaking | 10362 Hz | 0.48 | 24.5 dB  |
| Peaking | 10405 Hz | 0.08 | -36.9 dB |
| Peaking | 23 Hz    | 2.36 | 1.5 dB   |
| Peaking | 5039 Hz  | 5.25 | -3.0 dB  |
| Peaking | 6259 Hz  | 6.86 | 4.6 dB   |
| Peaking | 15742 Hz | 2.7  | -8.4 dB  |
| Peaking | 18269 Hz | 0.74 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Tin%20Audio%20T2/Tin%20Audio%20T2.png)