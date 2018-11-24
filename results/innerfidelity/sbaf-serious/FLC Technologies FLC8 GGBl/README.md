# FLC Technologies FLC8 GGBl

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.8; 23 -1.9; 25 -2.0; 28 -2.1; 31 -2.2; 34 -2.2; 37 -2.1; 41 -2.1; 45 -2.1; 49 -2.1; 54 -2.1; 60 -2.2; 66 -2.3; 72 -2.3; 79 -2.5; 87 -2.6; 96 -2.7; 106 -2.7; 116 -2.7; 128 -2.7; 141 -2.8; 155 -2.8; 170 -2.7; 187 -2.5; 206 -2.4; 227 -2.2; 249 -2.0; 274 -1.8; 302 -1.6; 332 -1.3; 365 -1.0; 402 -0.7; 442 -0.2; 486 -0.1; 535 0.2; 588 0.7; 647 0.9; 712 0.8; 783 1.1; 861 1.0; 947 0.4; 1042 -0.3; 1146 -0.7; 1261 -0.8; 1387 -0.5; 1526 0.2; 1678 1.1; 1846 2.6; 2031 4.1; 2234 5.0; 2457 5.9; 2703 5.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technologies FLC8 GGBl GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 GGBl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.24 | -2.0 dB |
| Peaking | 178 Hz  | 0.73 | -1.9 dB |
| Peaking | 1467 Hz | 1.4  | -6.4 dB |
| Peaking | 2213 Hz | 0.63 | 7.7 dB  |
| Peaking | 5305 Hz | 2.28 | 4.0 dB  |
| Peaking | 795 Hz  | 1.77 | 0.6 dB  |
| Peaking | 1063 Hz | 4.64 | -1.0 dB |
| Peaking | 3965 Hz | 2.64 | 1.3 dB  |
| Peaking | 6423 Hz | 4.09 | 4.3 dB  |
| Peaking | 6876 Hz | 1.26 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20GGBl/FLC%20Technologies%20FLC8%20GGBl.png)