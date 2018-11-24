# Koss UR-20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.2; 25 1.8; 28 1.3; 31 1.0; 34 0.9; 37 0.9; 41 1.0; 45 1.0; 49 0.9; 54 0.8; 60 0.5; 66 0.3; 72 0.0; 79 -0.1; 87 -0.4; 96 -0.9; 106 -1.4; 116 -1.8; 128 -2.3; 141 -2.5; 155 -2.7; 170 -2.7; 187 -2.7; 206 -2.6; 227 -2.4; 249 -2.0; 274 -2.2; 302 -2.4; 332 -2.8; 365 -3.3; 402 -3.8; 442 -4.2; 486 -4.4; 535 -3.8; 588 -3.3; 647 -3.0; 712 -2.2; 783 -1.0; 861 0.4; 947 -0.4; 1042 0.8; 1146 3.1; 1261 5.5; 1387 6.0; 1526 6.0; 1678 6.0; 1846 6.0; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 3.9; 3957 -1.9; 4353 -3.2; 4788 -0.9; 5267 0.2; 5793 -2.8; 6373 -3.9; 7010 -2.5; 7711 -5.5; 8482 -7.1; 9330 -2.6; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss UR-20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR-20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 151 Hz  | 1.3  | -2.4 dB |
| Peaking | 547 Hz  | 0.79 | -5.3 dB |
| Peaking | 1903 Hz | 0.67 | 7.9 dB  |
| Peaking | 7036 Hz | 1.17 | -5.8 dB |
| Peaking | 3342 Hz | 4.74 | 3.5 dB  |
| Peaking | 4124 Hz | 5.48 | -6.1 dB |
| Peaking | 8364 Hz | 4.41 | -8.0 dB |
| Peaking | 8825 Hz | 1.3  | 4.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Koss%20UR-20/Koss%20UR-20.png)