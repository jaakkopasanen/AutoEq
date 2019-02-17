# HiFiMAN HE-5LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -3.3; 25 -4.2; 28 -4.9; 31 -5.1; 34 -4.9; 37 -4.8; 41 -4.6; 45 -4.4; 49 -4.3; 54 -4.0; 60 -4.2; 66 -4.5; 72 -4.5; 79 -4.6; 87 -4.9; 96 -5.2; 106 -5.4; 116 -5.7; 128 -6.4; 141 -7.1; 155 -7.9; 170 -8.2; 187 -8.5; 206 -8.6; 227 -8.6; 249 -8.8; 274 -8.9; 302 -8.9; 332 -8.9; 365 -8.9; 402 -8.8; 442 -8.7; 486 -8.7; 535 -8.8; 588 -8.7; 647 -6.9; 712 -5.5; 783 -4.3; 861 -4.9; 947 -5.7; 1042 -5.9; 1146 -4.9; 1261 -4.0; 1387 -3.1; 1526 -2.2; 1678 -1.8; 1846 -0.5; 2031 -1.8; 2234 -3.0; 2457 -1.6; 2703 -2.4; 2973 -3.0; 3270 -3.6; 3597 -3.4; 3957 -5.0; 4353 -6.4; 4788 -9.1; 5267 -5.5; 5793 -7.6; 6373 -9.5; 7010 -9.1; 7711 -9.4; 8482 -12.1; 9330 -13.2; 10263 -9.6; 11289 -6.0; 12418 -5.9; 13660 -6.5; 15026 -6.9; 16529 -6.9; 18182 -7.5; 20000 -8.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 17 Hz    |  0.08 | 2.1 dB  |
| Peaking | 271 Hz   |  0.6  | -4.2 dB |
| Peaking | 1752 Hz  |  1.5  | 4.6 dB  |
| Peaking | 2820 Hz  |  2.5  | 2.4 dB  |
| Peaking | 8748 Hz  |  1.97 | -7.0 dB |
| Peaking | 32 Hz    |  3.4  | -1.3 dB |
| Peaking | 561 Hz   |  4.63 | -1.6 dB |
| Peaking | 772 Hz   |  5.84 | 2.4 dB  |
| Peaking | 6242 Hz  | 10.24 | -2.6 dB |
| Peaking | 11501 Hz |  5.7  | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.9 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)