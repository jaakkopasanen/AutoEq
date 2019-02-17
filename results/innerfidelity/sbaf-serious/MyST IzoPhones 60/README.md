# MyST IzoPhones 60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.7; 60 -3.5; 66 -4.8; 72 -5.9; 79 -6.8; 87 -7.3; 96 -7.6; 106 -7.6; 116 -7.5; 128 -7.4; 141 -7.2; 155 -7.1; 170 -6.9; 187 -6.7; 206 -6.5; 227 -6.3; 249 -6.0; 274 -5.6; 302 -5.1; 332 -5.2; 365 -5.3; 402 -5.5; 442 -5.2; 486 -5.6; 535 -5.4; 588 -4.8; 647 -4.9; 712 -5.2; 783 -5.1; 861 -5.7; 947 -6.5; 1042 -6.2; 1146 -6.4; 1261 -6.6; 1387 -7.0; 1526 -6.9; 1678 -6.8; 1846 -5.1; 2031 -3.8; 2234 -3.7; 2457 -2.5; 2703 -2.4; 2973 -4.0; 3270 -4.8; 3597 -6.0; 3957 -8.0; 4353 -10.3; 4788 -6.7; 5267 -3.2; 5793 -1.2; 6373 -6.0; 7010 -10.4; 7711 -11.0; 8482 -13.3; 9330 -13.2; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -7.4; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MyST IzoPhones 60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST IzoPhones 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 1.12 | 7.2 dB  |
| Peaking | 2557 Hz  | 2.39 | 4.4 dB  |
| Peaking | 4326 Hz  | 6.47 | -5.0 dB |
| Peaking | 5715 Hz  | 4.95 | 6.7 dB  |
| Peaking | 8464 Hz  | 2.63 | -7.7 dB |
| Peaking | 52 Hz    | 2.62 | 3.9 dB  |
| Peaking | 93 Hz    | 0.59 | -2.4 dB |
| Peaking | 411 Hz   | 0.52 | 1.6 dB  |
| Peaking | 1449 Hz  | 2.97 | -1.5 dB |
| Peaking | 10790 Hz | 6.4  | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.8 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MyST%20IzoPhones%2060/MyST%20IzoPhones%2060.png)