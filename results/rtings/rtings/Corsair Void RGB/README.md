# Corsair Void RGB

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.8; 45 4.9; 49 3.8; 54 2.7; 60 1.7; 66 1.1; 72 0.7; 79 0.5; 87 0.5; 96 0.7; 106 1.1; 116 1.5; 128 1.9; 141 2.3; 155 2.7; 170 3.2; 187 3.8; 206 4.4; 227 4.7; 249 3.1; 274 4.3; 302 4.9; 332 5.2; 365 5.4; 402 5.2; 442 4.8; 486 4.9; 535 4.9; 588 5.0; 647 5.0; 712 4.7; 783 3.9; 861 2.7; 947 0.8; 1042 -0.3; 1146 0.5; 1261 2.2; 1387 1.8; 1526 2.9; 1678 4.3; 1846 5.4; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.9; 5793 4.7; 6373 1.0; 7010 1.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair Void RGB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair Void RGB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.01 | 6.8 dB  |
| Peaking | 199 Hz  | 1.8  | 3.1 dB  |
| Peaking | 372 Hz  | 1.52 | 4.6 dB  |
| Peaking | 633 Hz  | 2.69 | 3.7 dB  |
| Peaking | 3144 Hz | 0.79 | 6.9 dB  |
| Peaking | 77 Hz   | 3.65 | -1.0 dB |
| Peaking | 1063 Hz | 6.11 | -2.6 dB |
| Peaking | 1942 Hz | 3.57 | 2.0 dB  |
| Peaking | 5223 Hz | 2.25 | 6.0 dB  |
| Peaking | 5643 Hz | 0.91 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Corsair%20Void%20RGB/Corsair%20Void%20RGB.png)