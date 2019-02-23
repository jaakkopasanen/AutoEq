# Klipsch X20i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -6.8; 25 -6.9; 28 -7.1; 31 -7.2; 34 -7.3; 37 -7.4; 41 -7.5; 45 -7.7; 49 -7.8; 54 -8.0; 60 -8.3; 66 -8.6; 72 -8.9; 79 -9.3; 87 -9.6; 96 -10.0; 106 -10.2; 116 -10.3; 128 -10.6; 141 -10.7; 155 -10.8; 170 -10.8; 187 -10.8; 206 -10.7; 227 -10.5; 249 -10.4; 274 -10.2; 302 -9.9; 332 -9.6; 365 -9.2; 402 -8.9; 442 -8.4; 486 -8.2; 535 -7.7; 588 -7.0; 647 -6.7; 712 -6.4; 783 -6.0; 861 -6.0; 947 -6.1; 1042 -6.3; 1146 -6.4; 1261 -6.6; 1387 -7.0; 1526 -7.5; 1678 -7.7; 1846 -7.7; 2031 -7.6; 2234 -7.8; 2457 -7.4; 2703 -7.1; 2973 -4.9; 3270 -1.2; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -2.5; 5267 -2.5; 5793 -1.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X20i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X20i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 0.64 | -3.9 dB |
| Peaking | 281 Hz  | 1.27 | -2.0 dB |
| Peaking | 2563 Hz | 1.56 | -4.2 dB |
| Peaking | 3645 Hz | 1.69 | 8.1 dB  |
| Peaking | 6191 Hz | 4.72 | 4.5 dB  |
| Peaking | 486 Hz  | 1.67 | -1.1 dB |
| Peaking | 730 Hz  | 0.87 | 1.2 dB  |
| Peaking | 1572 Hz | 3.34 | -1.0 dB |
| Peaking | 8272 Hz | 3.91 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X20i/Klipsch%20X20i.png)