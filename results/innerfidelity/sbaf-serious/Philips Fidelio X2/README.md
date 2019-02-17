# Philips Fidelio X2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.5; 25 -4.3; 28 -5.5; 31 -6.5; 34 -7.4; 37 -8.2; 41 -9.1; 45 -9.8; 49 -10.4; 54 -10.9; 60 -11.2; 66 -11.5; 72 -11.6; 79 -11.7; 87 -11.7; 96 -11.5; 106 -11.1; 116 -10.6; 128 -10.2; 141 -10.0; 155 -9.8; 170 -9.3; 187 -9.1; 206 -9.6; 227 -10.5; 249 -9.8; 274 -9.3; 302 -9.0; 332 -8.8; 365 -8.7; 402 -8.7; 442 -8.5; 486 -8.7; 535 -8.7; 588 -8.6; 647 -8.7; 712 -8.7; 783 -8.3; 861 -7.9; 947 -6.8; 1042 -6.2; 1146 -5.2; 1261 -5.4; 1387 -6.8; 1526 -8.8; 1678 -9.2; 1846 -8.7; 2031 -8.0; 2234 -8.1; 2457 -7.3; 2703 -4.6; 2973 -3.0; 3270 -5.0; 3597 -5.5; 3957 -6.6; 4353 -9.4; 4788 -10.2; 5267 -3.3; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.5; 8482 -11.7; 9330 -13.1; 10263 -7.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips Fidelio X2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Fidelio X2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.22 | 6.0 dB  |
| Peaking | 69 Hz   |  0.93 | -3.0 dB |
| Peaking | 124 Hz  |  0.16 | -2.8 dB |
| Peaking | 6143 Hz |  4.53 | 7.3 dB  |
| Peaking | 8994 Hz |  4.89 | -8.1 dB |
| Peaking | 1222 Hz |  2.32 | 5.9 dB  |
| Peaking | 1483 Hz |  1.11 | -4.4 dB |
| Peaking | 2934 Hz |  4.16 | 4.8 dB  |
| Peaking | 4697 Hz |  6.14 | -5.8 dB |
| Peaking | 5477 Hz | 10.32 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Fidelio%20X2/Philips%20Fidelio%20X2.png)