# Sony WI-1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.2; 25 -8.4; 28 -8.5; 31 -8.6; 34 -8.6; 37 -8.6; 41 -8.5; 45 -8.5; 49 -8.5; 54 -8.5; 60 -8.5; 66 -8.6; 72 -8.7; 79 -8.8; 87 -9.0; 96 -9.0; 106 -8.9; 116 -8.8; 128 -9.4; 141 -9.9; 155 -9.9; 170 -9.7; 187 -9.4; 206 -9.1; 227 -8.8; 249 -8.5; 274 -8.3; 302 -8.0; 332 -7.7; 365 -7.3; 402 -6.8; 442 -6.4; 486 -6.0; 535 -5.7; 588 -5.5; 647 -4.8; 712 -4.0; 783 -3.2; 861 -2.8; 947 -3.2; 1042 -2.8; 1146 -2.2; 1261 -1.5; 1387 -1.1; 1526 -0.8; 1678 -0.5; 1846 -0.6; 2031 -1.2; 2234 -2.1; 2457 -3.6; 2703 -4.2; 2973 -3.7; 3270 -3.9; 3597 -4.8; 3957 -5.1; 4353 -3.6; 4788 -3.8; 5267 -5.9; 5793 -6.1; 6373 -4.7; 7010 -7.1; 7711 -10.7; 8482 -11.2; 9330 -8.4; 10263 -7.0; 11289 -8.2; 12418 -8.5; 13660 -7.9; 15026 -8.4; 16529 -6.9; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 30 Hz    |  0.43 | -2.5 dB |
| Peaking | 174 Hz   |  0.61 | -3.6 dB |
| Peaking | 1524 Hz  |  0.78 | 5.0 dB  |
| Peaking | 8118 Hz  |  4.52 | -6.0 dB |
| Peaking | 13631 Hz |  1.13 | -2.8 dB |
| Peaking | 1138 Hz  |  5.1  | -0.6 dB |
| Peaking | 2094 Hz  |  2.48 | 1.5 dB  |
| Peaking | 2458 Hz  |  2.75 | -1.8 dB |
| Peaking | 4578 Hz  | 10.25 | 2.0 dB  |
| Peaking | 6494 Hz  | 11.94 | 2.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20WI-1000X/Sony%20WI-1000X.png)