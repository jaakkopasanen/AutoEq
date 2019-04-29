# Daiso $2 earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.6; 25 -4.7; 28 -4.9; 31 -5.1; 34 -5.2; 37 -5.3; 41 -5.5; 45 -5.7; 49 -5.9; 54 -6.1; 60 -6.4; 66 -6.7; 72 -7.1; 79 -7.5; 87 -8.0; 96 -8.4; 106 -8.9; 116 -9.4; 128 -9.8; 141 -10.3; 155 -10.7; 170 -11.0; 187 -11.3; 206 -11.5; 227 -11.8; 249 -12.1; 274 -12.3; 302 -12.6; 332 -12.9; 365 -13.4; 402 -13.8; 442 -14.3; 486 -14.9; 535 -15.6; 588 -16.4; 647 -17.3; 712 -18.0; 783 -17.9; 861 -16.6; 947 -14.3; 1042 -11.7; 1146 -9.0; 1261 -8.5; 1387 -8.4; 1526 -5.4; 1678 -2.4; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.6; 5793 -6.8; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Daiso $2 earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Daiso $2 earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.36 | 2.1 dB   |
| Peaking | 747 Hz  | 0.51 | -26.2 dB |
| Peaking | 755 Hz  | 0.49 | 12.2 dB  |
| Peaking | 2025 Hz | 0.93 | 11.3 dB  |
| Peaking | 4130 Hz | 1.23 | 6.4 dB   |
| Peaking | 1171 Hz | 7.64 | 1.8 dB   |
| Peaking | 1358 Hz | 7.79 | -2.3 dB  |
| Peaking | 5771 Hz | 7.25 | -6.8 dB  |
| Peaking | 6475 Hz | 2.71 | 6.2 dB   |
| Peaking | 7464 Hz | 2.38 | -3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -8.5 dB |
| Peaking | 1000 Hz  | 1.41 | -7.9 dB |
| Peaking | 2000 Hz  | 1.41 | 7.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Daiso%20$2%20earphones/Daiso%20$2%20earphones.png)