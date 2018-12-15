# Bose QuietComfort 25

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -3.0; 23 -2.8; 25 -2.7; 28 -2.4; 31 -2.3; 34 -2.3; 37 -2.4; 41 -2.6; 45 -2.8; 49 -2.9; 54 -3.0; 60 -3.2; 66 -3.3; 72 -3.4; 79 -3.5; 87 -3.6; 96 -3.7; 106 -3.9; 116 -4.1; 128 -4.3; 141 -4.3; 155 -4.3; 170 -4.2; 187 -4.1; 206 -3.7; 227 -3.4; 249 -3.2; 274 -3.0; 302 -2.8; 332 -2.6; 365 -2.3; 402 -2.3; 442 -2.2; 486 -2.0; 535 -1.8; 588 -1.5; 647 -1.2; 712 -0.7; 783 -0.4; 861 -0.2; 947 0.0; 1042 -0.1; 1146 -1.0; 1261 -2.8; 1387 -4.2; 1526 -4.4; 1678 -5.6; 1846 -6.6; 2031 -6.5; 2234 -5.5; 2457 -3.8; 2703 -1.7; 2973 -0.6; 3270 -3.0; 3597 -5.8; 3957 -5.1; 4353 -2.0; 4788 2.6; 5267 5.0; 5793 -2.0; 6373 -8.9; 7010 -2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.3; 12418 -3.7; 13660 -3.2; 15026 -5.0; 16529 -6.9; 18182 -7.2; 20000 -8.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 25 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 25 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 113 Hz   | 0.31 | -4.1 dB  |
| Peaking | 1879 Hz  | 2.13 | -6.8 dB  |
| Peaking | 3781 Hz  | 4.56 | -5.6 dB  |
| Peaking | 5083 Hz  | 8.96 | 7.0 dB   |
| Peaking | 19003 Hz | 0.58 | -8.0 dB  |
| Peaking | 21 Hz    | 2.15 | -1.9 dB  |
| Peaking | 939 Hz   | 4.39 | 1.5 dB   |
| Peaking | 5472 Hz  | 9.13 | 4.0 dB   |
| Peaking | 6362 Hz  | 4.59 | -13.0 dB |
| Peaking | 7212 Hz  | 1.65 | 4.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2025/Bose%20QuietComfort%2025.png)