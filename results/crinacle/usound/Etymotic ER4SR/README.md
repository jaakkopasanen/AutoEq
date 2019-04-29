# Etymotic ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.8; 49 -1.1; 54 -1.3; 60 -1.7; 66 -2.1; 72 -2.5; 79 -2.9; 87 -3.4; 96 -4.0; 106 -4.4; 116 -4.8; 128 -5.2; 141 -5.6; 155 -5.9; 170 -6.2; 187 -6.4; 206 -6.6; 227 -6.7; 249 -6.8; 274 -6.9; 302 -6.9; 332 -6.9; 365 -6.9; 402 -6.9; 442 -6.9; 486 -7.0; 535 -7.0; 588 -6.9; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.2; 947 -6.3; 1042 -6.9; 1146 -8.0; 1261 -9.3; 1387 -10.1; 1526 -10.3; 1678 -10.1; 1846 -9.9; 2031 -9.7; 2234 -9.7; 2457 -9.7; 2703 -9.4; 2973 -8.8; 3270 -8.0; 3597 -7.2; 3957 -6.3; 4353 -5.4; 4788 -4.1; 5267 -2.5; 5793 -0.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -10.7; 16529 -7.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.34 | 6.2 dB  |
| Peaking | 184 Hz   | 0.79 | -1.2 dB |
| Peaking | 1964 Hz  | 1.07 | -4.0 dB |
| Peaking | 5858 Hz  | 2.8  | 6.6 dB  |
| Peaking | 15332 Hz | 4.3  | -5.0 dB |
| Peaking | 936 Hz   | 2.94 | 1.4 dB  |
| Peaking | 1390 Hz  | 2.63 | -2.0 dB |
| Peaking | 2470 Hz  | 0.92 | 2.0 dB  |
| Peaking | 2812 Hz  | 1.98 | -2.4 dB |
| Peaking | 8000 Hz  | 4.69 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | 0.7 dB  |
| Peaking | 250 Hz   | 1.41 | -0.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Etymotic%20ER4SR/Etymotic%20ER4SR.png)