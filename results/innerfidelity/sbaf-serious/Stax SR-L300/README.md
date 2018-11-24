# Stax SR-L300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.3; 49 4.3; 54 3.5; 60 2.8; 66 2.2; 72 1.8; 79 1.5; 87 1.1; 96 0.9; 106 0.6; 116 0.9; 128 0.8; 141 0.9; 155 1.0; 170 1.1; 187 1.1; 206 1.2; 227 1.4; 249 1.4; 274 1.6; 302 1.6; 332 1.7; 365 1.7; 402 1.8; 442 1.8; 486 1.6; 535 1.5; 588 1.9; 647 1.7; 712 1.3; 783 1.1; 861 0.5; 947 -0.1; 1042 0.4; 1146 -0.0; 1261 -1.1; 1387 -1.0; 1526 0.1; 1678 1.8; 1846 2.9; 2031 2.7; 2234 1.6; 2457 0.9; 2703 0.6; 2973 2.0; 3270 2.7; 3597 2.8; 3957 2.1; 4353 0.7; 4788 0.4; 5267 1.7; 5793 0.6; 6373 0.2; 7010 0.5; 7711 -0.2; 8482 -3.0; 9330 -2.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.1; 20000 -3.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-L300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-L300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.79 | 6.6 dB  |
| Peaking | 385 Hz  | 0.86 | 1.8 dB  |
| Peaking | 3163 Hz | 1.02 | 2.1 dB  |
| Peaking | 8834 Hz | 4.64 | -5.7 dB |
| Peaking | 8858 Hz | 2.04 | 1.5 dB  |
| Peaking | 636 Hz  | 5.01 | 0.8 dB  |
| Peaking | 1346 Hz | 3.64 | -2.3 dB |
| Peaking | 1907 Hz | 2.56 | 3.5 dB  |
| Peaking | 2656 Hz | 1.38 | -2.5 dB |
| Peaking | 3356 Hz | 3.51 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-L300/Stax%20SR-L300.png)