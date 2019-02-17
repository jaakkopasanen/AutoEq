# Monster DNA Pro2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -2.1; 25 -3.3; 28 -4.7; 31 -5.8; 34 -6.6; 37 -7.2; 41 -7.6; 45 -7.8; 49 -7.9; 54 -7.8; 60 -7.8; 66 -7.8; 72 -7.8; 79 -7.8; 87 -7.7; 96 -7.7; 106 -7.7; 116 -7.8; 128 -8.1; 141 -8.3; 155 -8.4; 170 -7.9; 187 -8.1; 206 -8.1; 227 -7.8; 249 -7.7; 274 -7.1; 302 -6.3; 332 -5.3; 365 -4.6; 402 -3.3; 442 -5.0; 486 -6.7; 535 -7.2; 588 -7.3; 647 -7.5; 712 -7.7; 783 -7.4; 861 -7.4; 947 -7.0; 1042 -5.9; 1146 -4.7; 1261 -3.7; 1387 -3.3; 1526 -3.6; 1678 -4.8; 1846 -6.2; 2031 -7.8; 2234 -10.0; 2457 -11.4; 2703 -10.8; 2973 -8.9; 3270 -7.0; 3597 -5.7; 3957 -9.6; 4353 -9.4; 4788 -6.7; 5267 -1.1; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster DNA Pro2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster DNA Pro2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 3.64 | 6.1 dB  |
| Peaking | 1426 Hz | 3.17 | 3.9 dB  |
| Peaking | 2486 Hz | 3.33 | -5.7 dB |
| Peaking | 4298 Hz | 5.66 | -5.1 dB |
| Peaking | 5782 Hz | 3.08 | 7.2 dB  |
| Peaking | 168 Hz  | 0.24 | -1.7 dB |
| Peaking | 386 Hz  | 2.81 | 4.5 dB  |
| Peaking | 855 Hz  | 1.23 | -1.7 dB |
| Peaking | 1136 Hz | 1.5  | 1.7 dB  |
| Peaking | 8147 Hz | 5.36 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 0.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20DNA%20Pro2/Monster%20DNA%20Pro2.png)