# Fiio FH1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -6.9; 23 -7.5; 25 -7.8; 28 -7.5; 31 -7.4; 34 -7.4; 37 -7.3; 41 -7.3; 45 -7.3; 49 -7.3; 54 -7.6; 60 -7.6; 66 -8.0; 72 -7.9; 79 -8.1; 87 -8.2; 96 -7.7; 106 -8.0; 116 -7.6; 128 -7.6; 141 -7.3; 155 -7.0; 170 -6.8; 187 -6.5; 206 -6.2; 227 -5.7; 249 -5.3; 274 -4.8; 302 -4.4; 332 -3.9; 365 -3.4; 402 -2.9; 442 -2.5; 486 -2.0; 535 -1.5; 588 -1.1; 647 -0.6; 712 -0.1; 783 0.3; 861 0.5; 947 0.3; 1042 -0.4; 1146 -1.5; 1261 -2.6; 1387 -3.4; 1526 -3.9; 1678 -4.0; 1846 -4.0; 2031 -3.8; 2234 -3.1; 2457 -1.8; 2703 -0.5; 2973 0.3; 3270 0.7; 3597 1.6; 3957 4.6; 4353 5.2; 4788 1.4; 5267 3.4; 5793 5.2; 6373 5.2; 7010 2.5; 7711 -3.3; 8482 -6.6; 9330 -3.6; 10263 -0.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -2.6; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.22 | -8.3 dB |
| Peaking | 1791 Hz | 2.09 | -4.5 dB |
| Peaking | 4124 Hz | 6.14 | 5.7 dB  |
| Peaking | 6251 Hz | 2.67 | 6.7 dB  |
| Peaking | 8357 Hz | 4.06 | -8.7 dB |
| Peaking | 24 Hz   | 1.41 | -1.1 dB |
| Peaking | 44 Hz   | 1.19 | 1.1 dB  |
| Peaking | 223 Hz  | 0.83 | -0.6 dB |
| Peaking | 870 Hz  | 1.39 | 2.0 dB  |
| Peaking | 1299 Hz | 3.25 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Fiio%20FH1/Fiio%20FH1.png)