# Brainwavz S0
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -10.0; 25 -10.1; 28 -10.3; 31 -10.5; 34 -10.6; 37 -10.7; 41 -10.9; 45 -11.0; 49 -11.2; 54 -11.4; 60 -11.6; 66 -11.9; 72 -12.1; 79 -12.4; 87 -12.6; 96 -12.9; 106 -12.9; 116 -13.0; 128 -13.1; 141 -13.1; 155 -13.0; 170 -12.8; 187 -12.6; 206 -12.3; 227 -11.8; 249 -11.5; 274 -11.0; 302 -10.4; 332 -9.8; 365 -9.2; 402 -8.5; 442 -7.8; 486 -7.2; 535 -6.5; 588 -5.6; 647 -5.0; 712 -4.5; 783 -3.9; 861 -3.5; 947 -3.2; 1042 -2.7; 1146 -2.9; 1261 -2.5; 1387 -2.1; 1526 -2.4; 1678 -4.6; 1846 -5.7; 2031 -5.3; 2234 -4.8; 2457 -3.9; 2703 -3.2; 2973 -2.1; 3270 -1.6; 3597 -1.9; 3957 -3.2; 4353 -6.6; 4788 -9.7; 5267 -11.4; 5793 -6.4; 6373 -1.4; 7010 -0.5; 7711 -2.7; 8482 -3.0; 9330 -3.0; 10263 -3.0; 11289 -3.0; 12418 -3.0; 13660 -3.0; 15026 -3.0; 16529 -3.0; 18182 -3.0; 20000 -3.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Brainwavz S0 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz S0 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.29 | -6.7 dB |
| Peaking | 121 Hz  | 0.7  | -5.5 dB |
| Peaking | 233 Hz  | 1.02 | -4.4 dB |
| Peaking | 403 Hz  | 1.6  | -2.4 dB |
| Peaking | 5125 Hz | 5.73 | -9.5 dB |
| Peaking | 1507 Hz | 1.87 | 4.3 dB  |
| Peaking | 1805 Hz | 1.92 | -5.4 dB |
| Peaking | 3580 Hz | 2.23 | 3.2 dB  |
| Peaking | 4407 Hz | 3.26 | -3.1 dB |
| Peaking | 6722 Hz | 6.75 | 4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB |
| Peaking | 125 Hz   | 1.41 | -8.4 dB |
| Peaking | 250 Hz   | 1.41 | -7.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | -2.3 dB |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20S0/Brainwavz%20S0.png)