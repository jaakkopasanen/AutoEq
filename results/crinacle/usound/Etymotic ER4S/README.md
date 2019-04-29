# Etymotic ER4S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -0.9; 60 -1.3; 66 -1.7; 72 -2.0; 79 -2.4; 87 -2.9; 96 -3.5; 106 -3.9; 116 -4.3; 128 -4.7; 141 -5.1; 155 -5.5; 170 -5.7; 187 -6.0; 206 -6.1; 227 -6.2; 249 -6.4; 274 -6.4; 302 -6.5; 332 -6.5; 365 -6.5; 402 -6.5; 442 -6.6; 486 -6.6; 535 -6.5; 588 -6.4; 647 -6.3; 712 -6.2; 783 -6.0; 861 -5.9; 947 -6.1; 1042 -6.6; 1146 -7.7; 1261 -8.9; 1387 -9.8; 1526 -10.1; 1678 -10.1; 1846 -10.0; 2031 -10.1; 2234 -10.3; 2457 -10.5; 2703 -10.3; 2973 -9.5; 3270 -8.5; 3597 -7.4; 3957 -6.3; 4353 -5.4; 4788 -4.3; 5267 -3.1; 5793 -2.0; 6373 -1.5; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -12.0; 16529 -9.0; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.44 | 6.5 dB  |
| Peaking | 916 Hz   | 1.06 | 4.9 dB  |
| Peaking | 1519 Hz  | 0.48 | -5.8 dB |
| Peaking | 5699 Hz  | 1.86 | 6.1 dB  |
| Peaking | 15443 Hz | 3.47 | -6.5 dB |
| Peaking | 2758 Hz  | 2.99 | -1.9 dB |
| Peaking | 3048 Hz  | 1.42 | 1.2 dB  |
| Peaking | 8054 Hz  | 5.43 | -1.3 dB |
| Peaking | 12352 Hz | 4.38 | 0.2 dB  |
| Peaking | 13144 Hz | 7.39 | 0.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Etymotic%20ER4S/Etymotic%20ER4S.png)