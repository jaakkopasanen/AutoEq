# Audeze LCD-3 sn2717210
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.8; 31 -3.1; 34 -3.9; 37 -4.2; 41 -4.5; 45 -4.4; 49 -4.3; 54 -4.4; 60 -4.4; 66 -4.5; 72 -4.7; 79 -5.0; 87 -5.3; 96 -5.8; 106 -6.0; 116 -6.1; 128 -6.4; 141 -6.7; 155 -6.9; 170 -7.1; 187 -7.2; 206 -7.3; 227 -7.3; 249 -7.4; 274 -7.4; 302 -7.4; 332 -7.5; 365 -7.4; 402 -7.5; 442 -7.4; 486 -7.4; 535 -7.1; 588 -6.2; 647 -5.7; 712 -6.5; 783 -6.9; 861 -7.0; 947 -6.7; 1042 -6.3; 1146 -6.0; 1261 -5.6; 1387 -6.7; 1526 -8.1; 1678 -8.1; 1846 -7.0; 2031 -6.1; 2234 -6.1; 2457 -4.7; 2703 -3.5; 2973 -2.9; 3270 -2.5; 3597 -1.0; 3957 -0.5; 4353 -1.2; 4788 -3.2; 5267 -3.9; 5793 -7.4; 6373 -3.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -8.9; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2717210 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2717210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  1.4  | 6.1 dB  |
| Peaking | 62 Hz    |  2.08 | 1.7 dB  |
| Peaking | 1630 Hz  |  5.13 | -2.3 dB |
| Peaking | 2794 Hz  |  4.58 | 1.5 dB  |
| Peaking | 3934 Hz  |  2.06 | 6.1 dB  |
| Peaking | 292 Hz   |  1.01 | -1.1 dB |
| Peaking | 1268 Hz  |  5.05 | 1.8 dB  |
| Peaking | 1362 Hz  |  3.03 | -0.8 dB |
| Peaking | 6694 Hz  | 13.28 | 3.6 dB  |
| Peaking | 19642 Hz |  1.11 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.1 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2717210/Audeze%20LCD-3%20sn2717210.png)