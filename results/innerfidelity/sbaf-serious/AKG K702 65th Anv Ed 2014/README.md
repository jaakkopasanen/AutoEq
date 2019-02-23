# AKG K702 65th Anv Ed 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.4; 23 -1.9; 25 -2.4; 28 -3.0; 31 -3.5; 34 -3.9; 37 -4.2; 41 -4.6; 45 -4.9; 49 -5.2; 54 -5.5; 60 -5.9; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.2; 96 -7.6; 106 -7.8; 116 -8.0; 128 -8.1; 141 -8.3; 155 -8.8; 170 -8.6; 187 -8.5; 206 -8.8; 227 -8.9; 249 -9.0; 274 -9.0; 302 -8.9; 332 -8.8; 365 -8.6; 402 -8.5; 442 -8.0; 486 -7.8; 535 -7.4; 588 -6.7; 647 -6.4; 712 -5.8; 783 -5.0; 861 -4.7; 947 -4.4; 1042 -4.3; 1146 -4.0; 1261 -3.7; 1387 -4.6; 1526 -6.4; 1678 -7.7; 1846 -8.4; 2031 -8.6; 2234 -7.4; 2457 -4.3; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.7; 3957 -2.8; 4353 -5.4; 4788 -5.2; 5267 -4.9; 5793 -7.2; 6373 -8.3; 7010 -9.8; 7711 -9.2; 8482 -8.6; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.8; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 65th Anv Ed 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 65th Anv Ed 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.49 | 6.1 dB  |
| Peaking | 733 Hz   | 0.17 | -3.6 dB |
| Peaking | 949 Hz   | 1.06 | 5.9 dB  |
| Peaking | 3243 Hz  | 2.09 | 8.9 dB  |
| Peaking | 7278 Hz  | 3.62 | -3.3 dB |
| Peaking | 1325 Hz  | 4.33 | 2.4 dB  |
| Peaking | 2097 Hz  | 1.62 | -2.8 dB |
| Peaking | 2640 Hz  | 5    | 3.6 dB  |
| Peaking | 5198 Hz  | 8.57 | 1.9 dB  |
| Peaking | 18428 Hz | 2.24 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702%2065th%20Anv%20Ed%202014/AKG%20K702%2065th%20Anv%20Ed%202014.png)