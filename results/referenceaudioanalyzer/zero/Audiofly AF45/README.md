# Audiofly AF45
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -20.6; 23 -20.5; 25 -20.5; 28 -20.3; 31 -20.0; 34 -19.8; 37 -19.6; 41 -19.3; 45 -19.0; 49 -18.7; 54 -18.3; 60 -17.8; 66 -17.4; 72 -16.9; 79 -16.4; 87 -15.9; 96 -15.3; 106 -14.6; 116 -14.0; 128 -13.3; 141 -12.5; 155 -11.8; 170 -10.9; 187 -10.0; 206 -9.3; 227 -8.9; 249 -9.2; 274 -9.2; 302 -8.5; 332 -7.6; 365 -6.8; 402 -5.9; 442 -5.2; 486 -4.5; 535 -3.8; 588 -3.2; 647 -2.6; 712 -2.1; 783 -1.6; 861 -1.1; 947 -0.7; 1042 -0.5; 1146 -0.7; 1261 -1.0; 1387 -1.5; 1526 -2.0; 1678 -2.5; 1846 -3.2; 2031 -4.3; 2234 -5.6; 2457 -6.8; 2703 -7.8; 2973 -8.4; 3270 -8.4; 3597 -8.2; 3957 -8.8; 4353 -10.0; 4788 -11.7; 5267 -12.8; 5793 -11.7; 6373 -6.9; 7010 -3.2; 7711 -5.4; 8482 -5.7; 9330 -5.7; 10263 -5.7; 11289 -5.7; 12418 -5.7; 13660 -5.7; 15026 -5.7; 16529 -5.7; 18182 -5.7; 20000 -5.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audiofly AF45 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audiofly AF45 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 10 Hz   | 1.23 | -14.2 dB |
| Peaking | 31 Hz   | 0.26 | -11.2 dB |
| Peaking | 78 Hz   | 0.35 | -2.3 dB  |
| Peaking | 982 Hz  | 0.94 | 5.8 dB   |
| Peaking | 4838 Hz | 2.04 | -6.9 dB  |
| Peaking | 290 Hz  | 5.86 | -1.2 dB  |
| Peaking | 2923 Hz | 1.71 | -5.8 dB  |
| Peaking | 3420 Hz | 0.73 | 3.6 dB   |
| Peaking | 5710 Hz | 4.09 | -4.3 dB  |
| Peaking | 6831 Hz | 6.5  | 4.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.8 dB |
| Peaking | 62 Hz    | 1.41 | -8.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 4000 Hz  | 1.41 | -6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audiofly%20AF45/Audiofly%20AF45.png)