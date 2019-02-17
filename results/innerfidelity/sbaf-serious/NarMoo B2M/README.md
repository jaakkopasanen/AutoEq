# NarMoo B2M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.8; 28 -13.7; 31 -13.5; 34 -13.3; 37 -13.2; 41 -13.0; 45 -12.8; 49 -12.7; 54 -12.5; 60 -12.3; 66 -12.2; 72 -12.1; 79 -12.1; 87 -12.1; 96 -12.0; 106 -11.8; 116 -11.7; 128 -11.5; 141 -11.4; 155 -11.3; 170 -11.0; 187 -10.8; 206 -10.5; 227 -10.2; 249 -10.0; 274 -9.7; 302 -9.4; 332 -9.0; 365 -8.7; 402 -8.5; 442 -8.0; 486 -7.9; 535 -7.6; 588 -7.0; 647 -6.8; 712 -6.7; 783 -6.3; 861 -6.2; 947 -6.4; 1042 -6.7; 1146 -6.7; 1261 -6.8; 1387 -7.3; 1526 -7.6; 1678 -7.8; 1846 -6.3; 2031 -6.1; 2234 -6.1; 2457 -5.6; 2703 -4.8; 2973 -2.8; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -4.3; 5267 -1.9; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NarMoo B2M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo B2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.31 | -7.1 dB |
| Peaking | 147 Hz  | 0.49 | -3.8 dB |
| Peaking | 3592 Hz | 2.66 | 6.4 dB  |
| Peaking | 6083 Hz | 2.9  | 6.4 dB  |
| Peaking | 7715 Hz | 2.05 | -1.6 dB |
| Peaking | 798 Hz  | 2.89 | 0.8 dB  |
| Peaking | 1599 Hz | 4.76 | -1.6 dB |
| Peaking | 3073 Hz | 2.9  | -0.7 dB |
| Peaking | 3131 Hz | 8.06 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20B2M/NarMoo%20B2M.png)