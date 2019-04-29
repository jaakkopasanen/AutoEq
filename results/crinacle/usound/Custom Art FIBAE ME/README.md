# Custom Art FIBAE ME
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -9.9; 28 -10.1; 31 -10.3; 34 -10.5; 37 -10.6; 41 -10.8; 45 -11.0; 49 -11.1; 54 -11.3; 60 -11.5; 66 -11.8; 72 -12.1; 79 -12.4; 87 -12.7; 96 -13.1; 106 -13.4; 116 -13.6; 128 -13.8; 141 -13.9; 155 -14.0; 170 -14.0; 187 -13.9; 206 -13.7; 227 -13.4; 249 -13.1; 274 -12.7; 302 -12.3; 332 -11.8; 365 -11.2; 402 -10.7; 442 -10.1; 486 -9.4; 535 -8.6; 588 -7.8; 647 -7.0; 712 -6.1; 783 -5.2; 861 -4.4; 947 -3.9; 1042 -3.9; 1146 -4.6; 1261 -5.5; 1387 -6.6; 1526 -7.4; 1678 -8.6; 1846 -9.2; 2031 -7.3; 2234 -5.2; 2457 -3.1; 2703 -1.7; 2973 -2.3; 3270 -4.3; 3597 -4.6; 3957 -0.7; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.3; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.6; 18182 -9.1; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Custom Art FIBAE ME GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Custom Art FIBAE ME ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 54 Hz   | 0.37 | -4.2 dB |
| Peaking | 162 Hz  | 0.89 | -5.2 dB |
| Peaking | 316 Hz  | 1.63 | -3.2 dB |
| Peaking | 2736 Hz | 5.37 | 4.3 dB  |
| Peaking | 4998 Hz | 1.84 | 6.9 dB  |
| Peaking | 977 Hz  | 2.37 | 3.4 dB  |
| Peaking | 1809 Hz | 3.21 | -3.7 dB |
| Peaking | 2343 Hz | 4.72 | 1.5 dB  |
| Peaking | 6429 Hz | 7.35 | 2.6 dB  |
| Peaking | 8771 Hz | 4.39 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.9 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Custom%20Art%20FIBAE%20ME/Custom%20Art%20FIBAE%20ME.png)