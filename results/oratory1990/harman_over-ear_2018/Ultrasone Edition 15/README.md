# Ultrasone Edition 15

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.2; 41 4.5; 45 3.9; 49 3.2; 54 2.2; 60 1.3; 66 0.7; 72 0.0; 79 -0.7; 87 -1.7; 96 -2.6; 106 -3.5; 116 -4.2; 128 -4.7; 141 -5.0; 155 -5.2; 170 -5.1; 187 -5.2; 206 -5.1; 227 -4.9; 249 -4.7; 274 -4.0; 302 -3.8; 332 -3.2; 365 -2.7; 402 -1.9; 442 -2.7; 486 -3.2; 535 -2.7; 588 -2.2; 647 -1.6; 712 -1.0; 783 -0.6; 861 -0.4; 947 -0.2; 1042 0.3; 1146 0.8; 1261 1.3; 1387 1.8; 1526 2.0; 1678 1.9; 1846 2.3; 2031 1.0; 2234 -0.5; 2457 -0.0; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.8; 4353 3.0; 4788 2.1; 5267 0.5; 5793 2.7; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -6.3; 15026 -6.4; 16529 -2.8; 18182 -1.6; 20000 -0.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Edition 15 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Edition 15 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.45 | 6.9 dB  |
| Peaking | 154 Hz   | 0.5  | -6.3 dB |
| Peaking | 3361 Hz  | 1.94 | 6.7 dB  |
| Peaking | 6425 Hz  | 6.88 | 5.2 dB  |
| Peaking | 14645 Hz | 2.89 | -7.9 dB |
| Peaking | 531 Hz   | 3.93 | -1.4 dB |
| Peaking | 1950 Hz  | 0.95 | 2.7 dB  |
| Peaking | 2279 Hz  | 4.94 | -5.0 dB |
| Peaking | 11753 Hz | 3.27 | 2.0 dB  |
| Peaking | 15620 Hz | 0.05 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Ultrasone%20Edition%2015/Ultrasone%20Edition%2015.png)