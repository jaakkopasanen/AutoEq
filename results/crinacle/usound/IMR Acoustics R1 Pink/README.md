# IMR Acoustics R1 Pink
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.4; 25 -4.6; 28 -4.9; 31 -5.0; 34 -5.1; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.8; 54 -5.9; 60 -6.1; 66 -6.5; 72 -6.7; 79 -7.0; 87 -7.4; 96 -7.9; 106 -8.2; 116 -8.5; 128 -8.7; 141 -8.9; 155 -9.0; 170 -9.2; 187 -9.1; 206 -9.2; 227 -8.9; 249 -8.7; 274 -8.5; 302 -8.2; 332 -7.8; 365 -7.4; 402 -7.0; 442 -6.4; 486 -5.9; 535 -5.4; 588 -4.9; 647 -4.2; 712 -3.4; 783 -2.8; 861 -2.3; 947 -2.0; 1042 -2.1; 1146 -2.6; 1261 -3.2; 1387 -3.5; 1526 -3.6; 1678 -3.6; 1846 -3.7; 2031 -4.3; 2234 -5.5; 2457 -7.2; 2703 -8.6; 2973 -8.5; 3270 -7.1; 3597 -6.5; 3957 -7.1; 4353 -8.9; 4788 -9.5; 5267 -6.0; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -7.4; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -7.2; 13660 -7.9; 15026 -7.9; 16529 -10.4; 18182 -13.3; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Pink GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Pink ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 200 Hz   | 0.65 | -3.6 dB |
| Peaking | 997 Hz   | 0.91 | 4.3 dB  |
| Peaking | 4974 Hz  | 1.13 | -5.0 dB |
| Peaking | 6165 Hz  | 3.12 | 9.8 dB  |
| Peaking | 18913 Hz | 0.82 | -8.3 dB |
| Peaking | 20 Hz    | 0.82 | 1.8 dB  |
| Peaking | 2041 Hz  | 2.22 | 3.3 dB  |
| Peaking | 2763 Hz  | 1.27 | -4.2 dB |
| Peaking | 3573 Hz  | 3.23 | 4.1 dB  |
| Peaking | 10874 Hz | 3.85 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -5.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/IMR%20Acoustics%20R1%20Pink/IMR%20Acoustics%20R1%20Pink.png)