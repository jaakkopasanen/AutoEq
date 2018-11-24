# Jaybird X3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 -1.1; 23 -1.1; 25 -1.1; 28 -1.1; 31 -1.1; 34 -1.0; 37 -1.0; 41 -1.0; 45 -1.0; 49 -1.0; 54 -1.1; 60 -1.4; 66 -1.7; 72 -1.9; 79 -2.2; 87 -2.6; 96 -3.0; 106 -3.4; 116 -3.9; 128 -4.2; 141 -4.5; 155 -4.6; 170 -4.5; 187 -4.7; 206 -4.9; 227 -4.8; 249 -4.3; 274 -3.7; 302 -3.2; 332 -2.7; 365 -2.1; 402 -1.6; 442 -0.9; 486 -0.2; 535 0.4; 588 1.0; 647 1.6; 712 1.8; 783 1.7; 861 1.3; 947 0.5; 1042 -0.4; 1146 -0.9; 1261 -1.3; 1387 -1.5; 1526 -1.6; 1678 -2.0; 1846 -2.5; 2031 -3.1; 2234 -3.2; 2457 -3.1; 2703 -2.7; 2973 -1.3; 3270 0.4; 3597 1.8; 3957 2.7; 4353 2.9; 4788 4.0; 5267 4.9; 5793 4.0; 6373 -0.7; 7010 -6.1; 7711 -5.1; 8482 -1.4; 9330 -2.9; 10263 -6.9; 11289 -3.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 166 Hz   | 0.8  | -5.1 dB  |
| Peaking | 2348 Hz  | 1.6  | -4.7 dB  |
| Peaking | 5802 Hz  | 1.06 | 8.1 dB   |
| Peaking | 7135 Hz  | 3.22 | -12.7 dB |
| Peaking | 10399 Hz | 4.59 | -8.5 dB  |
| Peaking | 22 Hz    | 0.94 | -1.0 dB  |
| Peaking | 167 Hz   | 1.94 | 1.7 dB   |
| Peaking | 243 Hz   | 0.71 | -1.5 dB  |
| Peaking | 730 Hz   | 1.22 | 3.2 dB   |
| Peaking | 1192 Hz  | 1.62 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Jaybird%20X3/Jaybird%20X3.png)