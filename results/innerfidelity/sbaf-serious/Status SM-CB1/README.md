# Status SM-CB1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.2; 28 -2.2; 31 -3.1; 34 -3.9; 37 -4.6; 41 -5.5; 45 -6.2; 49 -6.7; 54 -7.2; 60 -7.7; 66 -8.0; 72 -8.1; 79 -8.4; 87 -8.6; 96 -8.6; 106 -8.2; 116 -8.1; 128 -8.5; 141 -8.7; 155 -8.9; 170 -8.3; 187 -8.6; 206 -8.7; 227 -8.6; 249 -8.5; 274 -7.9; 302 -7.3; 332 -7.0; 365 -6.5; 402 -5.9; 442 -5.2; 486 -5.0; 535 -5.3; 588 -5.7; 647 -6.4; 712 -6.8; 783 -6.9; 861 -7.2; 947 -6.4; 1042 -6.9; 1146 -7.5; 1261 -7.6; 1387 -7.7; 1526 -7.9; 1678 -8.0; 1846 -7.8; 2031 -6.9; 2234 -5.8; 2457 -4.3; 2703 -3.3; 2973 -4.4; 3270 -5.5; 3597 -5.4; 3957 -4.9; 4353 -4.2; 4788 -2.8; 5267 -2.4; 5793 -4.4; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -9.2; 9330 -10.4; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Status SM-CB1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Status SM-CB1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.16 | 6.3 dB  |
| Peaking | 111 Hz  | 0.56 | -2.5 dB |
| Peaking | 5013 Hz | 1.27 | 3.1 dB  |
| Peaking | 6987 Hz | 2.39 | 1.1 dB  |
| Peaking | 8958 Hz | 4.82 | -5.6 dB |
| Peaking | 235 Hz  | 2.9  | -1.0 dB |
| Peaking | 474 Hz  | 2.44 | 2.1 dB  |
| Peaking | 1707 Hz | 1.3  | -2.1 dB |
| Peaking | 2710 Hz | 2.82 | 4.1 dB  |
| Peaking | 3234 Hz | 2.93 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.8 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | -0.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Status%20SM-CB1/Status%20SM-CB1.png)