# Oppo PM1 2014 Alt Pads
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.3; 28 2.1; 31 1.9; 34 1.8; 37 1.7; 41 1.7; 45 1.6; 49 1.7; 54 1.8; 60 2.1; 66 1.8; 72 0.7; 79 0.1; 87 -0.2; 96 -0.9; 106 -1.1; 116 -1.3; 128 -1.7; 141 -1.9; 155 -2.0; 170 -2.0; 187 -2.2; 206 -2.2; 227 -2.1; 249 -2.4; 274 -2.8; 302 -3.1; 332 -3.0; 365 -1.5; 402 -0.1; 442 -0.5; 486 -1.2; 535 -1.5; 588 -1.2; 647 -1.7; 712 -2.1; 783 -2.2; 861 -2.5; 947 -0.6; 1042 0.0; 1146 -0.3; 1261 -0.3; 1387 -0.8; 1526 -1.1; 1678 -1.2; 1846 -0.5; 2031 0.0; 2234 0.5; 2457 1.5; 2703 2.3; 2973 3.5; 3270 3.8; 3597 3.8; 3957 4.6; 4353 4.9; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.8; 9330 -1.9; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM1 2014 Alt Pads GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM1 2014 Alt Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 63 Hz   | 0.13 | 2.8 dB  |
| Peaking | 153 Hz  | 0.69 | -4.5 dB |
| Peaking | 301 Hz  | 3.01 | -2.9 dB |
| Peaking | 745 Hz  | 1.32 | -2.5 dB |
| Peaking | 4798 Hz | 1.42 | 6.4 dB  |
| Peaking | 1678 Hz | 3.82 | -1.5 dB |
| Peaking | 3017 Hz | 3.57 | 1.7 dB  |
| Peaking | 4465 Hz | 4.9  | -1.2 dB |
| Peaking | 6246 Hz | 5.02 | 2.6 dB  |
| Peaking | 8834 Hz | 2.94 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Oppo%20PM1%202014%20Alt%20Pads/Oppo%20PM1%202014%20Alt%20Pads.png)