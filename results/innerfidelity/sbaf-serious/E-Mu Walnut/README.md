# E-Mu Walnut
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -8.2; 25 -8.5; 28 -8.8; 31 -9.0; 34 -9.2; 37 -9.3; 41 -9.5; 45 -9.6; 49 -9.8; 54 -9.9; 60 -9.9; 66 -10.1; 72 -10.2; 79 -10.4; 87 -10.5; 96 -10.6; 106 -10.6; 116 -10.5; 128 -10.6; 141 -10.6; 155 -10.6; 170 -10.3; 187 -10.1; 206 -9.8; 227 -9.5; 249 -9.2; 274 -8.7; 302 -8.2; 332 -7.9; 365 -7.6; 402 -7.2; 442 -6.9; 486 -7.0; 535 -7.2; 588 -7.1; 647 -7.4; 712 -7.8; 783 -7.7; 861 -7.9; 947 -7.8; 1042 -7.5; 1146 -6.8; 1261 -6.7; 1387 -6.9; 1526 -7.0; 1678 -7.1; 1846 -6.4; 2031 -5.2; 2234 -4.0; 2457 -2.8; 2703 -4.2; 2973 -4.7; 3270 -4.9; 3597 -3.7; 3957 -2.4; 4353 -6.1; 4788 -4.7; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.6; 9330 -8.2; 10263 -8.4; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`E-Mu Walnut GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Walnut ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.69 | -1.8 dB |
| Peaking | 128 Hz  | 0.5  | -3.9 dB |
| Peaking | 2453 Hz | 4.52 | 3.6 dB  |
| Peaking | 3805 Hz | 7.05 | 3.6 dB  |
| Peaking | 5838 Hz | 3.74 | 6.8 dB  |
| Peaking | 428 Hz  | 1.61 | 1.1 dB  |
| Peaking | 695 Hz  | 0.39 | -0.5 dB |
| Peaking | 856 Hz  | 2.56 | -0.9 dB |
| Peaking | 2963 Hz | 3.14 | 0.5 dB  |
| Peaking | 9755 Hz | 4.05 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Walnut/E-Mu%20Walnut.png)