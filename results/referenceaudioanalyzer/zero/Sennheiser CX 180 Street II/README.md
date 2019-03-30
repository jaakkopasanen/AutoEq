# Sennheiser CX 180 Street II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.5; 23 -19.3; 25 -19.1; 28 -18.8; 31 -18.4; 34 -18.1; 37 -17.8; 41 -17.4; 45 -16.9; 49 -16.5; 54 -16.0; 60 -15.4; 66 -14.9; 72 -14.4; 79 -13.7; 87 -13.1; 96 -12.5; 106 -11.9; 116 -11.1; 128 -10.4; 141 -9.7; 155 -9.0; 170 -8.3; 187 -7.5; 206 -6.9; 227 -6.0; 249 -5.2; 274 -4.4; 302 -4.3; 332 -4.7; 365 -4.4; 402 -3.7; 442 -3.1; 486 -2.6; 535 -2.2; 588 -1.8; 647 -1.5; 712 -1.2; 783 -0.9; 861 -0.8; 947 -0.8; 1042 -0.6; 1146 -0.5; 1261 -0.8; 1387 -1.1; 1526 -1.6; 1678 -2.2; 1846 -3.2; 2031 -4.6; 2234 -6.4; 2457 -8.9; 2703 -11.6; 2973 -13.1; 3270 -12.4; 3597 -10.0; 3957 -7.7; 4353 -6.9; 4788 -6.7; 5267 -7.9; 5793 -12.1; 6373 -14.6; 7010 -12.0; 7711 -5.6; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.4; 18182 -5.4; 20000 -5.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 180 Street II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 180 Street II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.9dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 12 Hz    |  0.56 | -13.3 dB |
| Peaking | 49 Hz    |  0.39 | -8.5 dB  |
| Peaking | 1665 Hz  |  0.26 | 6.3 dB   |
| Peaking | 2963 Hz  |  1.65 | -13.4 dB |
| Peaking | 6361 Hz  |  3.6  | -11.6 dB |
| Peaking | 280 Hz   |  3.32 | 1.6 dB   |
| Peaking | 337 Hz   |  2.36 | -1.1 dB  |
| Peaking | 7042 Hz  | 10.4  | -2.5 dB  |
| Peaking | 7674 Hz  |  5.05 | 2.3 dB   |
| Peaking | 11337 Hz |  1    | -0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB  |
| Peaking | 250 Hz   | 1.41 | 0.6 dB   |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX%20180%20Street%20II/Sennheiser%20CX%20180%20Street%20II.png)