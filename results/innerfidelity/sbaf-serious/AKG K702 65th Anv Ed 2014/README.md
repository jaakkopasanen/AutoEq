# AKG K702 65th Anv Ed 2014
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.5; 23 -3.1; 25 -3.6; 28 -4.1; 31 -4.6; 34 -5.0; 37 -5.4; 41 -5.7; 45 -6.1; 49 -6.3; 54 -6.6; 60 -7.0; 66 -7.3; 72 -7.7; 79 -7.9; 87 -8.4; 96 -8.7; 106 -9.0; 116 -9.1; 128 -9.2; 141 -9.4; 155 -9.9; 170 -9.8; 187 -9.7; 206 -9.9; 227 -10.1; 249 -10.2; 274 -10.1; 302 -10.1; 332 -9.9; 365 -9.7; 402 -9.6; 442 -9.2; 486 -8.9; 535 -8.5; 588 -7.9; 647 -7.6; 712 -6.9; 783 -6.1; 861 -5.9; 947 -5.6; 1042 -5.4; 1146 -5.1; 1261 -4.9; 1387 -5.8; 1526 -7.5; 1678 -8.8; 1846 -9.5; 2031 -9.7; 2234 -8.5; 2457 -5.5; 2703 -2.4; 2973 -0.6; 3270 -0.5; 3597 -1.6; 3957 -4.0; 4353 -6.5; 4788 -6.3; 5267 -6.1; 5793 -8.4; 6373 -9.5; 7010 -10.9; 7711 -10.3; 8482 -9.7; 9330 -7.2; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -7.2; 18182 -8.9; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K702 65th Anv Ed 2014 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K702 65th Anv Ed 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 1.5  | 3.1 dB  |
| Peaking | 209 Hz   | 0.45 | -4.9 dB |
| Peaking | 2009 Hz  | 3.07 | -5.6 dB |
| Peaking | 3105 Hz  | 2.52 | 6.5 dB  |
| Peaking | 7157 Hz  | 1.98 | -5.8 dB |
| Peaking | 1197 Hz  | 2.19 | 1.8 dB  |
| Peaking | 1612 Hz  | 5.42 | -1.8 dB |
| Peaking | 8613 Hz  | 6    | -1.9 dB |
| Peaking | 10531 Hz | 1.48 | 1.5 dB  |
| Peaking | 18670 Hz | 1.13 | -3.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K702%2065th%20Anv%20Ed%202014/AKG%20K702%2065th%20Anv%20Ed%202014.png)