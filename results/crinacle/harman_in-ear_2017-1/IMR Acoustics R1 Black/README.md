# IMR Acoustics R1 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.1; 23 -15.1; 25 -15.1; 28 -15.0; 31 -14.9; 34 -14.8; 37 -14.7; 41 -14.6; 45 -14.4; 49 -14.3; 54 -14.1; 60 -14.0; 66 -13.9; 72 -13.8; 79 -13.7; 87 -13.5; 96 -13.4; 106 -13.3; 116 -13.1; 128 -12.9; 141 -12.7; 155 -12.3; 170 -11.9; 187 -11.4; 206 -10.9; 227 -10.4; 249 -9.8; 274 -9.2; 302 -8.6; 332 -7.9; 365 -7.2; 402 -6.6; 442 -6.0; 486 -5.4; 535 -4.7; 588 -4.2; 647 -3.5; 712 -2.8; 783 -2.3; 861 -1.9; 947 -1.7; 1042 -1.9; 1146 -2.3; 1261 -2.6; 1387 -2.6; 1526 -2.5; 1678 -2.4; 1846 -2.5; 2031 -2.9; 2234 -3.7; 2457 -5.5; 2703 -7.5; 2973 -7.9; 3270 -6.1; 3597 -5.3; 3957 -6.0; 4353 -8.2; 4788 -9.1; 5267 -5.3; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -10.1; 13660 -16.0; 15026 -23.3; 16529 -30.1; 18182 -30.5; 20000 -19.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.27 | -8.7 dB  |
| Peaking | 149 Hz   | 0.53 | -4.6 dB  |
| Peaking | 997 Hz   | 0.71 | 4.9 dB   |
| Peaking | 10181 Hz | 0.52 | 16.6 dB  |
| Peaking | 17019 Hz | 0.4  | -32.6 dB |
| Peaking | 1981 Hz  | 3.41 | 1.7 dB   |
| Peaking | 2806 Hz  | 5.27 | -3.4 dB  |
| Peaking | 4780 Hz  | 4.75 | -5.7 dB  |
| Peaking | 6125 Hz  | 2.8  | 6.6 dB   |
| Peaking | 8070 Hz  | 2.67 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.5 dB  |
| Peaking | 62 Hz    | 1.41 | -5.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 16000 Hz | 1.41 | -29.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/IMR%20Acoustics%20R1%20Black/IMR%20Acoustics%20R1%20Black.png)