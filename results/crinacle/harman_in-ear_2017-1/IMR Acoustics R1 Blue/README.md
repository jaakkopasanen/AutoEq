# IMR Acoustics R1 Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.1; 28 -1.4; 31 -1.6; 34 -1.8; 37 -1.9; 41 -2.2; 45 -2.4; 49 -2.6; 54 -2.8; 60 -3.0; 66 -3.4; 72 -3.8; 79 -4.1; 87 -4.6; 96 -5.2; 106 -5.6; 116 -6.1; 128 -6.5; 141 -6.9; 155 -7.2; 170 -7.6; 187 -7.8; 206 -8.1; 227 -8.3; 249 -8.4; 274 -8.5; 302 -8.5; 332 -8.2; 365 -8.0; 402 -7.8; 442 -7.5; 486 -7.1; 535 -6.6; 588 -6.1; 647 -5.4; 712 -4.7; 783 -4.0; 861 -3.5; 947 -3.1; 1042 -3.1; 1146 -3.5; 1261 -3.8; 1387 -3.9; 1526 -3.6; 1678 -3.4; 1846 -3.3; 2031 -3.4; 2234 -3.9; 2457 -5.3; 2703 -7.5; 2973 -8.9; 3270 -7.9; 3597 -7.0; 3957 -7.4; 4353 -9.4; 4788 -10.7; 5267 -7.3; 5793 -2.6; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -7.3; 9330 -6.1; 10263 -5.9; 11289 -6.1; 12418 -11.5; 13660 -18.8; 15026 -25.4; 16529 -31.0; 18182 -31.9; 20000 -23.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 1.22 | 5.2 dB   |
| Peaking | 53 Hz    | 2.07 | 2.6 dB   |
| Peaking | 4113 Hz  | 1.2  | -8.2 dB  |
| Peaking | 8115 Hz  | 0.32 | 19.4 dB  |
| Peaking | 17114 Hz | 0.34 | -35.8 dB |
| Peaking | 272 Hz   | 1.11 | -3.1 dB  |
| Peaking | 4896 Hz  | 9.46 | -3.1 dB  |
| Peaking | 6166 Hz  | 4.31 | 5.7 dB   |
| Peaking | 10704 Hz | 0.85 | -6.3 dB  |
| Peaking | 11346 Hz | 2.37 | 10.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.9 dB   |
| Peaking | 62 Hz    | 1.41 | 2.2 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.8 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 9.8 dB   |
| Peaking | 16000 Hz | 1.41 | -33.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/IMR%20Acoustics%20R1%20Blue/IMR%20Acoustics%20R1%20Blue.png)