# Sennheiser MX 560
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.6; 141 -0.8; 155 -1.1; 170 -1.3; 187 -1.4; 206 -1.5; 227 -1.6; 249 -1.8; 274 -1.8; 302 -1.7; 332 -1.6; 365 -2.7; 402 -2.5; 442 -2.3; 486 -1.9; 535 -2.1; 588 -2.1; 647 -2.4; 712 -2.8; 783 -2.8; 861 -3.3; 947 -3.7; 1042 -4.2; 1146 -4.6; 1261 -5.5; 1387 -6.8; 1526 -8.5; 1678 -10.3; 1846 -12.4; 2031 -14.2; 2234 -15.8; 2457 -16.2; 2703 -16.3; 2973 -14.6; 3270 -12.1; 3597 -10.4; 3957 -10.4; 4353 -12.3; 4788 -13.5; 5267 -14.2; 5793 -14.7; 6373 -13.0; 7010 -11.3; 7711 -11.6; 8482 -11.0; 9330 -7.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.7; 15026 -7.7; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser MX 560 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MX 560 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 108 Hz  | 0.34 | 5.1 dB   |
| Peaking | 779 Hz  | 0.56 | 3.7 dB   |
| Peaking | 2350 Hz | 1.5  | -10.9 dB |
| Peaking | 5817 Hz | 1.63 | -7.2 dB  |
| Peaking | 18 Hz   | 0.59 | 3.8 dB   |
| Peaking | 32 Hz   | 0.46 | 1.1 dB   |
| Peaking | 3754 Hz | 9    | 1.8 dB   |
| Peaking | 8326 Hz | 5.3  | -3.7 dB  |
| Peaking | 9560 Hz | 2.33 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 4.4 dB  |
| Peaking | 125 Hz   | 1.41 | 4.6 dB  |
| Peaking | 250 Hz   | 1.41 | 3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.1 dB |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20MX%20560/Sennheiser%20MX%20560.png)