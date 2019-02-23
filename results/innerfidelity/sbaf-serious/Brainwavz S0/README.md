# Brainwavz S0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.8; 23 -9.0; 25 -9.1; 28 -9.3; 31 -9.5; 34 -9.6; 37 -9.7; 41 -9.9; 45 -10.0; 49 -10.2; 54 -10.4; 60 -10.6; 66 -10.9; 72 -11.1; 79 -11.4; 87 -11.6; 96 -11.9; 106 -12.0; 116 -12.0; 128 -12.1; 141 -12.1; 155 -12.0; 170 -11.8; 187 -11.6; 206 -11.3; 227 -10.8; 249 -10.5; 274 -10.0; 302 -9.4; 332 -8.9; 365 -8.2; 402 -7.5; 442 -6.8; 486 -6.3; 535 -5.5; 588 -4.6; 647 -4.0; 712 -3.6; 783 -2.9; 861 -2.5; 947 -2.2; 1042 -1.7; 1146 -1.9; 1261 -1.5; 1387 -1.1; 1526 -1.4; 1678 -3.6; 1846 -4.7; 2031 -4.3; 2234 -3.8; 2457 -2.9; 2703 -2.2; 2973 -1.1; 3270 -0.6; 3597 -0.9; 3957 -2.2; 4353 -5.6; 4788 -8.7; 5267 -10.4; 5793 -5.4; 6373 -0.5; 7010 -2.7; 7711 -4.9; 8482 -5.2; 9330 -5.2; 10263 -5.2; 11289 -5.2; 12418 -5.2; 13660 -5.2; 15026 -5.2; 16529 -5.2; 18182 -5.2; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 41 Hz   | 0.25 | -3.7 dB  |
| Peaking | 171 Hz  | 0.51 | -4.9 dB  |
| Peaking | 992 Hz  | 1.02 | 4.0 dB   |
| Peaking | 4475 Hz | 1.02 | 6.5 dB   |
| Peaking | 4979 Hz | 3.72 | -12.1 dB |
| Peaking | 1503 Hz | 3.99 | 3.4 dB   |
| Peaking | 1735 Hz | 2.1  | -2.7 dB  |
| Peaking | 3176 Hz | 2.95 | 1.8 dB   |
| Peaking | 6488 Hz | 5.53 | 6.0 dB   |
| Peaking | 6768 Hz | 1.13 | -2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S0/Brainwavz%20S0.png)