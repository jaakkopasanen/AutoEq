# Bose QuietComfort 25
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.0; 28 -0.1; 31 -0.9; 34 -1.4; 37 -1.7; 41 -1.8; 45 -1.8; 49 -1.7; 54 -1.6; 60 -1.4; 66 -1.3; 72 -1.3; 79 -1.3; 87 -1.4; 96 -1.5; 106 -1.7; 116 -1.8; 128 -2.0; 141 -2.1; 155 -2.1; 170 -2.0; 187 -1.9; 206 -1.8; 227 -1.4; 249 -1.2; 274 -0.8; 302 -0.4; 332 -0.0; 365 0.4; 402 0.7; 442 0.8; 486 0.9; 535 0.9; 588 1.0; 647 1.1; 712 0.5; 783 0.1; 861 -0.3; 947 -0.1; 1042 -0.2; 1146 -1.1; 1261 -2.2; 1387 -2.1; 1526 -1.5; 1678 -1.5; 1846 -1.5; 2031 -1.6; 2234 -1.6; 2457 -1.9; 2703 -0.5; 2973 4.1; 3270 6.0; 3597 1.4; 3957 -2.0; 4353 -0.4; 4788 2.2; 5267 2.3; 5793 -1.7; 6373 -3.1; 7010 2.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.1; 12418 -4.1; 13660 -4.8; 15026 -1.4; 16529 -0.4; 18182 -1.4; 20000 -0.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 2.73 | 3.7 dB  |
| Peaking | 85 Hz    | 0.47 | -1.9 dB |
| Peaking | 2222 Hz  | 1.11 | -2.4 dB |
| Peaking | 3178 Hz  | 5.92 | 8.3 dB  |
| Peaking | 13321 Hz | 3.94 | -5.8 dB |
| Peaking | 545 Hz   | 1.72 | 1.5 dB  |
| Peaking | 1310 Hz  | 5.87 | -1.8 dB |
| Peaking | 4032 Hz  | 5.72 | -4.2 dB |
| Peaking | 5519 Hz  | 1.74 | 4.5 dB  |
| Peaking | 6059 Hz  | 7.12 | -8.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)