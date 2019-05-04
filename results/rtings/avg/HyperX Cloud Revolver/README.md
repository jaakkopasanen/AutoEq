# HyperX Cloud Revolver
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.5; 28 -6.7; 31 -6.8; 34 -6.9; 37 -6.9; 41 -7.0; 45 -7.2; 49 -7.4; 54 -7.7; 60 -8.1; 66 -8.5; 72 -8.7; 79 -8.9; 87 -9.0; 96 -9.1; 106 -9.1; 116 -9.2; 128 -9.1; 141 -9.0; 155 -8.7; 170 -8.5; 187 -8.1; 206 -7.6; 227 -7.1; 249 -6.6; 274 -6.3; 302 -6.1; 332 -5.5; 365 -5.1; 402 -5.2; 442 -5.3; 486 -5.0; 535 -4.6; 588 -4.4; 647 -4.4; 712 -4.5; 783 -4.2; 861 -4.4; 947 -5.0; 1042 -5.6; 1146 -6.1; 1261 -6.6; 1387 -7.3; 1526 -8.5; 1678 -10.2; 1846 -10.9; 2031 -10.8; 2234 -9.8; 2457 -8.3; 2703 -7.3; 2973 -6.5; 3270 -4.1; 3597 -1.4; 3957 -0.5; 4353 -1.5; 4788 -3.1; 5267 -3.6; 5793 -2.7; 6373 -1.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.5; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -7.8; 18182 -9.9; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HyperX Cloud Revolver GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HyperX Cloud Revolver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 101 Hz   | 0.89 | -3.6 dB |
| Peaking | 1978 Hz  | 2.42 | -5.8 dB |
| Peaking | 3952 Hz  | 3    | 6.1 dB  |
| Peaking | 6339 Hz  | 4.44 | 4.3 dB  |
| Peaking | 18417 Hz | 1.36 | -4.3 dB |
| Peaking | 177 Hz   | 2.85 | -0.9 dB |
| Peaking | 362 Hz   | 3.42 | 0.9 dB  |
| Peaking | 708 Hz   | 1.29 | 2.0 dB  |
| Peaking | 1637 Hz  | 5.03 | -1.2 dB |
| Peaking | 8755 Hz  | 4.14 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/HyperX%20Cloud%20Revolver/HyperX%20Cloud%20Revolver.png)