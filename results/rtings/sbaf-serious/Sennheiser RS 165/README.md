# Sennheiser RS 165

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.4; 23 -1.5; 25 -1.6; 28 -1.6; 31 -1.5; 34 -1.3; 37 -1.1; 41 -0.7; 45 -0.4; 49 0.0; 54 0.4; 60 0.6; 66 0.4; 72 0.1; 79 -0.2; 87 -0.9; 96 -1.6; 106 -2.2; 116 -2.6; 128 -2.6; 141 -2.6; 155 -2.1; 170 -1.6; 187 -0.8; 206 0.2; 227 1.4; 249 2.5; 274 2.7; 302 2.5; 332 3.0; 365 4.1; 402 5.3; 442 5.8; 486 5.5; 535 4.9; 588 4.2; 647 3.7; 712 3.7; 783 2.5; 861 1.4; 947 0.4; 1042 0.0; 1146 0.5; 1261 0.2; 1387 0.1; 1526 0.3; 1678 1.2; 1846 1.7; 2031 2.4; 2234 3.1; 2457 3.5; 2703 4.1; 2973 5.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.1; 5793 5.9; 6373 4.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 165 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 165 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.86 | -1.7 dB |
| Peaking | 59 Hz   | 1.81 | 1.4 dB  |
| Peaking | 130 Hz  | 1.6  | -3.4 dB |
| Peaking | 448 Hz  | 1.22 | 5.8 dB  |
| Peaking | 4024 Hz | 1.08 | 6.7 dB  |
| Peaking | 170 Hz  | 3.96 | -0.2 dB |
| Peaking | 721 Hz  | 4.27 | 1.5 dB  |
| Peaking | 1063 Hz | 1.8  | -1.4 dB |
| Peaking | 6088 Hz | 4.11 | 2.9 dB  |
| Peaking | 8093 Hz | 1.47 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sennheiser%20RS%20165/Sennheiser%20RS%20165.png)