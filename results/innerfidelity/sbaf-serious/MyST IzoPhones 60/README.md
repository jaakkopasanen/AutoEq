# MyST IzoPhones 60
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.9; 60 -3.7; 66 -5.1; 72 -6.1; 79 -7.0; 87 -7.5; 96 -7.8; 106 -7.8; 116 -7.7; 128 -7.6; 141 -7.5; 155 -7.4; 170 -7.1; 187 -7.0; 206 -6.8; 227 -6.5; 249 -6.2; 274 -5.8; 302 -5.3; 332 -5.4; 365 -5.6; 402 -5.7; 442 -5.4; 486 -5.8; 535 -5.6; 588 -5.0; 647 -5.1; 712 -5.4; 783 -5.4; 861 -5.9; 947 -6.7; 1042 -6.4; 1146 -6.7; 1261 -6.8; 1387 -7.2; 1526 -7.2; 1678 -7.0; 1846 -5.3; 2031 -4.0; 2234 -3.9; 2457 -2.8; 2703 -2.7; 2973 -4.3; 3270 -5.0; 3597 -6.2; 3957 -8.2; 4353 -10.5; 4788 -6.9; 5267 -3.4; 5793 -1.0; 6373 -6.2; 7010 -10.7; 7711 -11.2; 8482 -13.5; 9330 -13.4; 10263 -7.3; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.0; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`MyST IzoPhones 60 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MyST IzoPhones 60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.16 | 7.3 dB  |
| Peaking | 2562 Hz  | 2.64 | 4.2 dB  |
| Peaking | 4282 Hz  | 6.37 | -4.9 dB |
| Peaking | 5669 Hz  | 5.22 | 6.9 dB  |
| Peaking | 8438 Hz  | 2.6  | -7.9 dB |
| Peaking | 51 Hz    | 2.57 | 4.1 dB  |
| Peaking | 95 Hz    | 0.59 | -2.5 dB |
| Peaking | 394 Hz   | 0.51 | 1.4 dB  |
| Peaking | 1432 Hz  | 2.88 | -1.6 dB |
| Peaking | 10810 Hz | 6.3  | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MyST%20IzoPhones%2060/MyST%20IzoPhones%2060.png)