# AKG K619
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.1; 25 -11.2; 28 -11.3; 31 -11.4; 34 -11.4; 37 -11.4; 41 -11.4; 45 -11.3; 49 -11.2; 54 -10.9; 60 -10.6; 66 -10.1; 72 -9.4; 79 -8.5; 87 -7.3; 96 -7.2; 106 -7.2; 116 -6.1; 128 -4.9; 141 -4.6; 155 -3.7; 170 -2.9; 187 -2.9; 206 -2.7; 227 -2.7; 249 -2.8; 274 -2.8; 302 -3.2; 332 -3.7; 365 -4.2; 402 -4.7; 442 -4.9; 486 -5.4; 535 -5.5; 588 -5.4; 647 -5.6; 712 -5.9; 783 -5.9; 861 -6.2; 947 -6.4; 1042 -6.4; 1146 -6.4; 1261 -5.9; 1387 -6.1; 1526 -6.0; 1678 -5.7; 1846 -4.7; 2031 -3.7; 2234 -2.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K619 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K619 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.47 | -5.4 dB |
| Peaking | 207 Hz  | 0.96 | 5.8 dB  |
| Peaking | 215 Hz  | 2.86 | -1.4 dB |
| Peaking | 2891 Hz | 1.6  | 5.8 dB  |
| Peaking | 5232 Hz | 1.86 | 5.6 dB  |
| Peaking | 1475 Hz | 1.41 | -0.7 dB |
| Peaking | 2326 Hz | 7.39 | 1.6 dB  |
| Peaking | 6462 Hz | 5.45 | 2.7 dB  |
| Peaking | 6748 Hz | 3.19 | 0.3 dB  |
| Peaking | 7602 Hz | 1.94 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K619/AKG%20K619.png)