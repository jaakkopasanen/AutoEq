# Custom Art Pro330v2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.2; 25 -3.5; 28 -3.9; 31 -4.3; 34 -4.5; 37 -4.8; 41 -5.1; 45 -5.3; 49 -5.5; 54 -5.7; 60 -6.1; 66 -6.4; 72 -6.8; 79 -7.2; 87 -7.7; 96 -8.2; 106 -8.7; 116 -9.1; 128 -9.4; 141 -9.8; 155 -10.1; 170 -10.4; 187 -10.6; 206 -10.7; 227 -10.8; 249 -10.9; 274 -10.9; 302 -10.9; 332 -10.9; 365 -10.7; 402 -10.6; 442 -10.3; 486 -10.1; 535 -9.7; 588 -9.1; 647 -8.5; 712 -7.6; 783 -6.6; 861 -5.6; 947 -4.8; 1042 -4.2; 1146 -4.0; 1261 -3.9; 1387 -4.0; 1526 -5.0; 1678 -6.8; 1846 -6.2; 2031 -3.8; 2234 -2.2; 2457 -1.5; 2703 -1.8; 2973 -3.0; 3270 -4.5; 3597 -5.2; 3957 -3.8; 4353 -3.4; 4788 -3.6; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.4; 8482 -7.6; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art Pro330v2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art Pro330v2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 13 Hz   |  0.17 | 3.5 dB  |
| Peaking | 294 Hz  |  0.27 | -4.9 dB |
| Peaking | 1047 Hz |  1.36 | 5.1 dB  |
| Peaking | 2519 Hz |  2.58 | 5.3 dB  |
| Peaking | 5787 Hz |  2.93 | 6.3 dB  |
| Peaking | 1656 Hz |  2.46 | 1.7 dB  |
| Peaking | 1727 Hz |  5.67 | -3.8 dB |
| Peaking | 4197 Hz | 10.18 | 1.8 dB  |
| Peaking | 6641 Hz |  9.4  | 1.6 dB  |
| Peaking | 8186 Hz |  4.3  | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.7 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Custom%20Art%20Pro330v2/Custom%20Art%20Pro330v2.png)