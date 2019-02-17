# Read Heath Audio MA600
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.0; 23 -13.1; 25 -13.2; 28 -13.3; 31 -13.5; 34 -13.6; 37 -13.6; 41 -13.7; 45 -13.8; 49 -13.9; 54 -14.0; 60 -14.3; 66 -14.4; 72 -14.6; 79 -14.8; 87 -15.0; 96 -15.2; 106 -15.2; 116 -15.2; 128 -15.2; 141 -15.1; 155 -14.9; 170 -14.6; 187 -14.2; 206 -13.9; 227 -13.3; 249 -12.8; 274 -12.2; 302 -11.5; 332 -10.9; 365 -10.1; 402 -9.4; 442 -8.5; 486 -7.8; 535 -7.0; 588 -5.9; 647 -5.2; 712 -4.5; 783 -3.6; 861 -3.2; 947 -2.8; 1042 -2.5; 1146 -2.2; 1261 -1.9; 1387 -2.1; 1526 -1.1; 1678 -1.1; 1846 -1.7; 2031 -3.0; 2234 -3.8; 2457 -3.3; 2703 -3.2; 2973 -3.6; 3270 -4.4; 3597 -6.0; 3957 -7.7; 4353 -11.2; 4788 -14.4; 5267 -12.1; 5793 -6.3; 6373 -2.1; 7010 -0.5; 7711 -2.3; 8482 -2.6; 9330 -2.7; 10263 -5.9; 11289 -5.9; 12418 -3.3; 13660 -7.0; 15026 -11.7; 16529 -9.8; 18182 -5.6; 20000 -2.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Read Heath Audio MA600 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Read Heath Audio MA600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.22 | -10.3 dB |
| Peaking | 154 Hz   | 0.68 | -6.6 dB  |
| Peaking | 335 Hz   | 1.25 | -3.8 dB  |
| Peaking | 4774 Hz  | 4    | -12.7 dB |
| Peaking | 15641 Hz | 1.71 | -9.7 dB  |
| Peaking | 1442 Hz  | 0.86 | 4.2 dB   |
| Peaking | 1778 Hz  | 0.43 | -2.6 dB  |
| Peaking | 5406 Hz  | 6.66 | -3.7 dB  |
| Peaking | 6607 Hz  | 2.12 | 4.2 dB   |
| Peaking | 10593 Hz | 8.03 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.7 dB |
| Peaking | 62 Hz    | 1.41 | -8.3 dB  |
| Peaking | 125 Hz   | 1.41 | -10.2 dB |
| Peaking | 250 Hz   | 1.41 | -8.3 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -7.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -9.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Read%20Heath%20Audio%20MA600/Read%20Heath%20Audio%20MA600.png)