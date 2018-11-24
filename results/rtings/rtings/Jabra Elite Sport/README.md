# Jabra Elite Sport

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.8; 28 -3.8; 31 -3.8; 34 -3.8; 37 -3.9; 41 -4.0; 45 -4.0; 49 -4.0; 54 -4.2; 60 -4.6; 66 -5.0; 72 -5.3; 79 -5.6; 87 -6.1; 96 -6.4; 106 -6.9; 116 -7.3; 128 -7.7; 141 -8.0; 155 -8.0; 170 -8.0; 187 -7.7; 206 -7.4; 227 -7.0; 249 -6.3; 274 -5.3; 302 -4.1; 332 -3.2; 365 -2.6; 402 -2.2; 442 -2.0; 486 -1.9; 535 -1.6; 588 -1.1; 647 -0.5; 712 -0.0; 783 0.1; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.2; 1261 0.3; 1387 0.8; 1526 0.9; 1678 0.3; 1846 -0.6; 2031 -1.3; 2234 -1.0; 2457 -0.3; 2703 0.6; 2973 1.6; 3270 2.3; 3597 2.9; 3957 3.4; 4353 3.5; 4788 4.7; 5267 6.0; 5793 5.9; 6373 3.3; 7010 0.3; 7711 -1.9; 8482 -2.7; 9330 -4.8; 10263 -7.4; 11289 -6.0; 12418 -1.6; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jabra Elite Sport GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jabra Elite Sport ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.2  | -3.4 dB |
| Peaking | 125 Hz   | 0.92 | -4.0 dB |
| Peaking | 211 Hz   | 1.09 | -4.6 dB |
| Peaking | 5244 Hz  | 1.8  | 6.6 dB  |
| Peaking | 10147 Hz | 2.28 | -8.1 dB |
| Peaking | 1629 Hz  | 1.82 | 1.7 dB  |
| Peaking | 2030 Hz  | 2.42 | -2.7 dB |
| Peaking | 3321 Hz  | 3.47 | 1.3 dB  |
| Peaking | 7576 Hz  | 7.93 | -1.8 dB |
| Peaking | 13441 Hz | 4.75 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jabra%20Elite%20Sport/Jabra%20Elite%20Sport.png)