# Empire Ears EVR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.6; 25 -3.9; 28 -4.3; 31 -4.6; 34 -4.9; 37 -5.1; 41 -5.4; 45 -5.6; 49 -5.8; 54 -6.1; 60 -6.5; 66 -6.8; 72 -7.2; 79 -7.5; 87 -8.0; 96 -8.5; 106 -8.9; 116 -9.3; 128 -9.6; 141 -10.0; 155 -10.3; 170 -10.5; 187 -10.6; 206 -10.7; 227 -10.7; 249 -10.8; 274 -10.7; 302 -10.6; 332 -10.3; 365 -10.1; 402 -9.9; 442 -9.7; 486 -9.5; 535 -9.2; 588 -8.8; 647 -8.5; 712 -8.1; 783 -7.6; 861 -7.4; 947 -7.4; 1042 -7.8; 1146 -8.5; 1261 -9.1; 1387 -9.2; 1526 -8.8; 1678 -8.3; 1846 -7.4; 2031 -5.5; 2234 -3.2; 2457 -0.8; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.1; 7010 -5.7; 7711 -8.8; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.0; 15026 -14.9; 16529 -17.3; 18182 -17.8; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears EVR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears EVR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 11 Hz    | 0.24 | 3.5 dB   |
| Peaking | 231 Hz   | 0.43 | -4.5 dB  |
| Peaking | 1582 Hz  | 1.46 | -6.3 dB  |
| Peaking | 3197 Hz  | 0.61 | 8.0 dB   |
| Peaking | 18299 Hz | 0.66 | -12.8 dB |
| Peaking | 3579 Hz  | 4.47 | -1.0 dB  |
| Peaking | 5937 Hz  | 3.14 | 3.1 dB   |
| Peaking | 7776 Hz  | 3.32 | -5.1 dB  |
| Peaking | 13418 Hz | 1.59 | 5.3 dB   |
| Peaking | 15052 Hz | 2.22 | -5.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB   |
| Peaking | 62 Hz    | 1.41 | 0.0 dB   |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -11.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Empire%20Ears%20EVR/Empire%20Ears%20EVR.png)