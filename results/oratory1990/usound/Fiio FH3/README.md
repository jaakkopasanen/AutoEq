# Fiio FH3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 -2.7; 23 -3.4; 25 -3.7; 28 -3.8; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.3; 45 -4.4; 49 -4.6; 54 -4.9; 60 -5.1; 66 -5.5; 72 -5.6; 79 -6.0; 87 -6.0; 96 -5.8; 106 -6.1; 116 -5.8; 128 -6.1; 141 -5.8; 155 -5.6; 170 -5.5; 187 -5.4; 206 -5.1; 227 -4.8; 249 -4.5; 274 -4.1; 302 -3.7; 332 -3.3; 365 -2.9; 402 -2.5; 442 -2.1; 486 -1.7; 535 -1.3; 588 -1.0; 647 -0.7; 712 -0.3; 783 -0.0; 861 0.2; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.5; 1387 -1.8; 1526 -1.8; 1678 -1.2; 1846 -0.3; 2031 0.8; 2234 1.9; 2457 2.9; 2703 3.6; 2973 4.0; 3270 3.9; 3597 3.7; 3957 3.9; 4353 4.4; 4788 4.7; 5267 4.2; 5793 2.0; 6373 -1.7; 7010 -3.9; 7711 -6.3; 8482 -5.7; 9330 -0.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.2; 15026 -2.5; 16529 -0.9; 18182 -1.5; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fiio FH3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fiio FH3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.34 | -3.3 dB |
| Peaking | 156 Hz   | 0.48 | -4.5 dB |
| Peaking | 2934 Hz  | 2.67 | 3.7 dB  |
| Peaking | 4799 Hz  | 2.12 | 5.3 dB  |
| Peaking | 7699 Hz  | 3.12 | -7.8 dB |
| Peaking | 884 Hz   | 1.85 | 1.2 dB  |
| Peaking | 1457 Hz  | 2.03 | -2.3 dB |
| Peaking | 2299 Hz  | 3.46 | 1.1 dB  |
| Peaking | 10615 Hz | 2.01 | 2.2 dB  |
| Peaking | 16901 Hz | 0.42 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Fiio%20FH3/Fiio%20FH3.png)