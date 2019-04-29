# Etymotic ER4S custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.2; 72 -1.7; 79 -2.2; 87 -2.7; 96 -3.3; 106 -3.8; 116 -4.3; 128 -4.7; 141 -5.1; 155 -5.5; 170 -5.7; 187 -6.0; 206 -6.2; 227 -6.4; 249 -6.4; 274 -6.5; 302 -6.6; 332 -6.7; 365 -6.7; 402 -6.7; 442 -6.7; 486 -6.7; 535 -6.8; 588 -6.7; 647 -6.6; 712 -6.5; 783 -6.4; 861 -6.3; 947 -6.6; 1042 -7.3; 1146 -8.5; 1261 -9.9; 1387 -11.0; 1526 -11.6; 1678 -11.8; 1846 -12.0; 2031 -12.3; 2234 -12.3; 2457 -11.6; 2703 -10.2; 2973 -8.7; 3270 -7.5; 3597 -6.9; 3957 -6.9; 4353 -7.2; 4788 -6.9; 5267 -4.7; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -8.1; 13660 -14.0; 15026 -15.9; 16529 -8.1; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4S custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4S custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.5  | 6.7 dB   |
| Peaking | 1931 Hz  | 1.35 | -6.4 dB  |
| Peaking | 4837 Hz  | 5.52 | -1.3 dB  |
| Peaking | 6103 Hz  | 3.27 | 6.7 dB   |
| Peaking | 14637 Hz | 2.87 | -11.0 dB |
| Peaking | 909 Hz   | 2.99 | 1.3 dB   |
| Peaking | 1350 Hz  | 5.47 | -1.4 dB  |
| Peaking | 2513 Hz  | 6.72 | -1.0 dB  |
| Peaking | 3423 Hz  | 4.6  | 0.9 dB   |
| Peaking | 11731 Hz | 6.26 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 4.7 dB  |
| Peaking | 125 Hz   | 1.41 | 1.0 dB  |
| Peaking | 250 Hz   | 1.41 | -0.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -7.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 16000 Hz | 1.41 | -7.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Etymotic%20ER4S%20custom/Etymotic%20ER4S%20custom.png)