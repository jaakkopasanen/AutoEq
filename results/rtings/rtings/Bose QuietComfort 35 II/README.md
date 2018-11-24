# Bose QuietComfort 35 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -5.7; 23 -5.1; 25 -4.7; 28 -4.4; 31 -4.3; 34 -4.3; 37 -4.3; 41 -4.4; 45 -4.4; 49 -4.4; 54 -4.4; 60 -4.3; 66 -4.2; 72 -4.2; 79 -4.1; 87 -4.0; 96 -4.0; 106 -3.9; 116 -3.9; 128 -3.8; 141 -3.8; 155 -3.7; 170 -3.5; 187 -3.4; 206 -3.1; 227 -2.8; 249 -2.6; 274 -2.5; 302 -2.4; 332 -2.2; 365 -2.0; 402 -1.9; 442 -1.9; 486 -1.8; 535 -1.6; 588 -1.4; 647 -1.1; 712 -0.9; 783 -0.5; 861 -0.1; 947 -0.1; 1042 0.1; 1146 0.6; 1261 0.8; 1387 0.3; 1526 -0.3; 1678 -1.9; 1846 -3.8; 2031 -5.1; 2234 -4.5; 2457 -3.1; 2703 -1.9; 2973 -1.2; 3270 0.6; 3597 -1.8; 3957 -3.5; 4353 -2.0; 4788 0.3; 5267 4.2; 5793 0.9; 6373 -4.9; 7010 -0.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.0; 13660 -2.4; 15026 -2.6; 16529 -0.2; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.8  | -6.0 dB |
| Peaking | 79 Hz    | 0.2  | -3.9 dB |
| Peaking | 1398 Hz  | 1.65 | 2.5 dB  |
| Peaking | 2035 Hz  | 2.01 | -5.7 dB |
| Peaking | 14375 Hz | 3.02 | -3.1 dB |
| Peaking | 3339 Hz  | 5.52 | 3.2 dB  |
| Peaking | 3909 Hz  | 3.53 | -4.1 dB |
| Peaking | 5496 Hz  | 5.37 | 7.8 dB  |
| Peaking | 6295 Hz  | 5.13 | -7.6 dB |
| Peaking | 7330 Hz  | 4.31 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Bose%20QuietComfort%2035%20II/Bose%20QuietComfort%2035%20II.png)