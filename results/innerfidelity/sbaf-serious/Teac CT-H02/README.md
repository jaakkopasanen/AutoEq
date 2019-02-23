# Teac CT-H02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.1; 23 -5.3; 25 -5.5; 28 -5.6; 31 -5.8; 34 -5.8; 37 -5.8; 41 -5.8; 45 -5.8; 49 -5.8; 54 -5.9; 60 -6.0; 66 -6.0; 72 -6.2; 79 -6.5; 87 -6.6; 96 -6.7; 106 -7.0; 116 -7.4; 128 -7.2; 141 -6.7; 155 -7.5; 170 -7.2; 187 -7.8; 206 -8.6; 227 -9.0; 249 -8.9; 274 -8.7; 302 -8.9; 332 -8.9; 365 -8.8; 402 -8.8; 442 -8.7; 486 -8.8; 535 -8.8; 588 -8.6; 647 -8.7; 712 -8.3; 783 -7.9; 861 -8.1; 947 -7.6; 1042 -7.6; 1146 -7.8; 1261 -7.6; 1387 -7.6; 1526 -7.6; 1678 -7.7; 1846 -7.1; 2031 -5.9; 2234 -5.0; 2457 -3.0; 2703 -2.0; 2973 -0.8; 3270 -0.7; 3597 -0.6; 3957 -1.2; 4353 -2.1; 4788 -0.5; 5267 -1.8; 5793 -0.6; 6373 -1.0; 7010 -4.4; 7711 -8.8; 8482 -13.0; 9330 -13.7; 10263 -10.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Teac CT-H02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.27 | 1.1 dB   |
| Peaking | 521 Hz   | 0.21 | -2.3 dB  |
| Peaking | 3058 Hz  | 1.96 | 5.0 dB   |
| Peaking | 6171 Hz  | 0.94 | 7.7 dB   |
| Peaking | 8777 Hz  | 2.38 | -12.5 dB |
| Peaking | 177 Hz   | 2.19 | 1.9 dB   |
| Peaking | 202 Hz   | 1.69 | -1.8 dB  |
| Peaking | 971 Hz   | 2.35 | 0.7 dB   |
| Peaking | 1716 Hz  | 5.39 | -1.0 dB  |
| Peaking | 11099 Hz | 9.04 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -0.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)