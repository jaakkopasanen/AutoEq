# Beyerdynamic DT 250-250
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.7; 34 5.3; 37 5.0; 41 4.6; 45 4.2; 49 4.0; 54 3.7; 60 3.5; 66 3.4; 72 3.3; 79 4.1; 87 4.6; 96 4.0; 106 3.9; 116 3.4; 128 2.1; 141 1.5; 155 1.5; 170 2.0; 187 1.1; 206 1.0; 227 1.1; 249 1.2; 274 1.2; 302 1.0; 332 1.1; 365 1.3; 402 1.3; 442 1.3; 486 1.0; 535 0.9; 588 1.0; 647 0.7; 712 0.3; 783 0.3; 861 -0.2; 947 -0.6; 1042 0.5; 1146 0.2; 1261 -1.1; 1387 -2.1; 1526 -2.9; 1678 -3.2; 1846 -2.7; 2031 -1.6; 2234 -0.6; 2457 0.6; 2703 1.8; 2973 3.6; 3270 5.0; 3597 4.0; 3957 2.6; 4353 1.6; 4788 2.2; 5267 4.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.7; 10263 -0.2; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 250-250 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.18 | 4.7 dB  |
| Peaking | 32 Hz   | 1.5  | 2.5 dB  |
| Peaking | 87 Hz   | 0.65 | 3.5 dB  |
| Peaking | 3321 Hz | 4.48 | 5.2 dB  |
| Peaking | 5871 Hz | 3.66 | 6.6 dB  |
| Peaking | 101 Hz  | 1.93 | 2.7 dB  |
| Peaking | 106 Hz  | 0.86 | -3.0 dB |
| Peaking | 449 Hz  | 0.1  | 0.9 dB  |
| Peaking | 1660 Hz | 2.02 | -4.4 dB |
| Peaking | 9419 Hz | 4.46 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)