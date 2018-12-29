# Fostex TH900mk2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 -2.8; 23 -3.0; 25 -3.3; 28 -3.6; 31 -3.8; 34 -4.0; 37 -4.1; 41 -4.1; 45 -4.2; 49 -4.2; 54 -4.2; 60 -4.2; 66 -4.0; 72 -4.0; 79 -4.2; 87 -4.5; 96 -4.6; 106 -4.7; 116 -4.5; 128 -4.6; 141 -4.4; 155 -4.2; 170 -3.7; 187 -3.5; 206 -3.1; 227 -2.6; 249 -2.2; 274 -1.7; 302 -1.1; 332 -0.3; 365 0.4; 402 1.1; 442 1.9; 486 2.1; 535 2.0; 588 1.9; 647 1.3; 712 0.3; 783 1.2; 861 0.6; 947 0.0; 1042 0.1; 1146 0.6; 1261 1.2; 1387 1.4; 1526 1.4; 1678 1.3; 1846 1.4; 2031 1.6; 2234 1.8; 2457 3.2; 2703 3.4; 2973 1.9; 3270 0.4; 3597 1.8; 3957 1.7; 4353 -0.0; 4788 -1.4; 5267 -3.1; 5793 -6.0; 6373 -3.1; 7010 -1.6; 7711 -3.6; 8482 -1.8; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -3.3; 20000 -7.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fostex TH900mk2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex TH900mk2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.63 | -3.2 dB |
| Peaking | 129 Hz  |  0.56 | -4.1 dB |
| Peaking | 477 Hz  |  1.63 | 3.1 dB  |
| Peaking | 2765 Hz |  0.91 | 2.8 dB  |
| Peaking | 5843 Hz |  2.36 | -5.9 dB |
| Peaking | 983 Hz  |  8.32 | -0.7 dB |
| Peaking | 3227 Hz |  6.19 | -4.2 dB |
| Peaking | 3246 Hz |  2.66 | 2.4 dB  |
| Peaking | 6710 Hz | 11.4  | 2.1 dB  |
| Peaking | 7879 Hz |  8.55 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20TH900mk2/Fostex%20TH900mk2.png)