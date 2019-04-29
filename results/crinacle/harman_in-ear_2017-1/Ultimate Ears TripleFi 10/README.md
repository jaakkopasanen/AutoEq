# Ultimate Ears TripleFi 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.1; 23 -7.3; 25 -7.5; 28 -7.7; 31 -7.9; 34 -8.0; 37 -8.1; 41 -8.3; 45 -8.5; 49 -8.7; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.1; 87 -10.5; 96 -10.8; 106 -11.2; 116 -11.5; 128 -11.7; 141 -12.0; 155 -12.1; 170 -12.2; 187 -12.2; 206 -12.1; 227 -12.0; 249 -11.8; 274 -11.6; 302 -11.3; 332 -10.9; 365 -10.5; 402 -10.1; 442 -9.9; 486 -9.5; 535 -9.1; 588 -8.7; 647 -8.4; 712 -7.9; 783 -7.5; 861 -7.1; 947 -7.0; 1042 -7.1; 1146 -7.5; 1261 -7.7; 1387 -7.4; 1526 -6.5; 1678 -5.4; 1846 -4.2; 2031 -2.8; 2234 -1.7; 2457 -0.9; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -2.0; 6373 -5.3; 7010 -6.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.9; 12418 -10.4; 13660 -18.4; 15026 -26.6; 16529 -23.7; 18182 -11.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears TripleFi 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears TripleFi 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 114 Hz   | 0.04 | -0.4 dB  |
| Peaking | 191 Hz   | 0.4  | -5.3 dB  |
| Peaking | 1417 Hz  | 1.53 | -4.3 dB  |
| Peaking | 3082 Hz  | 0.46 | 7.4 dB   |
| Peaking | 15550 Hz | 1.83 | -23.4 dB |
| Peaking | 5528 Hz  | 3.27 | 3.0 dB   |
| Peaking | 6626 Hz  | 2.77 | -3.9 dB  |
| Peaking | 11477 Hz | 2.53 | 3.8 dB   |
| Peaking | 14251 Hz | 4.59 | -4.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -20.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20TripleFi%2010/Ultimate%20Ears%20TripleFi%2010.png)