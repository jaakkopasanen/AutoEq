# Ultimate Ears UE5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.5; 23 -6.6; 25 -6.8; 28 -7.0; 31 -7.3; 34 -7.4; 37 -7.6; 41 -7.8; 45 -8.0; 49 -8.1; 54 -8.3; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.5; 87 -9.9; 96 -10.3; 106 -10.7; 116 -11.0; 128 -11.3; 141 -11.6; 155 -11.8; 170 -11.9; 187 -12.0; 206 -11.9; 227 -11.8; 249 -11.7; 274 -11.6; 302 -11.3; 332 -10.9; 365 -10.5; 402 -10.1; 442 -9.8; 486 -9.3; 535 -8.9; 588 -8.4; 647 -7.9; 712 -7.3; 783 -6.8; 861 -6.3; 947 -6.1; 1042 -6.3; 1146 -6.8; 1261 -7.2; 1387 -7.3; 1526 -6.9; 1678 -6.2; 1846 -5.4; 2031 -4.5; 2234 -3.7; 2457 -2.6; 2703 -1.5; 2973 -0.8; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -10.4; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -12.4; 15026 -18.4; 16529 -10.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears UE5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears UE5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 121 Hz   | 0.59 | -2.8 dB  |
| Peaking | 258 Hz   | 0.63 | -3.9 dB  |
| Peaking | 4043 Hz  | 0.99 | 7.0 dB   |
| Peaking | 14944 Hz | 2.96 | -13.5 dB |
| Peaking | 22050 Hz | 1.54 | -7.4 dB  |
| Peaking | 1453 Hz  | 3.98 | -1.5 dB  |
| Peaking | 2701 Hz  | 5.42 | 1.3 dB   |
| Peaking | 6161 Hz  | 5.52 | 2.8 dB   |
| Peaking | 9078 Hz  | 4.62 | -5.0 dB  |
| Peaking | 12524 Hz | 4.75 | 2.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | -1.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -8.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20UE5/Ultimate%20Ears%20UE5.png)