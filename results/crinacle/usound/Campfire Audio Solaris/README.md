# Campfire Audio Solaris
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.1; 23 -6.2; 25 -6.4; 28 -6.5; 31 -6.7; 34 -6.8; 37 -6.9; 41 -7.0; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.5; 66 -7.8; 72 -8.0; 79 -8.3; 87 -8.5; 96 -8.9; 106 -9.2; 116 -9.4; 128 -9.6; 141 -9.8; 155 -9.9; 170 -9.9; 187 -10.0; 206 -10.0; 227 -9.9; 249 -9.7; 274 -9.5; 302 -9.4; 332 -9.2; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.6; 647 -7.4; 712 -7.0; 783 -6.9; 861 -6.8; 947 -6.5; 1042 -6.2; 1146 -6.2; 1261 -6.5; 1387 -6.6; 1526 -6.6; 1678 -6.7; 1846 -7.4; 2031 -8.3; 2234 -8.0; 2457 -6.0; 2703 -3.9; 2973 -3.2; 3270 -3.8; 3597 -2.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.6; 7010 -5.1; 7711 -6.7; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.9; 15026 -8.7; 16529 -10.0; 18182 -10.2; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Campfire Audio Solaris GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Campfire Audio Solaris ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 131 Hz   | 0.78 | -2.4 dB |
| Peaking | 280 Hz   | 0.76 | -2.3 dB |
| Peaking | 2090 Hz  | 4.84 | -3.2 dB |
| Peaking | 4619 Hz  | 1.34 | 6.8 dB  |
| Peaking | 17945 Hz | 0.73 | -4.0 dB |
| Peaking | 16 Hz    | 1.28 | 0.6 dB  |
| Peaking | 4761 Hz  | 5.72 | -0.8 dB |
| Peaking | 5972 Hz  | 4.63 | 2.4 dB  |
| Peaking | 7593 Hz  | 2.9  | -2.1 dB |
| Peaking | 12951 Hz | 3.72 | 1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.6 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Campfire%20Audio%20Solaris/Campfire%20Audio%20Solaris.png)