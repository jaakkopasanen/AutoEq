# IMR Acoustics R1 Black
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.9; 28 -13.8; 31 -13.7; 34 -13.6; 37 -13.5; 41 -13.4; 45 -13.2; 49 -13.1; 54 -12.9; 60 -12.8; 66 -12.7; 72 -12.6; 79 -12.5; 87 -12.3; 96 -12.2; 106 -12.1; 116 -11.9; 128 -11.7; 141 -11.5; 155 -11.1; 170 -10.7; 187 -10.2; 206 -9.7; 227 -9.2; 249 -8.6; 274 -8.0; 302 -7.5; 332 -6.9; 365 -6.3; 402 -5.7; 442 -5.1; 486 -4.6; 535 -4.0; 588 -3.5; 647 -2.8; 712 -2.1; 783 -1.6; 861 -1.1; 947 -0.9; 1042 -1.0; 1146 -1.5; 1261 -2.1; 1387 -2.4; 1526 -2.5; 1678 -2.5; 1846 -2.7; 2031 -3.4; 2234 -4.9; 2457 -7.2; 2703 -9.6; 2973 -10.1; 3270 -8.3; 3597 -7.2; 3957 -7.5; 4353 -9.3; 4788 -9.9; 5267 -6.2; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -6.4; 8482 -7.2; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -7.5; 13660 -7.1; 15026 -6.9; 16529 -11.2; 18182 -14.0; 20000 -7.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Black GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Black ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.25 | -7.8 dB |
| Peaking | 145 Hz   | 0.75 | -3.2 dB |
| Peaking | 925 Hz   | 1.05 | 5.5 dB  |
| Peaking | 14978 Hz | 2.26 | 1.9 dB  |
| Peaking | 17874 Hz | 1.09 | -8.7 dB |
| Peaking | 1893 Hz  | 2.54 | 2.4 dB  |
| Peaking | 2837 Hz  | 3.34 | -5.4 dB |
| Peaking | 4729 Hz  | 3.76 | -6.0 dB |
| Peaking | 6187 Hz  | 2.76 | 6.8 dB  |
| Peaking | 8012 Hz  | 5.9  | -3.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.0 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.6 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/IMR%20Acoustics%20R1%20Black/IMR%20Acoustics%20R1%20Black.png)