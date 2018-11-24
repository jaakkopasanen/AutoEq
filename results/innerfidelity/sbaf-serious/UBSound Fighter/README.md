# UBSound Fighter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.5; 23 -5.9; 25 -6.2; 28 -6.6; 31 -6.9; 34 -7.2; 37 -7.5; 41 -7.8; 45 -8.0; 49 -8.2; 54 -8.5; 60 -8.7; 66 -8.9; 72 -9.1; 79 -9.3; 87 -9.4; 96 -9.6; 106 -9.5; 116 -9.4; 128 -9.3; 141 -9.2; 155 -9.0; 170 -8.6; 187 -8.2; 206 -7.8; 227 -7.2; 249 -6.7; 274 -6.1; 302 -5.4; 332 -4.8; 365 -4.2; 402 -3.4; 442 -2.6; 486 -2.1; 535 -1.5; 588 -0.4; 647 0.2; 712 1.0; 783 1.8; 861 0.2; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.3; 1387 -1.2; 1526 -1.9; 1678 -2.4; 1846 -2.4; 2031 -1.4; 2234 0.6; 2457 3.7; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.0; 6373 -3.2; 7010 0.6; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`UBSound Fighter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UBSound Fighter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.37 | -7.2 dB |
| Peaking | 135 Hz  | 0.79 | -5.2 dB |
| Peaking | 268 Hz  | 1.39 | -3.0 dB |
| Peaking | 1836 Hz | 2.44 | -5.4 dB |
| Peaking | 3322 Hz | 1.08 | 7.4 dB  |
| Peaking | 697 Hz  | 0.85 | -0.9 dB |
| Peaking | 738 Hz  | 2.72 | 3.0 dB  |
| Peaking | 3481 Hz | 6.31 | -1.3 dB |
| Peaking | 5412 Hz | 3.41 | 4.4 dB  |
| Peaking | 6323 Hz | 5.41 | -6.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UBSound%20Fighter/UBSound%20Fighter.png)