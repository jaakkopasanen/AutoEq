# FLC Technology FLC8 C C Bk Ligh
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.8; 49 5.6; 54 5.3; 60 4.8; 66 4.5; 72 4.1; 79 3.6; 87 3.1; 96 2.5; 106 2.2; 116 1.9; 128 1.5; 141 1.1; 155 0.9; 170 0.8; 187 0.6; 206 0.5; 227 0.5; 249 0.4; 274 0.5; 302 0.6; 332 0.7; 365 0.9; 402 1.0; 442 1.3; 486 1.3; 535 1.5; 588 1.9; 647 1.8; 712 1.7; 783 1.7; 861 1.5; 947 0.7; 1042 -0.4; 1146 -1.3; 1261 -1.7; 1387 -2.0; 1526 -1.5; 1678 -0.5; 1846 0.8; 2031 1.6; 2234 1.9; 2457 2.2; 2703 1.6; 2973 3.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 3.5; 7010 -1.4; 7711 -3.6; 8482 -3.9; 9330 -4.0; 10263 -3.5; 11289 -0.8; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FLC Technology FLC8 C C Bk Ligh GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Bk Ligh ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.43 | 6.3 dB  |
| Peaking | 1382 Hz  | 4.13 | -2.8 dB |
| Peaking | 3600 Hz  | 1.66 | 4.9 dB  |
| Peaking | 5888 Hz  | 1.59 | 9.0 dB  |
| Peaking | 7772 Hz  | 1.54 | -8.9 dB |
| Peaking | 688 Hz   | 1.24 | 1.9 dB  |
| Peaking | 1129 Hz  | 5.09 | -1.6 dB |
| Peaking | 1604 Hz  | 7.82 | -0.8 dB |
| Peaking | 10319 Hz | 4.4  | -2.7 dB |
| Peaking | 11286 Hz | 1.84 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh.png)