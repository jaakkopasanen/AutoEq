# iMetal iM590
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -7.5; 23 -7.4; 25 -7.4; 28 -7.4; 31 -7.3; 34 -7.2; 37 -7.2; 41 -7.1; 45 -7.1; 49 -7.0; 54 -7.0; 60 -7.0; 66 -6.9; 72 -6.8; 79 -6.9; 87 -6.9; 96 -7.0; 106 -6.8; 116 -6.6; 128 -6.4; 141 -6.2; 155 -5.9; 170 -5.5; 187 -5.1; 206 -4.7; 227 -4.2; 249 -3.7; 274 -3.2; 302 -2.7; 332 -2.1; 365 -1.6; 402 -1.1; 442 -0.5; 486 -0.2; 535 0.1; 588 0.7; 647 0.9; 712 1.0; 783 1.1; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.0; 1387 -1.7; 1526 -2.5; 1678 -3.7; 1846 -4.7; 2031 -5.5; 2234 -5.9; 2457 -4.2; 2703 -1.5; 2973 2.2; 3270 5.0; 3597 6.0; 3957 4.8; 4353 0.8; 4788 -3.1; 5267 -3.4; 5793 -2.9; 6373 -2.4; 7010 1.1; 7711 0.3; 8482 0.0; 9330 -1.2; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`iMetal iM590 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `iMetal iM590 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.26 | -7.2 dB |
| Peaking | 148 Hz  | 0.86 | -3.6 dB |
| Peaking | 2207 Hz | 1.91 | -8.6 dB |
| Peaking | 3655 Hz | 1.59 | 10.6 dB |
| Peaking | 5037 Hz | 2.24 | -8.0 dB |
| Peaking | 274 Hz  | 2.05 | -0.8 dB |
| Peaking | 707 Hz  | 1.49 | 1.8 dB  |
| Peaking | 1582 Hz | 3    | -0.9 dB |
| Peaking | 6367 Hz | 8.61 | -1.6 dB |
| Peaking | 7091 Hz | 7.54 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/iMetal%20iM590/iMetal%20iM590.png)