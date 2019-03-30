# Sony XBA-4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.8; 23 -17.0; 25 -17.0; 28 -17.0; 31 -16.9; 34 -16.7; 37 -16.6; 41 -16.5; 45 -16.3; 49 -16.1; 54 -15.8; 60 -15.4; 66 -15.1; 72 -14.7; 79 -14.4; 87 -13.9; 96 -13.5; 106 -13.1; 116 -12.8; 128 -12.5; 141 -12.1; 155 -11.8; 170 -11.5; 187 -11.1; 206 -10.8; 227 -10.4; 249 -9.9; 274 -9.5; 302 -9.0; 332 -8.6; 365 -8.1; 402 -7.7; 442 -7.4; 486 -7.0; 535 -6.6; 588 -6.2; 647 -5.9; 712 -5.5; 783 -5.2; 861 -4.8; 947 -4.5; 1042 -4.2; 1146 -3.9; 1261 -3.6; 1387 -3.5; 1526 -3.5; 1678 -3.6; 1846 -3.9; 2031 -4.5; 2234 -5.8; 2457 -7.3; 2703 -9.1; 2973 -10.9; 3270 -12.1; 3597 -12.0; 3957 -10.4; 4353 -7.9; 4788 -5.5; 5267 -2.9; 5793 -0.5; 6373 -0.9; 7010 -3.8; 7711 -6.0; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -9.2; 15026 -7.8; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.1  | -10.3 dB |
| Peaking | 1667 Hz  | 0.69 | 4.2 dB   |
| Peaking | 3335 Hz  | 1.6  | -8.5 dB  |
| Peaking | 5857 Hz  | 2.89 | 7.5 dB   |
| Peaking | 14035 Hz | 4.14 | -3.5 dB  |
| Peaking | 30 Hz    | 0.96 | -0.5 dB  |
| Peaking | 95 Hz    | 1.31 | 0.6 dB   |
| Peaking | 236 Hz   | 1.54 | -0.5 dB  |
| Peaking | 7946 Hz  | 6.37 | -1.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.4 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.7 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 16000 Hz | 1.41 | -1.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XBA-4/Sony%20XBA-4.png)