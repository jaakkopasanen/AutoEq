# Audeze LCD-3 sn2717210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.2; 28 -2.5; 31 -4.0; 34 -4.8; 37 -5.2; 41 -5.4; 45 -5.3; 49 -5.3; 54 -5.4; 60 -5.3; 66 -5.5; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.8; 106 -6.9; 116 -7.1; 128 -7.4; 141 -7.6; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.3; 227 -8.2; 249 -8.4; 274 -8.4; 302 -8.4; 332 -8.5; 365 -8.4; 402 -8.4; 442 -8.3; 486 -8.3; 535 -8.0; 588 -7.1; 647 -6.7; 712 -7.5; 783 -7.8; 861 -7.9; 947 -7.7; 1042 -7.3; 1146 -6.9; 1261 -6.5; 1387 -7.7; 1526 -9.1; 1678 -9.1; 1846 -7.9; 2031 -7.0; 2234 -7.0; 2457 -5.7; 2703 -4.5; 2973 -3.8; 3270 -3.4; 3597 -1.9; 3957 -1.4; 4353 -2.2; 4788 -4.1; 5267 -4.8; 5793 -8.3; 6373 -4.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -7.7; 18182 -9.8; 20000 -11.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2717210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2717210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 16 Hz    |  0.83 | 7.7 dB  |
| Peaking | 297 Hz   |  0.57 | -2.1 dB |
| Peaking | 1645 Hz  |  3.48 | -2.8 dB |
| Peaking | 2856 Hz  |  4.33 | 1.4 dB  |
| Peaking | 3929 Hz  |  2.64 | 5.3 dB  |
| Peaking | 68 Hz    |  3.86 | 0.7 dB  |
| Peaking | 635 Hz   |  7.88 | 1.1 dB  |
| Peaking | 846 Hz   |  4.88 | -0.9 dB |
| Peaking | 6795 Hz  | 12.59 | 3.5 dB  |
| Peaking | 19443 Hz |  0.96 | -5.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.6 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2717210/Audeze%20LCD-3%20sn2717210.png)