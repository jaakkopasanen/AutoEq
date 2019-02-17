# V-MODA Crossfade M-100
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.6; 25 -7.7; 28 -8.0; 31 -8.1; 34 -8.1; 37 -8.1; 41 -8.1; 45 -8.1; 49 -8.2; 54 -8.2; 60 -8.3; 66 -8.5; 72 -8.7; 79 -9.0; 87 -9.2; 96 -9.5; 106 -9.9; 116 -10.2; 128 -10.5; 141 -10.6; 155 -10.7; 170 -10.4; 187 -10.0; 206 -9.3; 227 -8.3; 249 -7.2; 274 -6.3; 302 -4.7; 332 -2.2; 365 -2.2; 402 -2.0; 442 -2.2; 486 -2.0; 535 -1.8; 588 -2.1; 647 -2.8; 712 -3.7; 783 -4.6; 861 -5.4; 947 -6.1; 1042 -6.7; 1146 -7.1; 1261 -7.4; 1387 -7.6; 1526 -7.6; 1678 -7.8; 1846 -8.3; 2031 -8.6; 2234 -8.1; 2457 -7.3; 2703 -6.7; 2973 -7.8; 3270 -7.5; 3597 -6.3; 3957 -4.3; 4353 -1.8; 4788 -0.9; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -6.8; 11289 -6.8; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA Crossfade M-100 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA Crossfade M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 47 Hz   |  0.21 | -1.2 dB |
| Peaking | 183 Hz  |  0.75 | -6.1 dB |
| Peaking | 422 Hz  |  0.65 | 8.4 dB  |
| Peaking | 2631 Hz |  0.23 | -3.4 dB |
| Peaking | 5299 Hz |  1.47 | 9.6 dB  |
| Peaking | 337 Hz  | 12.26 | 1.3 dB  |
| Peaking | 2642 Hz |  5.21 | 2.8 dB  |
| Peaking | 2852 Hz |  2.22 | -2.0 dB |
| Peaking | 8193 Hz |  0.49 | 0.9 dB  |
| Peaking | 8448 Hz |  2.18 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.5 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20Crossfade%20M-100/V-MODA%20Crossfade%20M-100.png)