# Sennheiser CX 200 Street II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.9; 23 -17.7; 25 -17.5; 28 -17.2; 31 -16.9; 34 -16.6; 37 -16.3; 41 -15.9; 45 -15.5; 49 -15.1; 54 -14.6; 60 -14.0; 66 -13.5; 72 -12.9; 79 -12.4; 87 -11.7; 96 -11.1; 106 -10.4; 116 -9.7; 128 -9.0; 141 -8.2; 155 -7.5; 170 -6.7; 187 -5.8; 206 -4.7; 227 -4.3; 249 -5.0; 274 -5.5; 302 -5.0; 332 -4.2; 365 -3.5; 402 -2.9; 442 -2.4; 486 -1.9; 535 -1.5; 588 -1.2; 647 -0.9; 712 -0.7; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.7; 1387 -1.1; 1526 -1.6; 1678 -2.3; 1846 -3.3; 2031 -4.7; 2234 -6.6; 2457 -9.2; 2703 -12.2; 2973 -13.8; 3270 -13.2; 3597 -10.8; 3957 -8.6; 4353 -7.9; 4788 -7.7; 5267 -8.9; 5793 -12.2; 6373 -13.8; 7010 -10.9; 7711 -5.1; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.1; 16529 -5.1; 18182 -5.1; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser CX 200 Street II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 200 Street II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 21 Hz   |  0.51 | -11.5 dB |
| Peaking | 67 Hz   |  0.62 | -4.7 dB  |
| Peaking | 1780 Hz |  0.28 | 6.9 dB   |
| Peaking | 2988 Hz |  1.46 | -14.9 dB |
| Peaking | 6273 Hz |  3.39 | -10.5 dB |
| Peaking | 219 Hz  |  4.63 | 1.7 dB   |
| Peaking | 282 Hz  |  3.72 | -1.4 dB  |
| Peaking | 7026 Hz | 10.23 | -1.9 dB  |
| Peaking | 7722 Hz |  7.69 | 2.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB   |
| Peaking | 500 Hz   | 1.41 | 2.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 16000 Hz | 1.41 | 0.5 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sennheiser%20CX%20200%20Street%20II/Sennheiser%20CX%20200%20Street%20II.png)