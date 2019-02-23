# Denon AH-C551
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -7.3; 25 -7.6; 28 -8.0; 31 -8.3; 34 -8.5; 37 -8.7; 41 -9.0; 45 -9.2; 49 -9.4; 54 -9.5; 60 -9.8; 66 -10.0; 72 -10.3; 79 -10.5; 87 -10.7; 96 -10.9; 106 -10.9; 116 -10.9; 128 -10.8; 141 -10.7; 155 -10.5; 170 -10.2; 187 -9.8; 206 -9.4; 227 -8.9; 249 -8.3; 274 -7.7; 302 -7.0; 332 -6.4; 365 -5.6; 402 -4.8; 442 -4.0; 486 -3.3; 535 -2.6; 588 -1.7; 647 -1.2; 712 -0.9; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.4; 1146 -1.9; 1261 -2.6; 1387 -3.2; 1526 -4.3; 1678 -5.3; 1846 -5.9; 2031 -6.5; 2234 -7.5; 2457 -8.9; 2703 -10.6; 2973 -10.9; 3270 -7.6; 3597 -5.3; 3957 -5.2; 4353 -7.4; 4788 -9.3; 5267 -11.4; 5793 -12.1; 6373 -8.6; 7010 -6.1; 7711 -6.2; 8482 -7.5; 9330 -8.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C551 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 69 Hz   |  0.51 | -2.5 dB |
| Peaking | 154 Hz  |  0.65 | -3.2 dB |
| Peaking | 775 Hz  |  0.8  | 6.5 dB  |
| Peaking | 2733 Hz |  3.82 | -5.5 dB |
| Peaking | 5538 Hz |  4.89 | -6.5 dB |
| Peaking | 1937 Hz |  4.02 | -0.8 dB |
| Peaking | 3059 Hz | 11.88 | -1.7 dB |
| Peaking | 3709 Hz |  6.1  | 2.6 dB  |
| Peaking | 7246 Hz |  7.93 | 1.7 dB  |
| Peaking | 9009 Hz |  7.56 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C551/Denon%20AH-C551.png)