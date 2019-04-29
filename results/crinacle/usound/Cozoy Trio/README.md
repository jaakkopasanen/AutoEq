# Cozoy Trio
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -3.0; 25 -3.2; 28 -3.5; 31 -3.8; 34 -4.0; 37 -4.2; 41 -4.5; 45 -4.8; 49 -5.0; 54 -5.3; 60 -5.6; 66 -6.0; 72 -6.3; 79 -6.7; 87 -7.1; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.7; 141 -9.0; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.2; 227 -9.1; 249 -8.9; 274 -8.6; 302 -8.1; 332 -7.6; 365 -7.0; 402 -6.2; 442 -5.5; 486 -4.7; 535 -3.9; 588 -3.1; 647 -2.2; 712 -1.3; 783 -0.6; 861 -0.5; 947 -2.0; 1042 -3.7; 1146 -5.0; 1261 -6.6; 1387 -7.9; 1526 -8.4; 1678 -7.9; 1846 -6.6; 2031 -4.9; 2234 -3.6; 2457 -3.0; 2703 -3.0; 2973 -3.8; 3270 -4.7; 3597 -4.3; 3957 -3.3; 4353 -2.4; 4788 -1.5; 5267 -3.6; 5793 -7.5; 6373 -9.3; 7010 -11.6; 7711 -9.3; 8482 -5.5; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cozoy Trio GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cozoy Trio ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.39 | 3.5 dB  |
| Peaking | 176 Hz  | 0.69 | -4.1 dB |
| Peaking | 752 Hz  | 2.23 | 5.9 dB  |
| Peaking | 4652 Hz | 1.96 | 4.4 dB  |
| Peaking | 6820 Hz | 3.27 | -7.2 dB |
| Peaking | 510 Hz  | 4.48 | 1.0 dB  |
| Peaking | 928 Hz  | 5.22 | 1.8 dB  |
| Peaking | 1525 Hz | 2.33 | -3.8 dB |
| Peaking | 2416 Hz | 3.35 | 3.0 dB  |
| Peaking | 8529 Hz | 7.72 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Cozoy%20Trio/Cozoy%20Trio.png)