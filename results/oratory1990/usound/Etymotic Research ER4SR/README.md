# Etymotic Research ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.1; 96 -1.6; 106 -2.1; 116 -2.6; 128 -3.0; 141 -3.4; 155 -3.7; 170 -4.0; 187 -4.2; 206 -4.4; 227 -4.5; 249 -4.7; 274 -4.9; 302 -4.9; 332 -5.0; 365 -5.1; 402 -5.1; 442 -5.2; 486 -5.3; 535 -5.4; 588 -5.6; 647 -5.6; 712 -5.5; 783 -5.5; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.5; 1261 -8.3; 1387 -9.2; 1526 -9.6; 1678 -9.7; 1846 -9.7; 2031 -9.9; 2234 -10.1; 2457 -10.3; 2703 -10.0; 2973 -9.2; 3270 -8.4; 3597 -7.7; 3957 -7.2; 4353 -6.5; 4788 -5.5; 5267 -3.8; 5793 -1.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.3  | 6.4 dB  |
| Peaking | 844 Hz   | 0.74 | 2.3 dB  |
| Peaking | 1877 Hz  | 0.71 | -4.6 dB |
| Peaking | 6020 Hz  | 3.14 | 6.7 dB  |
| Peaking | 14965 Hz | 5.45 | -2.1 dB |
| Peaking | 154 Hz   | 3.91 | -0.3 dB |
| Peaking | 2684 Hz  | 3.58 | -1.3 dB |
| Peaking | 2952 Hz  | 1.15 | 0.7 dB  |
| Peaking | 7927 Hz  | 5.39 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.1 dB  |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)