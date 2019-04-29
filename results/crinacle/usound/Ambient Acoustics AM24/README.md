# Ambient Acoustics AM24
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.4; 25 -4.7; 28 -5.1; 31 -5.4; 34 -5.6; 37 -5.7; 41 -6.0; 45 -6.2; 49 -6.4; 54 -6.6; 60 -6.8; 66 -7.0; 72 -7.3; 79 -7.5; 87 -7.9; 96 -8.2; 106 -8.5; 116 -8.8; 128 -9.0; 141 -9.2; 155 -9.3; 170 -9.4; 187 -9.5; 206 -9.5; 227 -9.5; 249 -9.3; 274 -9.3; 302 -9.2; 332 -9.1; 365 -8.9; 402 -8.7; 442 -8.5; 486 -8.3; 535 -8.1; 588 -7.9; 647 -7.6; 712 -7.3; 783 -7.0; 861 -6.8; 947 -6.9; 1042 -7.3; 1146 -8.1; 1261 -9.1; 1387 -9.9; 1526 -9.7; 1678 -8.7; 1846 -6.9; 2031 -4.6; 2234 -2.6; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -2.8; 3957 -4.1; 4353 -1.1; 4788 -0.5; 5267 -0.5; 5793 -1.8; 6373 -10.2; 7010 -12.8; 7711 -10.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.8; 16529 -9.5; 18182 -8.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM24 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM24 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 218 Hz   | 0.57 | -3.2 dB  |
| Peaking | 1507 Hz  | 2.34 | -4.7 dB  |
| Peaking | 2686 Hz  | 1.73 | 6.5 dB   |
| Peaking | 5416 Hz  | 2.29 | 8.4 dB   |
| Peaking | 6775 Hz  | 3.62 | -10.9 dB |
| Peaking | 19 Hz    | 1.05 | 2.6 dB   |
| Peaking | 835 Hz   | 1.11 | -0.9 dB  |
| Peaking | 868 Hz   | 2.29 | 1.5 dB   |
| Peaking | 15438 Hz | 0.71 | 0.9 dB   |
| Peaking | 16862 Hz | 1.66 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | -1.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Ambient%20Acoustics%20AM24/Ambient%20Acoustics%20AM24.png)