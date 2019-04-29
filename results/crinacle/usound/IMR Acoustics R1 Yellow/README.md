# IMR Acoustics R1 Yellow
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.4; 23 -14.4; 25 -14.3; 28 -14.3; 31 -14.2; 34 -14.1; 37 -14.1; 41 -13.9; 45 -13.8; 49 -13.6; 54 -13.4; 60 -13.2; 66 -13.0; 72 -12.9; 79 -12.8; 87 -12.7; 96 -12.5; 106 -12.4; 116 -12.2; 128 -12.0; 141 -11.8; 155 -11.4; 170 -11.0; 187 -10.5; 206 -10.1; 227 -9.5; 249 -8.9; 274 -8.3; 302 -7.8; 332 -7.2; 365 -6.5; 402 -6.0; 442 -5.4; 486 -4.8; 535 -4.3; 588 -3.8; 647 -3.1; 712 -2.4; 783 -1.9; 861 -1.4; 947 -1.2; 1042 -1.3; 1146 -1.9; 1261 -2.4; 1387 -2.7; 1526 -2.8; 1678 -2.8; 1846 -3.0; 2031 -3.6; 2234 -4.9; 2457 -6.8; 2703 -8.5; 2973 -8.7; 3270 -7.3; 3597 -6.5; 3957 -7.1; 4353 -8.9; 4788 -9.5; 5267 -5.9; 5793 -1.9; 6373 -0.5; 7010 -3.4; 7711 -5.8; 8482 -6.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -7.1; 13660 -7.8; 15026 -7.6; 16529 -10.6; 18182 -13.6; 20000 -10.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Yellow GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Yellow ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.25 | -8.2 dB |
| Peaking | 148 Hz   | 0.7  | -3.4 dB |
| Peaking | 930 Hz   | 0.99 | 5.2 dB  |
| Peaking | 18550 Hz | 1.02 | -8.3 dB |
| Peaking | 22050 Hz | 1.75 | 3.5 dB  |
| Peaking | 1893 Hz  | 2.89 | 1.9 dB  |
| Peaking | 2804 Hz  | 3.58 | -3.9 dB |
| Peaking | 4671 Hz  | 4.62 | -4.9 dB |
| Peaking | 6176 Hz  | 4.24 | 6.6 dB  |
| Peaking | 17142 Hz | 5.65 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/IMR%20Acoustics%20R1%20Yellow/IMR%20Acoustics%20R1%20Yellow.png)