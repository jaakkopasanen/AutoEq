# AKG K44
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -2.1; 25 -2.8; 28 -3.7; 31 -4.5; 34 -5.1; 37 -5.6; 41 -6.1; 45 -6.5; 49 -6.7; 54 -7.0; 60 -7.3; 66 -7.5; 72 -7.7; 79 -7.8; 87 -7.9; 96 -8.0; 106 -8.1; 116 -8.4; 128 -8.6; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.4; 249 -9.6; 274 -9.8; 302 -10.1; 332 -10.2; 365 -10.2; 402 -10.4; 442 -10.8; 486 -10.7; 535 -9.9; 588 -9.6; 647 -10.8; 712 -10.5; 783 -9.0; 861 -9.1; 947 -10.7; 1042 -11.5; 1146 -11.3; 1261 -10.3; 1387 -8.9; 1526 -7.4; 1678 -5.7; 1846 -4.6; 2031 -4.6; 2234 -3.4; 2457 -1.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -2.4; 5267 -2.5; 5793 -0.5; 6373 -1.5; 7010 -5.6; 7711 -7.2; 8482 -6.6; 9330 -6.8; 10263 -10.0; 11289 -12.0; 12418 -9.7; 13660 -7.2; 15026 -7.1; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K44 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K44 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.79 | 5.3 dB  |
| Peaking | 1036 Hz  | 0.15 | -4.9 dB |
| Peaking | 3162 Hz  | 0.88 | 10.9 dB |
| Peaking | 5915 Hz  | 5.03 | 5.1 dB  |
| Peaking | 11290 Hz | 3.09 | -5.9 dB |
| Peaking | 829 Hz   | 5.04 | 2.1 dB  |
| Peaking | 1119 Hz  | 2.73 | -2.6 dB |
| Peaking | 1748 Hz  | 3.77 | 1.6 dB  |
| Peaking | 3273 Hz  | 7.03 | -1.0 dB |
| Peaking | 4424 Hz  | 9.83 | 1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.0 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -1.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.7 dB |
| Peaking | 1000 Hz  | 1.41 | -4.9 dB |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -1.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K44/AKG%20K44.png)