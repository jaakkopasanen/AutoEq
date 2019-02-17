# Dunu DN1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.7; 25 -10.7; 28 -10.6; 31 -10.6; 34 -10.6; 37 -10.6; 41 -10.6; 45 -10.6; 49 -10.7; 54 -10.7; 60 -10.8; 66 -10.9; 72 -11.0; 79 -11.1; 87 -11.3; 96 -11.4; 106 -11.3; 116 -11.2; 128 -11.2; 141 -11.1; 155 -11.0; 170 -10.7; 187 -10.5; 206 -10.2; 227 -9.8; 249 -9.5; 274 -9.2; 302 -8.8; 332 -8.5; 365 -8.1; 402 -7.8; 442 -7.4; 486 -7.2; 535 -6.9; 588 -6.4; 647 -6.3; 712 -6.2; 783 -5.9; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -6.8; 1261 -7.0; 1387 -7.4; 1526 -7.7; 1678 -7.7; 1846 -7.3; 2031 -6.7; 2234 -6.0; 2457 -4.8; 2703 -4.1; 2973 -2.8; 3270 -0.8; 3597 -0.5; 3957 -0.9; 4353 -6.1; 4788 -8.0; 5267 -5.3; 5793 -4.9; 6373 -4.7; 7010 -5.2; 7711 -7.6; 8482 -12.0; 9330 -14.7; 10263 -12.6; 11289 -6.9; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Dunu DN1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.19 | -3.9 dB |
| Peaking | 152 Hz   | 0.68 | -2.9 dB |
| Peaking | 3467 Hz  | 3.35 | 6.9 dB  |
| Peaking | 6693 Hz  | 3.96 | 2.9 dB  |
| Peaking | 9314 Hz  | 3.39 | -9.3 dB |
| Peaking | 741 Hz   | 2.24 | 1.0 dB  |
| Peaking | 1603 Hz  | 2.81 | -1.6 dB |
| Peaking | 4304 Hz  | 2.45 | 2.5 dB  |
| Peaking | 4657 Hz  | 6.41 | -5.7 dB |
| Peaking | 11716 Hz | 6.93 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN1000/Dunu%20DN1000.png)