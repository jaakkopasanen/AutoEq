# Sennheiser HD 820

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.9; 25 4.8; 28 4.8; 31 4.9; 34 5.0; 37 5.1; 41 5.2; 45 5.1; 49 5.1; 54 5.1; 60 4.9; 66 4.6; 72 4.2; 79 3.7; 87 3.1; 96 2.5; 106 1.9; 116 1.5; 128 1.1; 141 0.9; 155 0.9; 170 1.1; 187 1.8; 206 3.2; 227 5.4; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 4.8; 442 3.8; 486 3.0; 535 2.5; 588 2.0; 647 1.2; 712 0.5; 783 -0.0; 861 -0.2; 947 -0.2; 1042 0.1; 1146 0.4; 1261 1.0; 1387 1.5; 1526 2.2; 1678 2.9; 1846 2.9; 2031 2.2; 2234 2.4; 2457 3.4; 2703 4.0; 2973 5.5; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 4.7; 6373 2.0; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser HD 820 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 820 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.77 | 4.8 dB  |
| Peaking | 61 Hz   | 1.51 | 3.4 dB  |
| Peaking | 310 Hz  | 1.38 | 6.6 dB  |
| Peaking | 3399 Hz | 1.19 | 5.7 dB  |
| Peaking | 5169 Hz | 3.23 | 3.7 dB  |
| Peaking | 163 Hz  | 2.88 | -1.2 dB |
| Peaking | 234 Hz  | 7.63 | 2.0 dB  |
| Peaking | 890 Hz  | 3.15 | -1.3 dB |
| Peaking | 1645 Hz | 5.09 | 1.7 dB  |
| Peaking | 8743 Hz | 3.02 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sennheiser%20HD%20820/Sennheiser%20HD%20820.png)