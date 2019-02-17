# Superlux HD 681
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -1.2; 72 -2.1; 79 -2.7; 87 -2.9; 96 -3.4; 106 -3.8; 116 -4.1; 128 -4.4; 141 -4.8; 155 -4.9; 170 -4.5; 187 -4.3; 206 -4.7; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.3; 332 -3.9; 365 -3.9; 402 -3.8; 442 -4.0; 486 -4.1; 535 -4.5; 588 -4.5; 647 -4.5; 712 -4.9; 783 -5.3; 861 -5.7; 947 -6.3; 1042 -6.7; 1146 -7.2; 1261 -8.0; 1387 -9.1; 1526 -10.0; 1678 -10.1; 1846 -11.1; 2031 -11.8; 2234 -11.9; 2457 -11.8; 2703 -10.6; 2973 -9.5; 3270 -8.0; 3597 -6.2; 3957 -6.6; 4353 -8.3; 4788 -11.6; 5267 -9.3; 5793 -11.4; 6373 -8.3; 7010 -6.8; 7711 -13.1; 8482 -16.5; 9330 -15.9; 10263 -12.8; 11289 -7.0; 12418 -6.5; 13660 -7.8; 15026 -8.2; 16529 -6.5; 18182 -6.5; 20000 -11.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Superlux HD 681 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 35 Hz    |  0.45 | 6.5 dB   |
| Peaking | 463 Hz   |  0.73 | 2.5 dB   |
| Peaking | 1524 Hz  |  2.02 | -2.0 dB  |
| Peaking | 2248 Hz  |  1.77 | -5.2 dB  |
| Peaking | 8860 Hz  |  2.65 | -10.9 dB |
| Peaking | 3742 Hz  |  4.65 | 2.9 dB   |
| Peaking | 4676 Hz  | 13.6  | -3.2 dB  |
| Peaking | 6305 Hz  |  1.95 | -5.0 dB  |
| Peaking | 6759 Hz  |  5.45 | 8.4 dB   |
| Peaking | 11739 Hz |  5.92 | 2.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -7.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)