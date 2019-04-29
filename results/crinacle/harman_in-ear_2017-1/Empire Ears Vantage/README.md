# Empire Ears Vantage
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -16.5; 23 -16.4; 25 -16.3; 28 -16.1; 31 -15.9; 34 -15.7; 37 -15.5; 41 -15.3; 45 -15.1; 49 -14.8; 54 -14.5; 60 -14.3; 66 -14.1; 72 -14.0; 79 -13.8; 87 -13.6; 96 -13.6; 106 -13.4; 116 -13.2; 128 -13.0; 141 -12.7; 155 -12.4; 170 -12.0; 187 -11.6; 206 -11.2; 227 -10.7; 249 -10.3; 274 -9.7; 302 -9.2; 332 -8.6; 365 -8.0; 402 -7.5; 442 -7.1; 486 -6.4; 535 -6.0; 588 -5.6; 647 -5.1; 712 -4.7; 783 -4.4; 861 -4.4; 947 -4.8; 1042 -5.6; 1146 -6.5; 1261 -7.4; 1387 -7.9; 1526 -8.0; 1678 -7.8; 1846 -7.5; 2031 -6.8; 2234 -5.5; 2457 -4.1; 2703 -2.7; 2973 -1.5; 3270 -0.6; 3597 -0.5; 3957 -2.2; 4353 -5.3; 4788 -6.8; 5267 -5.3; 5793 -2.4; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.7; 15026 -22.5; 16529 -25.9; 18182 -20.4; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Vantage GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Vantage ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.21 | -9.8 dB  |
| Peaking | 156 Hz   | 0.96 | -3.3 dB  |
| Peaking | 3320 Hz  | 2.71 | 6.2 dB   |
| Peaking | 11890 Hz | 0.51 | 13.3 dB  |
| Peaking | 16117 Hz | 0.74 | -29.2 dB |
| Peaking | 804 Hz   | 1.64 | 2.8 dB   |
| Peaking | 1549 Hz  | 1.69 | -2.7 dB  |
| Peaking | 4925 Hz  | 2.64 | -7.2 dB  |
| Peaking | 6250 Hz  | 1.28 | 10.3 dB  |
| Peaking | 7782 Hz  | 1.63 | -7.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.6 dB   |
| Peaking | 16000 Hz | 1.41 | -20.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20Vantage/Empire%20Ears%20Vantage.png)