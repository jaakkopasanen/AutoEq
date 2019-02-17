# Fidue A71
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.2; 23 -8.6; 25 -9.0; 28 -9.4; 31 -9.7; 34 -10.0; 37 -10.2; 41 -10.5; 45 -10.7; 49 -11.0; 54 -11.3; 60 -11.6; 66 -11.9; 72 -12.2; 79 -12.5; 87 -12.8; 96 -13.2; 106 -13.3; 116 -13.4; 128 -13.6; 141 -13.6; 155 -13.6; 170 -13.5; 187 -13.2; 206 -13.0; 227 -12.6; 249 -12.3; 274 -11.8; 302 -11.3; 332 -10.8; 365 -10.3; 402 -9.9; 442 -8.8; 486 -8.1; 535 -7.7; 588 -6.9; 647 -6.4; 712 -6.3; 783 -5.8; 861 -5.9; 947 -6.2; 1042 -6.7; 1146 -7.2; 1261 -8.0; 1387 -9.2; 1526 -10.6; 1678 -11.6; 1846 -11.5; 2031 -10.3; 2234 -8.6; 2457 -6.5; 2703 -3.9; 2973 -0.9; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -4.5; 7010 -8.5; 7711 -7.8; 8482 -7.4; 9330 -7.3; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fidue A71 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 89 Hz    | 0.38 | -5.3 dB  |
| Peaking | 222 Hz   | 0.69 | -3.5 dB  |
| Peaking | 1870 Hz  | 1.16 | -14.9 dB |
| Peaking | 3147 Hz  | 0.38 | 12.0 dB  |
| Peaking | 7970 Hz  | 1.32 | -7.3 dB  |
| Peaking | 4119 Hz  | 5.35 | -0.7 dB  |
| Peaking | 5979 Hz  | 4.47 | 3.8 dB   |
| Peaking | 6810 Hz  | 4.19 | -4.5 dB  |
| Peaking | 8091 Hz  | 2.6  | 1.8 dB   |
| Peaking | 13615 Hz | 0.97 | -0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.0 dB |
| Peaking | 4000 Hz  | 1.41 | 9.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A71/Fidue%20A71.png)