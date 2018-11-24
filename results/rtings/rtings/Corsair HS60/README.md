# Corsair HS60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 21 -2.5; 23 -2.7; 25 -3.0; 28 -3.3; 31 -3.6; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.5; 54 -4.6; 60 -4.9; 66 -5.3; 72 -5.6; 79 -6.0; 87 -6.4; 96 -6.8; 106 -7.1; 116 -7.1; 128 -7.1; 141 -7.0; 155 -6.7; 170 -6.1; 187 -5.3; 206 -4.3; 227 -3.2; 249 -2.3; 274 -1.3; 302 -0.5; 332 0.1; 365 0.6; 402 0.8; 442 0.4; 486 -0.3; 535 -1.2; 588 -2.2; 647 -2.6; 712 -2.4; 783 -1.9; 861 -0.8; 947 0.7; 1042 -0.2; 1146 0.2; 1261 0.5; 1387 0.5; 1526 0.7; 1678 0.5; 1846 0.0; 2031 -0.5; 2234 -0.5; 2457 -0.6; 2703 -0.9; 2973 -0.9; 3270 0.1; 3597 2.6; 3957 3.2; 4353 -0.9; 4788 -2.8; 5267 0.0; 5793 0.9; 6373 3.6; 7010 2.5; 7711 -1.2; 8482 -8.4; 9330 -10.3; 10263 -7.2; 11289 -4.7; 12418 -3.4; 13660 -1.6; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair HS60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair HS60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 53 Hz   | 0.52 | -4.3 dB  |
| Peaking | 135 Hz  | 1.24 | -5.6 dB  |
| Peaking | 675 Hz  | 4.48 | -2.7 dB  |
| Peaking | 6877 Hz | 3.21 | 8.0 dB   |
| Peaking | 9119 Hz | 2.1  | -12.1 dB |
| Peaking | 196 Hz  | 3.8  | -1.0 dB  |
| Peaking | 366 Hz  | 2.74 | 1.9 dB   |
| Peaking | 3024 Hz | 3.21 | -1.7 dB  |
| Peaking | 3815 Hz | 3.98 | 4.9 dB   |
| Peaking | 4643 Hz | 6.18 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Corsair%20HS60/Corsair%20HS60.png)