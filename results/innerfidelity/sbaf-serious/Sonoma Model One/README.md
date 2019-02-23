# Sonoma Model One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -3.9; 25 -4.0; 28 -4.0; 31 -4.0; 34 -3.9; 37 -3.9; 41 -3.9; 45 -3.8; 49 -3.6; 54 -3.4; 60 -3.2; 66 -3.8; 72 -5.3; 79 -5.8; 87 -5.4; 96 -5.1; 106 -5.0; 116 -5.0; 128 -4.9; 141 -4.8; 155 -4.7; 170 -4.7; 187 -4.8; 206 -4.8; 227 -4.7; 249 -4.7; 274 -4.7; 302 -4.7; 332 -4.8; 365 -4.8; 402 -4.8; 442 -4.8; 486 -5.4; 535 -5.2; 588 -4.7; 647 -5.6; 712 -6.5; 783 -6.1; 861 -6.1; 947 -5.5; 1042 -5.0; 1146 -6.5; 1261 -7.7; 1387 -7.6; 1526 -8.8; 1678 -7.4; 1846 -6.6; 2031 -6.0; 2234 -6.8; 2457 -5.6; 2703 -7.2; 2973 -6.0; 3270 -6.9; 3597 -6.1; 3957 -5.1; 4353 -5.3; 4788 -5.2; 5267 -6.4; 5793 -0.5; 6373 -3.6; 7010 -4.4; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sonoma Model One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sonoma Model One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.05 | 1.0 dB  |
| Peaking | 1437 Hz |  2.28 | -1.8 dB |
| Peaking | 1539 Hz |  4.92 | -1.6 dB |
| Peaking | 2916 Hz |  2.28 | -1.1 dB |
| Peaking | 5953 Hz | 10.61 | 6.4 dB  |
| Peaking | 62 Hz   |  1.83 | 2.8 dB  |
| Peaking | 76 Hz   |  2.03 | -3.0 dB |
| Peaking | 431 Hz  |  1.15 | 0.4 dB  |
| Peaking | 744 Hz  |  3.96 | -1.1 dB |
| Peaking | 1027 Hz |  9.66 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB  |
| Peaking | 62 Hz    | 1.41 | 0.9 dB  |
| Peaking | 125 Hz   | 1.41 | 0.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sonoma%20Model%20One/Sonoma%20Model%20One.png)