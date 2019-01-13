# Bose QuietComfort 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.4; 25 -4.6; 28 -4.7; 31 -4.7; 34 -4.7; 37 -4.6; 41 -4.4; 45 -4.3; 49 -4.2; 54 -4.1; 60 -4.0; 66 -4.2; 72 -4.2; 79 -4.4; 87 -4.6; 96 -4.8; 106 -4.8; 116 -4.9; 128 -5.0; 141 -5.0; 155 -5.0; 170 -4.7; 187 -4.5; 206 -4.1; 227 -3.6; 249 -3.1; 274 -2.6; 302 -2.2; 332 -1.7; 365 -1.3; 402 -0.9; 442 -0.7; 486 -0.6; 535 -0.4; 588 -0.2; 647 -0.4; 712 -0.5; 783 -0.5; 861 -0.1; 947 0.1; 1042 -0.2; 1146 -0.5; 1261 -0.7; 1387 -0.5; 1526 0.9; 1678 1.4; 1846 3.2; 2031 4.8; 2234 5.9; 2457 6.0; 2703 6.0; 2973 5.9; 3270 5.5; 3597 4.1; 3957 2.5; 4353 1.4; 4788 4.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.41 | -4.3 dB |
| Peaking | 148 Hz  | 0.7  | -4.4 dB |
| Peaking | 2604 Hz | 1.75 | 6.6 dB  |
| Peaking | 5882 Hz | 2.42 | 6.6 dB  |
| Peaking | 7916 Hz | 2.15 | -1.8 dB |
| Peaking | 1308 Hz | 3.32 | -1.6 dB |
| Peaking | 2013 Hz | 6.85 | 1.3 dB  |
| Peaking | 4107 Hz | 7.33 | -2.7 dB |
| Peaking | 4179 Hz | 2.81 | 2.4 dB  |
| Peaking | 4413 Hz | 9.39 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Bose%20QuietComfort%203/Bose%20QuietComfort%203.png)