# Stax SR-003 SA-1993
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.5; 25 -2.7; 28 -3.0; 31 -3.2; 34 -3.3; 37 -3.5; 41 -3.7; 45 -3.9; 49 -4.2; 54 -4.4; 60 -4.8; 66 -5.1; 72 -5.5; 79 -5.9; 87 -6.3; 96 -6.8; 106 -7.2; 116 -7.4; 128 -7.8; 141 -8.1; 155 -8.5; 170 -8.5; 187 -8.7; 206 -8.9; 227 -9.0; 249 -9.2; 274 -9.2; 302 -9.5; 332 -9.5; 365 -9.6; 402 -9.9; 442 -10.0; 486 -10.2; 535 -10.3; 588 -9.8; 647 -9.3; 712 -8.6; 783 -7.5; 861 -6.1; 947 -6.2; 1042 -7.0; 1146 -7.8; 1261 -9.2; 1387 -10.4; 1526 -12.4; 1678 -12.5; 1846 -10.1; 2031 -8.7; 2234 -7.2; 2457 -5.3; 2703 -4.4; 2973 -1.9; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -3.7; 6373 -3.7; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -9.1; 16529 -10.7; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-003 SA-1993 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-003 SA-1993 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.51 | 4.0 dB  |
| Peaking | 326 Hz   | 0.57 | -3.5 dB |
| Peaking | 1644 Hz  | 2.83 | -7.0 dB |
| Peaking | 3971 Hz  | 1.28 | 7.1 dB  |
| Peaking | 16322 Hz | 2.13 | -4.7 dB |
| Peaking | 568 Hz   | 2.96 | -1.3 dB |
| Peaking | 896 Hz   | 4.54 | 2.4 dB  |
| Peaking | 5293 Hz  | 6.17 | 0.9 dB  |
| Peaking | 5310 Hz  | 6.93 | 1.3 dB  |
| Peaking | 7486 Hz  | 1.91 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 8.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-003%20SA-1993/Stax%20SR-003%20SA-1993.png)