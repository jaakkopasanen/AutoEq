# Jomo Flamenco
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -2.3; 25 -2.7; 28 -3.3; 31 -3.7; 34 -4.0; 37 -4.3; 41 -4.7; 45 -5.0; 49 -5.3; 54 -5.6; 60 -6.0; 66 -6.3; 72 -6.7; 79 -7.1; 87 -7.6; 96 -8.1; 106 -8.5; 116 -8.9; 128 -9.2; 141 -9.5; 155 -9.7; 170 -9.8; 187 -10.0; 206 -10.0; 227 -10.0; 249 -9.8; 274 -9.7; 302 -9.5; 332 -9.3; 365 -9.0; 402 -8.6; 442 -8.2; 486 -7.7; 535 -7.2; 588 -6.6; 647 -5.9; 712 -5.0; 783 -4.2; 861 -3.3; 947 -2.8; 1042 -2.8; 1146 -3.3; 1261 -3.9; 1387 -4.4; 1526 -4.5; 1678 -4.6; 1846 -4.8; 2031 -5.5; 2234 -6.1; 2457 -5.8; 2703 -4.8; 2973 -4.3; 3270 -4.9; 3597 -5.4; 3957 -3.4; 4353 -0.5; 4788 -1.4; 5267 -6.0; 5793 -5.7; 6373 -5.1; 7010 -6.6; 7711 -6.7; 8482 -6.2; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -7.3; 16529 -8.1; 18182 -6.5; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Flamenco GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Flamenco ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.31 | 5.3 dB  |
| Peaking | 210 Hz   | 0.46 | -4.0 dB |
| Peaking | 952 Hz   | 1.44 | 4.0 dB  |
| Peaking | 1739 Hz  | 0.9  | 0.6 dB  |
| Peaking | 4454 Hz  | 5.01 | 6.3 dB  |
| Peaking | 2276 Hz  | 6.57 | -1.0 dB |
| Peaking | 2898 Hz  | 6.21 | 1.3 dB  |
| Peaking | 7457 Hz  | 5.15 | -0.7 dB |
| Peaking | 16325 Hz | 2.82 | -2.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Jomo%20Flamenco/Jomo%20Flamenco.png)