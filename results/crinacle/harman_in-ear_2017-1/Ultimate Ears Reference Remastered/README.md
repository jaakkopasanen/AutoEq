# Ultimate Ears Reference Remastered
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.0; 25 -3.1; 28 -3.3; 31 -3.6; 34 -3.8; 37 -4.1; 41 -4.3; 45 -4.5; 49 -4.7; 54 -4.9; 60 -5.2; 66 -5.5; 72 -5.9; 79 -6.3; 87 -6.8; 96 -7.3; 106 -7.7; 116 -8.1; 128 -8.5; 141 -8.7; 155 -9.1; 170 -9.3; 187 -9.4; 206 -9.6; 227 -9.7; 249 -9.8; 274 -9.9; 302 -9.8; 332 -9.7; 365 -9.5; 402 -9.5; 442 -9.5; 486 -9.3; 535 -9.2; 588 -9.0; 647 -8.8; 712 -8.5; 783 -8.2; 861 -7.9; 947 -7.9; 1042 -8.1; 1146 -8.7; 1261 -9.4; 1387 -9.7; 1526 -9.3; 1678 -8.2; 1846 -6.6; 2031 -4.7; 2234 -2.9; 2457 -1.5; 2703 -0.9; 2973 -0.8; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -1.2; 4788 -4.1; 5267 -4.3; 5793 -2.5; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.8; 15026 -27.1; 16529 -36.6; 18182 -36.3; 20000 -21.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears Reference Remastered GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears Reference Remastered ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.32 | 3.8 dB   |
| Peaking | 483 Hz   | 0.14 | -3.7 dB  |
| Peaking | 3734 Hz  | 0.45 | 17.5 dB  |
| Peaking | 12153 Hz | 0.65 | 25.5 dB  |
| Peaking | 16655 Hz | 0.28 | -46.0 dB |
| Peaking | 1515 Hz  | 3.44 | -3.0 dB  |
| Peaking | 2459 Hz  | 3.5  | 2.0 dB   |
| Peaking | 4975 Hz  | 5.14 | -3.1 dB  |
| Peaking | 6390 Hz  | 6.33 | 3.6 dB   |
| Peaking | 18036 Hz | 4.87 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB   |
| Peaking | 62 Hz    | 1.41 | 1.0 dB   |
| Peaking | 125 Hz   | 1.41 | -1.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 16000 Hz | 1.41 | -33.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20Reference%20Remastered/Ultimate%20Ears%20Reference%20Remastered.png)