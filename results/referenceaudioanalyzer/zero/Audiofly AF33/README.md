# Audiofly AF33
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -20.2; 23 -20.0; 25 -19.7; 28 -19.3; 31 -19.0; 34 -18.6; 37 -18.2; 41 -17.7; 45 -17.3; 49 -16.8; 54 -16.3; 60 -15.7; 66 -15.1; 72 -14.5; 79 -13.9; 87 -13.2; 96 -12.4; 106 -11.6; 116 -10.9; 128 -10.5; 141 -10.1; 155 -9.6; 170 -8.9; 187 -8.1; 206 -7.2; 227 -6.6; 249 -6.3; 274 -6.1; 302 -6.0; 332 -5.7; 365 -5.1; 402 -4.4; 442 -3.9; 486 -3.3; 535 -2.9; 588 -2.5; 647 -2.2; 712 -1.9; 783 -1.8; 861 -1.6; 947 -1.3; 1042 -0.9; 1146 -0.5; 1261 -0.5; 1387 -0.6; 1526 -0.8; 1678 -1.2; 1846 -2.4; 2031 -3.9; 2234 -5.3; 2457 -7.2; 2703 -9.3; 2973 -11.2; 3270 -11.8; 3597 -10.9; 3957 -9.8; 4353 -9.6; 4788 -9.6; 5267 -10.2; 5793 -12.3; 6373 -13.2; 7010 -10.6; 7711 -6.0; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -5.9; 15026 -5.9; 16529 -5.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audiofly AF33 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audiofly AF33 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 11 Hz   | 0.58 | -14.0 dB |
| Peaking | 44 Hz   | 0.38 | -8.7 dB  |
| Peaking | 1997 Hz | 0.35 | 9.1 dB   |
| Peaking | 3149 Hz | 1.08 | -13.5 dB |
| Peaking | 6182 Hz | 3.01 | -8.2 dB  |
| Peaking | 153 Hz  | 5.22 | -0.5 dB  |
| Peaking | 225 Hz  | 5.19 | 0.7 dB   |
| Peaking | 905 Hz  | 5.73 | -0.5 dB  |
| Peaking | 6943 Hz | 9.72 | -1.5 dB  |
| Peaking | 7777 Hz | 6.72 | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -14.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 5.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.4 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audiofly%20AF33/Audiofly%20AF33.png)