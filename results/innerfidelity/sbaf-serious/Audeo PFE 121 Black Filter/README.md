# Audeo PFE 121 Black Filter
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.3; 28 -6.4; 31 -6.6; 34 -6.7; 37 -6.8; 41 -7.0; 45 -7.1; 49 -7.3; 54 -7.6; 60 -7.9; 66 -8.2; 72 -8.5; 79 -8.9; 87 -9.3; 96 -9.6; 106 -9.9; 116 -10.1; 128 -10.3; 141 -10.6; 155 -10.6; 170 -10.7; 187 -10.7; 206 -10.6; 227 -10.5; 249 -10.4; 274 -10.1; 302 -9.9; 332 -9.6; 365 -9.3; 402 -9.0; 442 -8.5; 486 -8.3; 535 -7.9; 588 -7.1; 647 -6.8; 712 -6.6; 783 -6.2; 861 -6.2; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -6.8; 1526 -7.1; 1678 -7.0; 1846 -6.2; 2031 -5.5; 2234 -4.3; 2457 -3.0; 2703 -3.5; 2973 -3.1; 3270 -2.2; 3597 -1.3; 3957 -1.0; 4353 -1.5; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -7.4; 8482 -10.7; 9330 -10.1; 10263 -8.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeo PFE 121 Black Filter GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 129 Hz  | 0.76 | -3.2 dB |
| Peaking | 274 Hz  | 0.91 | -2.6 dB |
| Peaking | 3539 Hz | 1.42 | 3.8 dB  |
| Peaking | 6030 Hz | 1.47 | 6.4 dB  |
| Peaking | 8588 Hz | 2.44 | -7.2 dB |
| Peaking | 19 Hz   | 1.16 | 0.5 dB  |
| Peaking | 791 Hz  | 3.34 | 0.8 dB  |
| Peaking | 1623 Hz | 2.6  | -1.2 dB |
| Peaking | 2395 Hz | 7.02 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Black%20Filter/Audeo%20PFE%20121%20Black%20Filter.png)