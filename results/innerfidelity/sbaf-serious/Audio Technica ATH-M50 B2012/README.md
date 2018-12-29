# Audio Technica ATH-M50 B2012
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 -0.0; 28 -0.3; 31 -0.6; 34 -0.7; 37 -0.8; 41 -0.9; 45 -0.9; 49 -0.9; 54 -0.8; 60 -0.8; 66 -0.5; 72 0.1; 79 0.2; 87 1.9; 96 3.4; 106 0.5; 116 -0.9; 128 -1.7; 141 -1.8; 155 -1.0; 170 -0.5; 187 -0.7; 206 0.1; 227 1.1; 249 1.8; 274 2.4; 302 2.7; 332 1.6; 365 1.0; 402 0.5; 442 0.1; 486 -0.5; 535 -0.6; 588 -0.4; 647 -0.5; 712 -0.6; 783 -0.3; 861 -0.4; 947 -0.2; 1042 0.0; 1146 0.0; 1261 -0.3; 1387 -0.8; 1526 -1.7; 1678 -3.1; 1846 -3.7; 2031 -3.5; 2234 -2.9; 2457 -1.6; 2703 -0.3; 2973 1.5; 3270 2.9; 3597 3.5; 3957 0.4; 4353 -2.5; 4788 0.5; 5267 5.6; 5793 6.0; 6373 5.5; 7010 2.3; 7711 -2.8; 8482 -6.7; 9330 -4.8; 10263 -0.3; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50 B2012 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 290 Hz  |  3.91 | 3.0 dB  |
| Peaking | 1939 Hz |  2.3  | -4.1 dB |
| Peaking | 3361 Hz |  5.93 | 4.1 dB  |
| Peaking | 6030 Hz |  3.43 | 7.6 dB  |
| Peaking | 8563 Hz |  4.33 | -8.4 dB |
| Peaking | 12 Hz   |  1.14 | 1.8 dB  |
| Peaking | 44 Hz   |  1.09 | -1.1 dB |
| Peaking | 95 Hz   |  5.44 | 4.2 dB  |
| Peaking | 131 Hz  |  2.74 | -2.1 dB |
| Peaking | 4357 Hz | 10.57 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M50%20B2012/Audio%20Technica%20ATH-M50%20B2012.png)