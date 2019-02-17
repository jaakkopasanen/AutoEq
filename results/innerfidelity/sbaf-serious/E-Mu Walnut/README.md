# E-Mu Walnut
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.3; 28 -7.6; 31 -7.8; 34 -8.0; 37 -8.1; 41 -8.3; 45 -8.4; 49 -8.6; 54 -8.7; 60 -8.8; 66 -8.9; 72 -9.0; 79 -9.2; 87 -9.3; 96 -9.4; 106 -9.4; 116 -9.3; 128 -9.5; 141 -9.5; 155 -9.4; 170 -9.1; 187 -8.9; 206 -8.7; 227 -8.3; 249 -8.0; 274 -7.6; 302 -7.0; 332 -6.8; 365 -6.4; 402 -6.0; 442 -5.7; 486 -5.8; 535 -6.0; 588 -5.9; 647 -6.2; 712 -6.6; 783 -6.5; 861 -6.7; 947 -6.6; 1042 -6.3; 1146 -5.6; 1261 -5.5; 1387 -5.7; 1526 -5.8; 1678 -5.9; 1846 -5.2; 2031 -4.0; 2234 -2.8; 2457 -1.7; 2703 -3.0; 2973 -3.5; 3270 -3.7; 3597 -2.5; 3957 -1.2; 4353 -5.0; 4788 -3.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.1; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`E-Mu Walnut GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Walnut ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 0.66 | -2.4 dB |
| Peaking | 157 Hz  | 1.39 | -2.0 dB |
| Peaking | 2450 Hz | 2.52 | 4.3 dB  |
| Peaking | 3775 Hz | 6.21 | 4.1 dB  |
| Peaking | 5773 Hz | 3.23 | 6.6 dB  |
| Peaking | 249 Hz  | 2.07 | -0.8 dB |
| Peaking | 549 Hz  | 0.74 | 1.2 dB  |
| Peaking | 774 Hz  | 1.98 | -1.2 dB |
| Peaking | 6645 Hz | 9.85 | 1.9 dB  |
| Peaking | 8746 Hz | 1.57 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Walnut/E-Mu%20Walnut.png)