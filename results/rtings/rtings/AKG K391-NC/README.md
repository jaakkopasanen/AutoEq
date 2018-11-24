# AKG K391-NC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.7; 28 1.5; 31 1.2; 34 1.1; 37 1.0; 41 0.9; 45 0.8; 49 0.8; 54 0.7; 60 0.5; 66 0.3; 72 0.1; 79 -0.0; 87 -0.2; 96 -0.4; 106 -0.7; 116 -1.1; 128 -1.4; 141 -1.7; 155 -2.0; 170 -2.3; 187 -2.6; 206 -3.0; 227 -3.5; 249 -3.9; 274 -4.4; 302 -4.8; 332 -5.2; 365 -5.6; 402 -5.9; 442 -5.9; 486 -5.7; 535 -5.2; 588 -4.2; 647 -2.8; 712 -1.4; 783 -0.1; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -0.9; 1526 -0.7; 1678 -0.5; 1846 -0.3; 2031 0.1; 2234 0.9; 2457 1.9; 2703 2.0; 2973 1.1; 3270 -0.7; 3597 -2.6; 3957 -4.2; 4353 -4.9; 4788 -2.3; 5267 1.5; 5793 4.0; 6373 3.4; 7010 2.4; 7711 0.2; 8482 -5.0; 9330 -10.0; 10263 -7.6; 11289 -0.5; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K391-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K391-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.58 | 2.4 dB   |
| Peaking | 372 Hz   | 0.86 | -6.1 dB  |
| Peaking | 4274 Hz  | 2.26 | -11.8 dB |
| Peaking | 5761 Hz  | 0.7  | 8.7 dB   |
| Peaking | 9380 Hz  | 2.93 | -15.3 dB |
| Peaking | 549 Hz   | 3.46 | -1.5 dB  |
| Peaking | 843 Hz   | 2.11 | 2.5 dB   |
| Peaking | 1668 Hz  | 0.86 | -1.4 dB  |
| Peaking | 2571 Hz  | 3.71 | 2.1 dB   |
| Peaking | 16617 Hz | 2.98 | -0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/AKG%20K391-NC/AKG%20K391-NC.png)