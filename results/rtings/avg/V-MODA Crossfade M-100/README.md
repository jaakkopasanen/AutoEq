# V-MODA Crossfade M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.3; 25 -8.5; 28 -8.7; 31 -8.8; 34 -8.8; 37 -8.9; 41 -8.9; 45 -8.9; 49 -8.9; 54 -9.0; 60 -9.1; 66 -9.3; 72 -9.4; 79 -9.6; 87 -9.9; 96 -10.2; 106 -10.5; 116 -10.9; 128 -11.2; 141 -11.4; 155 -11.4; 170 -11.2; 187 -10.7; 206 -10.1; 227 -9.1; 249 -8.1; 274 -7.1; 302 -5.6; 332 -3.2; 365 -3.0; 402 -2.9; 442 -3.1; 486 -2.9; 535 -2.8; 588 -3.1; 647 -3.8; 712 -4.7; 783 -5.6; 861 -6.4; 947 -7.1; 1042 -7.8; 1146 -8.2; 1261 -8.5; 1387 -8.7; 1526 -8.8; 1678 -9.0; 1846 -9.6; 2031 -9.9; 2234 -9.9; 2457 -9.0; 2703 -8.2; 2973 -8.8; 3270 -8.1; 3597 -7.0; 3957 -4.7; 4353 -2.5; 4788 -1.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.2; 11289 -8.7; 12418 -6.6; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 47 Hz    |  0.18 | -1.9 dB |
| Peaking | 189 Hz   |  0.74 | -6.3 dB |
| Peaking | 407 Hz   |  0.66 | 7.8 dB  |
| Peaking | 3082 Hz  |  0.26 | -5.3 dB |
| Peaking | 5349 Hz  |  1.31 | 11.3 dB |
| Peaking | 185 Hz   |  3.88 | 0.1 dB  |
| Peaking | 625 Hz   |  4.92 | 0.6 dB  |
| Peaking | 4195 Hz  | 11.51 | 1.1 dB  |
| Peaking | 14364 Hz |  3.05 | 0.8 dB  |
| Peaking | 22048 Hz |  1.83 | -0.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 5.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -4.8 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20M-100/V-MODA%20Crossfade%20M-100.png)