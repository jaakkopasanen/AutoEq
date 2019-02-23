# AKG K376
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.0; 23 -15.9; 25 -15.8; 28 -15.6; 31 -15.4; 34 -15.3; 37 -15.1; 41 -14.9; 45 -14.7; 49 -14.6; 54 -14.4; 60 -14.2; 66 -14.1; 72 -13.9; 79 -13.8; 87 -13.7; 96 -13.5; 106 -13.2; 116 -12.9; 128 -12.6; 141 -12.3; 155 -11.9; 170 -11.4; 187 -10.9; 206 -10.3; 227 -9.7; 249 -9.1; 274 -8.5; 302 -7.8; 332 -7.2; 365 -6.5; 402 -5.9; 442 -5.1; 486 -4.7; 535 -4.1; 588 -3.4; 647 -2.7; 712 -2.6; 783 -2.0; 861 -2.1; 947 -2.6; 1042 -3.0; 1146 -3.3; 1261 -3.7; 1387 -4.5; 1526 -5.3; 1678 -6.0; 1846 -6.5; 2031 -7.0; 2234 -7.9; 2457 -8.5; 2703 -8.3; 2973 -5.4; 3270 -2.0; 3597 -0.5; 3957 -1.5; 4353 -4.0; 4788 -6.9; 5267 -8.8; 5793 -7.4; 6373 -3.0; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K376 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K376 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.5  | -8.4 dB |
| Peaking | 101 Hz  | 0.36 | -6.6 dB |
| Peaking | 798 Hz  | 0.69 | 4.6 dB  |
| Peaking | 2770 Hz | 1.08 | -5.5 dB |
| Peaking | 3517 Hz | 3.05 | 9.6 dB  |
| Peaking | 4137 Hz | 7.11 | 1.8 dB  |
| Peaking | 5408 Hz | 3.87 | -4.2 dB |
| Peaking | 6569 Hz | 5.23 | 5.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.3 dB |
| Peaking | 62 Hz    | 1.41 | -5.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K376/AKG%20K376.png)