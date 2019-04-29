# IMR Acoustics R1 Blue
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -0.9; 31 -1.1; 34 -1.2; 37 -1.4; 41 -1.6; 45 -1.8; 49 -2.0; 54 -2.2; 60 -2.5; 66 -2.9; 72 -3.2; 79 -3.6; 87 -4.0; 96 -4.6; 106 -5.1; 116 -5.5; 128 -6.0; 141 -6.3; 155 -6.7; 170 -7.0; 187 -7.3; 206 -7.5; 227 -7.7; 249 -7.8; 274 -7.9; 302 -8.0; 332 -7.9; 365 -7.7; 402 -7.6; 442 -7.3; 486 -6.9; 535 -6.5; 588 -6.0; 647 -5.3; 712 -4.6; 783 -3.9; 861 -3.4; 947 -2.9; 1042 -2.9; 1146 -3.4; 1261 -3.9; 1387 -4.3; 1526 -4.3; 1678 -4.1; 1846 -4.1; 2031 -4.5; 2234 -5.6; 2457 -7.6; 2703 -10.2; 2973 -11.7; 3270 -10.7; 3597 -9.6; 3957 -9.6; 4353 -11.2; 4788 -12.1; 5267 -8.7; 5793 -4.3; 6373 -2.0; 7010 -4.0; 7711 -7.6; 8482 -9.6; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -9.5; 13660 -10.5; 15026 -9.7; 16529 -12.8; 18182 -16.0; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`IMR Acoustics R1 Blue GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `IMR Acoustics R1 Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.85 | 5.9 dB  |
| Peaking | 60 Hz    | 1.54 | 2.8 dB  |
| Peaking | 3572 Hz  | 2.21 | -4.6 dB |
| Peaking | 18079 Hz | 0.95 | -9.1 dB |
| Peaking | 19671 Hz | 2.03 | -3.4 dB |
| Peaking | 970 Hz   | 2.38 | 3.3 dB  |
| Peaking | 2441 Hz  | 0.95 | 3.9 dB  |
| Peaking | 2786 Hz  | 3.47 | -6.4 dB |
| Peaking | 4763 Hz  | 5.43 | -5.8 dB |
| Peaking | 6345 Hz  | 5.48 | 5.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.2 dB |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -8.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/IMR%20Acoustics%20R1%20Blue/IMR%20Acoustics%20R1%20Blue.png)