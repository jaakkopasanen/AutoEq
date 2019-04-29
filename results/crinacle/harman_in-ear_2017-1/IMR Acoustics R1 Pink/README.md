# IMR Acoustics R1 Pink
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.6; 25 -5.8; 28 -6.1; 31 -6.2; 34 -6.3; 37 -6.5; 41 -6.7; 45 -6.9; 49 -7.0; 54 -7.1; 60 -7.3; 66 -7.6; 72 -7.9; 79 -8.2; 87 -8.5; 96 -9.0; 106 -9.4; 116 -9.7; 128 -9.9; 141 -10.1; 155 -10.2; 170 -10.3; 187 -10.3; 206 -10.4; 227 -10.1; 249 -9.9; 274 -9.7; 302 -9.3; 332 -8.8; 365 -8.3; 402 -7.8; 442 -7.3; 486 -6.7; 535 -6.1; 588 -5.6; 647 -4.9; 712 -4.1; 783 -3.5; 861 -3.1; 947 -2.8; 1042 -2.9; 1146 -3.4; 1261 -3.7; 1387 -3.7; 1526 -3.6; 1678 -3.4; 1846 -3.5; 2031 -3.8; 2234 -4.3; 2457 -5.5; 2703 -6.5; 2973 -6.2; 3270 -4.8; 3597 -4.5; 3957 -5.5; 4353 -7.8; 4788 -8.6; 5267 -5.2; 5793 -0.9; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -9.7; 13660 -16.8; 15026 -24.2; 16529 -29.3; 18182 -29.8; 20000 -24.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Pink GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Pink ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 187 Hz   | 0.52 | -4.6 dB  |
| Peaking | 908 Hz   | 1.13 | 3.8 dB   |
| Peaking | 1801 Hz  | 2.81 | 2.0 dB   |
| Peaking | 10012 Hz | 0.38 | 20.9 dB  |
| Peaking | 16881 Hz | 0.28 | -35.5 dB |
| Peaking | 3627 Hz  | 4.98 | 2.2 dB   |
| Peaking | 4747 Hz  | 4.45 | -4.2 dB  |
| Peaking | 6123 Hz  | 3.16 | 7.7 dB   |
| Peaking | 10019 Hz | 0.67 | -4.2 dB  |
| Peaking | 11615 Hz | 2.33 | 6.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB   |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -3.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 8.4 dB   |
| Peaking | 16000 Hz | 1.41 | -30.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/IMR%20Acoustics%20R1%20Pink/IMR%20Acoustics%20R1%20Pink.png)