# Fischer Audio TS-9005
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -18.9; 23 -18.9; 25 -18.8; 28 -18.7; 31 -18.6; 34 -18.5; 37 -18.3; 41 -18.0; 45 -17.7; 49 -17.5; 54 -17.2; 60 -16.9; 66 -16.5; 72 -16.1; 79 -15.7; 87 -15.2; 96 -14.7; 106 -14.1; 116 -13.6; 128 -13.0; 141 -12.4; 155 -11.7; 170 -11.0; 187 -10.2; 206 -9.4; 227 -8.7; 249 -8.5; 274 -8.6; 302 -8.4; 332 -7.8; 365 -7.0; 402 -6.2; 442 -5.5; 486 -4.8; 535 -4.1; 588 -3.5; 647 -2.9; 712 -2.3; 783 -1.9; 861 -1.4; 947 -1.1; 1042 -0.7; 1146 -0.5; 1261 -0.5; 1387 -0.5; 1526 -0.7; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -0.6; 2457 -2.0; 2703 -3.9; 2973 -6.3; 3270 -9.0; 3597 -11.0; 3957 -12.0; 4353 -12.6; 4788 -12.7; 5267 -13.0; 5793 -16.2; 6373 -18.1; 7010 -15.4; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio TS-9005 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio TS-9005 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 52 Hz   | 0.32 | -9.3 dB  |
| Peaking | 1547 Hz | 0.54 | 8.8 dB   |
| Peaking | 6430 Hz | 0.95 | -22.4 dB |
| Peaking | 8233 Hz | 1.01 | 14.0 dB  |
| Peaking | 17 Hz   | 0.73 | -6.0 dB  |
| Peaking | 25 Hz   | 0.66 | -0.7 dB  |
| Peaking | 2478 Hz | 2.03 | 5.6 dB   |
| Peaking | 3050 Hz | 0.96 | -4.3 dB  |
| Peaking | 5261 Hz | 4.32 | 3.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.1 dB |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.0 dB  |
| Peaking | 250 Hz   | 1.41 | -1.6 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 4000 Hz  | 1.41 | -8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 16000 Hz | 1.41 | 0.8 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20TS-9005/Fischer%20Audio%20TS-9005.png)