# Bose QuietComfort 35 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 -5.3; 23 -4.8; 25 -4.4; 28 -4.2; 31 -4.2; 34 -4.3; 37 -4.4; 41 -4.6; 45 -4.7; 49 -4.8; 54 -4.7; 60 -4.6; 66 -4.4; 72 -4.2; 79 -3.9; 87 -3.6; 96 -3.5; 106 -3.4; 116 -3.4; 128 -3.3; 141 -3.2; 155 -3.1; 170 -2.9; 187 -2.8; 206 -2.6; 227 -2.3; 249 -2.1; 274 -1.8; 302 -1.6; 332 -1.3; 365 -1.0; 402 -0.8; 442 -0.7; 486 -0.6; 535 -0.4; 588 -0.3; 647 -0.1; 712 -0.0; 783 -0.0; 861 0.0; 947 -0.1; 1042 0.2; 1146 0.8; 1261 1.0; 1387 0.3; 1526 -0.7; 1678 -2.3; 1846 -3.7; 2031 -4.6; 2234 -4.0; 2457 -2.6; 2703 -1.3; 2973 -0.1; 3270 2.4; 3597 0.4; 3957 -2.3; 4353 -2.0; 4788 0.1; 5267 4.6; 5793 2.4; 6373 -2.4; 7010 1.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  1.91 | -4.9 dB |
| Peaking | 47 Hz   |  0.23 | -4.3 dB |
| Peaking | 2063 Hz |  3.59 | -5.1 dB |
| Peaking | 5456 Hz |  8.8  | 6.6 dB  |
| Peaking | 6183 Hz | 10.95 | -3.7 dB |
| Peaking | 1231 Hz |  3.6  | 1.6 dB  |
| Peaking | 3065 Hz |  1.3  | -1.2 dB |
| Peaking | 3321 Hz |  5.18 | 4.8 dB  |
| Peaking | 4073 Hz |  3.16 | -3.7 dB |
| Peaking | 4910 Hz |  1.22 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20QuietComfort%2035%20II/Bose%20QuietComfort%2035%20II.png)