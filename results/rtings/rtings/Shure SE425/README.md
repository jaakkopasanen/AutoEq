# Shure SE425

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 5.6; 106 5.0; 116 3.9; 128 3.0; 141 2.2; 155 1.5; 170 1.0; 187 0.5; 206 0.1; 227 -0.2; 249 -0.3; 274 -0.4; 302 -0.4; 332 -0.4; 365 -0.3; 402 -0.2; 442 -0.0; 486 0.2; 535 0.6; 588 1.1; 647 1.5; 712 1.7; 783 1.8; 861 1.5; 947 0.5; 1042 -0.3; 1146 -0.8; 1261 -1.1; 1387 -1.2; 1526 -1.1; 1678 -0.9; 1846 -0.7; 2031 -0.4; 2234 0.2; 2457 0.9; 2703 2.0; 2973 2.4; 3270 2.0; 3597 1.4; 3957 1.3; 4353 2.5; 4788 5.4; 5267 6.0; 5793 6.0; 6373 4.5; 7010 0.7; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Shure SE425 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE425 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.32 | 7.2 dB  |
| Peaking | 721 Hz  | 0.88 | 5.7 dB  |
| Peaking | 911 Hz  | 0.15 | -4.6 dB |
| Peaking | 2802 Hz | 1.46 | 4.7 dB  |
| Peaking | 5434 Hz | 2.26 | 8.3 dB  |
| Peaking | 17 Hz   | 1    | 1.9 dB  |
| Peaking | 42 Hz   | 1.02 | -1.0 dB |
| Peaking | 93 Hz   | 2.38 | 1.3 dB  |
| Peaking | 161 Hz  | 2.14 | -0.6 dB |
| Peaking | 4744 Hz | 8.79 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Shure%20SE425/Shure%20SE425.png)