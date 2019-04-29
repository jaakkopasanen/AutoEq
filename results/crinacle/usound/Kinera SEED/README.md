# Kinera SEED
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.2; 54 -2.1; 60 -3.0; 66 -3.9; 72 -4.8; 79 -5.6; 87 -6.5; 96 -7.3; 106 -8.0; 116 -8.7; 128 -9.2; 141 -9.7; 155 -10.0; 170 -10.2; 187 -10.2; 206 -10.2; 227 -10.1; 249 -9.9; 274 -9.7; 302 -9.3; 332 -8.9; 365 -8.5; 402 -8.1; 442 -7.6; 486 -7.1; 535 -6.5; 588 -6.0; 647 -5.5; 712 -4.9; 783 -4.5; 861 -4.3; 947 -4.3; 1042 -4.8; 1146 -5.7; 1261 -6.7; 1387 -7.5; 1526 -7.9; 1678 -7.8; 1846 -7.2; 2031 -5.9; 2234 -4.2; 2457 -2.7; 2703 -2.2; 2973 -4.3; 3270 -8.7; 3597 -8.7; 3957 -8.3; 4353 -8.8; 4788 -8.0; 5267 -6.7; 5793 -4.1; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera SEED GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera SEED ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.59 | 6.9 dB  |
| Peaking | 169 Hz  | 0.82 | -4.8 dB |
| Peaking | 2673 Hz | 3.11 | 7.5 dB  |
| Peaking | 3458 Hz | 1.37 | -4.3 dB |
| Peaking | 6363 Hz | 4.84 | 6.2 dB  |
| Peaking | 100 Hz  | 2.49 | -0.5 dB |
| Peaking | 173 Hz  | 1.81 | 0.8 dB  |
| Peaking | 333 Hz  | 0.86 | -1.2 dB |
| Peaking | 894 Hz  | 0.98 | 3.2 dB  |
| Peaking | 1488 Hz | 2.16 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.4 dB |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Kinera%20SEED/Kinera%20SEED.png)