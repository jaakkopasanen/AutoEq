# Monster DNA Pro2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -2.6; 25 -3.7; 28 -5.1; 31 -6.2; 34 -7.0; 37 -7.6; 41 -8.0; 45 -8.3; 49 -8.3; 54 -8.3; 60 -8.2; 66 -8.2; 72 -8.2; 79 -8.2; 87 -8.2; 96 -8.1; 106 -8.2; 116 -8.3; 128 -8.6; 141 -8.7; 155 -8.8; 170 -8.4; 187 -8.5; 206 -8.5; 227 -8.2; 249 -8.2; 274 -7.5; 302 -6.7; 332 -5.8; 365 -5.0; 402 -3.8; 442 -5.5; 486 -7.1; 535 -7.6; 588 -7.7; 647 -7.9; 712 -8.1; 783 -7.9; 861 -7.9; 947 -7.5; 1042 -6.4; 1146 -5.1; 1261 -4.1; 1387 -3.8; 1526 -4.1; 1678 -5.2; 1846 -6.7; 2031 -8.3; 2234 -10.4; 2457 -11.8; 2703 -11.3; 2973 -9.4; 3270 -7.4; 3597 -6.1; 3957 -10.0; 4353 -9.8; 4788 -7.1; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster DNA Pro2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster DNA Pro2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 3.87 | 5.2 dB  |
| Peaking | 1432 Hz | 3.67 | 3.6 dB  |
| Peaking | 2487 Hz | 3.1  | -6.0 dB |
| Peaking | 4323 Hz | 5.25 | -5.4 dB |
| Peaking | 5799 Hz | 3.13 | 7.3 dB  |
| Peaking | 22 Hz   | 1.84 | 3.0 dB  |
| Peaking | 98 Hz   | 0.24 | -2.2 dB |
| Peaking | 386 Hz  | 3.46 | 4.0 dB  |
| Peaking | 679 Hz  | 2.02 | -1.5 dB |
| Peaking | 8116 Hz | 5.44 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.1 dB |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20DNA%20Pro2/Monster%20DNA%20Pro2.png)