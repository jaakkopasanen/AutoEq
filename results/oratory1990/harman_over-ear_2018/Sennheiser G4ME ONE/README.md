# Sennheiser G4ME ONE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 5.7; 96 4.3; 106 3.1; 116 2.3; 128 1.2; 141 0.2; 155 -0.4; 170 -0.9; 187 -1.3; 206 -1.6; 227 -1.6; 249 -1.4; 274 -1.2; 302 -1.0; 332 -0.8; 365 -0.6; 402 -0.5; 442 -0.4; 486 -0.2; 535 -0.0; 588 0.3; 647 0.4; 712 0.4; 783 0.6; 861 0.5; 947 0.1; 1042 -0.0; 1146 0.2; 1261 0.8; 1387 2.1; 1526 3.3; 1678 4.1; 1846 4.1; 2031 3.3; 2234 2.1; 2457 1.2; 2703 1.0; 2973 1.9; 3270 3.4; 3597 4.9; 3957 5.9; 4353 4.7; 4788 0.7; 5267 -1.6; 5793 -0.4; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -1.2; 16529 -6.5; 18182 -8.6; 20000 -16.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser G4ME ONE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser G4ME ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 58 Hz    | 0.26 | 7.4 dB   |
| Peaking | 184 Hz   | 0.79 | -6.1 dB  |
| Peaking | 1759 Hz  | 2.6  | 4.4 dB   |
| Peaking | 3867 Hz  | 4.09 | 6.2 dB   |
| Peaking | 6507 Hz  | 9.24 | 5.2 dB   |
| Peaking | 17 Hz    | 1.26 | 1.6 dB   |
| Peaking | 43 Hz    | 0.49 | -0.8 dB  |
| Peaking | 81 Hz    | 3.65 | 1.5 dB   |
| Peaking | 3288 Hz  | 9.26 | 1.1 dB   |
| Peaking | 19832 Hz | 1.34 | -15.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20G4ME%20ONE/Sennheiser%20G4ME%20ONE.png)