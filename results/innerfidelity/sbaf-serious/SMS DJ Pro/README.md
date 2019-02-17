# SMS DJ Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.8; 23 -11.0; 25 -11.1; 28 -11.2; 31 -11.2; 34 -11.1; 37 -11.0; 41 -10.8; 45 -10.6; 49 -10.3; 54 -9.9; 60 -9.3; 66 -8.7; 72 -8.4; 79 -8.6; 87 -10.0; 96 -11.7; 106 -11.5; 116 -10.1; 128 -9.0; 141 -8.6; 155 -7.5; 170 -7.3; 187 -7.5; 206 -7.8; 227 -7.8; 249 -8.1; 274 -8.5; 302 -8.6; 332 -8.8; 365 -10.1; 402 -10.8; 442 -10.0; 486 -10.0; 535 -9.4; 588 -8.5; 647 -8.0; 712 -6.9; 783 -5.9; 861 -6.9; 947 -6.5; 1042 -6.4; 1146 -6.0; 1261 -6.2; 1387 -6.7; 1526 -7.3; 1678 -7.6; 1846 -7.2; 2031 -6.0; 2234 -5.1; 2457 -3.9; 2703 -2.8; 2973 -1.8; 3270 -1.8; 3597 -2.1; 3957 -3.3; 4353 -2.7; 4788 -4.5; 5267 -2.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SMS DJ Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS DJ Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.68 | -5.0 dB |
| Peaking | 102 Hz  |  3.14 | -4.5 dB |
| Peaking | 416 Hz  |  1.55 | -4.1 dB |
| Peaking | 3226 Hz |  2.16 | 4.9 dB  |
| Peaking | 5938 Hz |  3.65 | 6.1 dB  |
| Peaking | 764 Hz  | 12.04 | 1.5 dB  |
| Peaking | 1170 Hz |  3.69 | 0.8 dB  |
| Peaking | 1699 Hz |  3.04 | -1.8 dB |
| Peaking | 2512 Hz |  4.51 | 0.9 dB  |
| Peaking | 8160 Hz |  4.77 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20DJ%20Pro/SMS%20DJ%20Pro.png)