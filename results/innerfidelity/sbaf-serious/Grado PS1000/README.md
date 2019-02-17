# Grado PS1000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.6; 37 -1.1; 41 -2.4; 45 -3.6; 49 -4.7; 54 -6.1; 60 -7.5; 66 -8.7; 72 -9.7; 79 -10.6; 87 -11.3; 96 -11.8; 106 -11.8; 116 -11.6; 128 -11.2; 141 -10.7; 155 -10.3; 170 -9.8; 187 -9.2; 206 -8.7; 227 -8.2; 249 -7.8; 274 -7.2; 302 -6.9; 332 -6.9; 365 -6.5; 402 -6.6; 442 -6.4; 486 -6.4; 535 -6.3; 588 -6.1; 647 -6.0; 712 -6.3; 783 -6.0; 861 -6.3; 947 -6.4; 1042 -6.6; 1146 -7.1; 1261 -7.6; 1387 -8.3; 1526 -8.7; 1678 -8.2; 1846 -8.4; 2031 -7.7; 2234 -7.7; 2457 -7.8; 2703 -8.2; 2973 -8.4; 3270 -8.9; 3597 -7.5; 3957 -11.0; 4353 -13.1; 4788 -12.6; 5267 -13.8; 5793 -15.3; 6373 -18.4; 7010 -16.5; 7711 -13.4; 8482 -14.0; 9330 -16.9; 10263 -14.8; 11289 -8.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado PS1000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.74 | 7.4 dB   |
| Peaking | 97 Hz    | 0.88 | -6.8 dB  |
| Peaking | 1567 Hz  | 3.04 | -1.9 dB  |
| Peaking | 6256 Hz  | 1.48 | -10.6 dB |
| Peaking | 9623 Hz  | 4.64 | -8.2 dB  |
| Peaking | 606 Hz   | 1.07 | 0.8 dB   |
| Peaking | 3630 Hz  | 6.41 | 4.6 dB   |
| Peaking | 4094 Hz  | 2.43 | -3.4 dB  |
| Peaking | 5464 Hz  | 5.74 | 2.2 dB   |
| Peaking | 12417 Hz | 3.95 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB   |
| Peaking | 62 Hz    | 1.41 | -2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.3 dB  |
| Peaking | 500 Hz   | 1.41 | 0.8 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -10.7 dB |
| Peaking | 16000 Hz | 1.41 | 1.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)