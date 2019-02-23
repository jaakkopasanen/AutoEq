# V-Moda Crossfade M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -11.0; 25 -11.2; 28 -11.3; 31 -11.4; 34 -11.4; 37 -11.5; 41 -11.6; 45 -11.7; 49 -11.8; 54 -12.0; 60 -12.1; 66 -12.2; 72 -12.2; 79 -12.4; 87 -12.5; 96 -12.2; 106 -12.3; 116 -13.0; 128 -13.5; 141 -13.6; 155 -13.0; 170 -12.0; 187 -11.9; 206 -10.8; 227 -9.6; 249 -8.2; 274 -6.9; 302 -6.6; 332 -5.2; 365 -3.8; 402 -3.0; 442 -2.7; 486 -3.2; 535 -3.7; 588 -4.0; 647 -4.7; 712 -5.6; 783 -6.0; 861 -6.6; 947 -7.1; 1042 -7.3; 1146 -7.5; 1261 -7.6; 1387 -7.8; 1526 -8.1; 1678 -8.2; 1846 -7.9; 2031 -7.8; 2234 -7.8; 2457 -7.2; 2703 -7.2; 2973 -6.3; 3270 -6.2; 3597 -6.3; 3957 -6.0; 4353 -5.0; 4788 -1.1; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -11.1; 10263 -11.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-Moda Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 32 Hz   |  0.63 | -4.7 dB |
| Peaking | 82 Hz   |  1.27 | -3.8 dB |
| Peaking | 148 Hz  |  2    | -5.9 dB |
| Peaking | 5674 Hz |  2.59 | 7.1 dB  |
| Peaking | 9723 Hz |  4.31 | -6.4 dB |
| Peaking | 213 Hz  |  3.1  | -2.2 dB |
| Peaking | 452 Hz  |  1.36 | 4.5 dB  |
| Peaking | 1503 Hz |  0.67 | -1.5 dB |
| Peaking | 1748 Hz |  2.02 | -0.4 dB |
| Peaking | 4884 Hz | 12.21 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 4.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20M-100/V-Moda%20Crossfade%20M-100.png)