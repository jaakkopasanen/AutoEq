# Bose QuietComfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.0; 23 -2.8; 25 -2.7; 28 -2.4; 31 -2.3; 34 -2.3; 37 -2.4; 41 -2.6; 45 -2.8; 49 -2.9; 54 -3.0; 60 -3.2; 66 -3.3; 72 -3.4; 79 -3.5; 87 -3.6; 96 -3.7; 106 -3.9; 116 -4.1; 128 -4.3; 141 -4.3; 155 -4.3; 170 -4.2; 187 -4.1; 206 -3.7; 227 -3.4; 249 -3.2; 274 -3.0; 302 -2.8; 332 -2.6; 365 -2.3; 402 -2.3; 442 -2.2; 486 -2.0; 535 -1.8; 588 -1.5; 647 -1.2; 712 -0.7; 783 -0.4; 861 -0.2; 947 0.0; 1042 -0.1; 1146 -1.0; 1261 -2.8; 1387 -4.2; 1526 -4.4; 1678 -5.6; 1846 -6.6; 2031 -6.5; 2234 -5.5; 2457 -3.8; 2703 -1.5; 2973 -0.1; 3270 -2.3; 3597 -4.7; 3957 -3.9; 4353 -0.7; 4788 4.4; 5267 6.0; 5793 0.4; 6373 -7.7; 7010 -1.6; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.5; 12418 -0.4; 13660 -0.1; 15026 -2.4; 16529 -3.9; 18182 -2.8; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 113 Hz   |  0.31 | -4.1 dB  |
| Peaking | 1886 Hz  |  2.14 | -7.0 dB  |
| Peaking | 3836 Hz  |  4.47 | -5.8 dB  |
| Peaking | 5241 Hz  |  3.3  | 8.8 dB   |
| Peaking | 6335 Hz  |  6.63 | -11.1 dB |
| Peaking | 21 Hz    |  2.27 | -2.0 dB  |
| Peaking | 988 Hz   |  2.73 | 1.5 dB   |
| Peaking | 1347 Hz  |  5.63 | -1.9 dB  |
| Peaking | 2941 Hz  | 10.74 | 2.2 dB   |
| Peaking | 17251 Hz |  1.52 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)