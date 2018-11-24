# Corsair Void RGB

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 4.6; 49 3.5; 54 2.4; 60 1.5; 66 0.9; 72 0.7; 79 0.7; 87 0.8; 96 1.2; 106 1.6; 116 2.0; 128 2.4; 141 2.9; 155 3.3; 170 3.9; 187 4.3; 206 4.9; 227 5.2; 249 3.7; 274 5.0; 302 5.7; 332 6.0; 365 6.0; 402 6.0; 442 5.9; 486 6.0; 535 6.0; 588 6.0; 647 6.0; 712 5.5; 783 4.4; 861 2.9; 947 0.9; 1042 -0.2; 1146 0.7; 1261 2.4; 1387 1.8; 1526 2.5; 1678 3.9; 1846 5.4; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 5.9; 6373 3.5; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Corsair Void RGB GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Corsair Void RGB ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.09 | 6.8 dB  |
| Peaking | 299 Hz  | 0.75 | 5.4 dB  |
| Peaking | 605 Hz  | 2.19 | 3.9 dB  |
| Peaking | 2420 Hz | 1.39 | 5.6 dB  |
| Peaking | 4810 Hz | 1.61 | 5.6 dB  |
| Peaking | 77 Hz   | 2.91 | -1.2 dB |
| Peaking | 164 Hz  | 3.21 | 0.7 dB  |
| Peaking | 946 Hz  | 1.61 | 1.8 dB  |
| Peaking | 1022 Hz | 3.69 | -4.3 dB |
| Peaking | 8492 Hz | 3.58 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Corsair%20Void%20RGB/Corsair%20Void%20RGB.png)