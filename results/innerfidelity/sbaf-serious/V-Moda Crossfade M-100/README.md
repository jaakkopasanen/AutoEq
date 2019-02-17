# V-Moda Crossfade M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.4; 28 -10.5; 31 -10.6; 34 -10.7; 37 -10.8; 41 -10.8; 45 -10.9; 49 -11.0; 54 -11.2; 60 -11.4; 66 -11.4; 72 -11.4; 79 -11.7; 87 -11.7; 96 -11.5; 106 -11.6; 116 -12.2; 128 -12.8; 141 -12.8; 155 -12.3; 170 -11.2; 187 -11.2; 206 -10.1; 227 -8.8; 249 -7.4; 274 -6.1; 302 -5.8; 332 -4.4; 365 -3.0; 402 -2.2; 442 -1.9; 486 -2.5; 535 -3.0; 588 -3.2; 647 -4.0; 712 -4.8; 783 -5.2; 861 -5.9; 947 -6.3; 1042 -6.6; 1146 -6.7; 1261 -6.8; 1387 -7.0; 1526 -7.3; 1678 -7.4; 1846 -7.1; 2031 -7.1; 2234 -7.0; 2457 -6.5; 2703 -6.4; 2973 -5.6; 3270 -5.4; 3597 -5.6; 3957 -5.2; 4353 -4.2; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.6; 9330 -10.3; 10263 -10.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 23 Hz   |  0.71 | -2.8 dB |
| Peaking | 64 Hz   |  0.69 | -3.4 dB |
| Peaking | 150 Hz  |  1.12 | -5.1 dB |
| Peaking | 431 Hz  |  1.45 | 5.5 dB  |
| Peaking | 5470 Hz |  2.8  | 7.1 dB  |
| Peaking | 270 Hz  | 11.13 | 0.6 dB  |
| Peaking | 627 Hz  |  5.25 | 0.9 dB  |
| Peaking | 1619 Hz |  1.32 | -1.2 dB |
| Peaking | 8129 Hz |  0.7  | 1.0 dB  |
| Peaking | 9707 Hz |  3.71 | -6.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20M-100/V-Moda%20Crossfade%20M-100.png)