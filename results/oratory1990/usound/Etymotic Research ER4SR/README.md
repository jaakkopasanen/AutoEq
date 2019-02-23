# Etymotic Research ER4SR
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.8; 72 -1.2; 79 -1.6; 87 -2.1; 96 -2.6; 106 -3.1; 116 -3.6; 128 -4.0; 141 -4.4; 155 -4.7; 170 -5.0; 187 -5.2; 206 -5.4; 227 -5.5; 249 -5.7; 274 -5.9; 302 -5.9; 332 -6.0; 365 -6.1; 402 -6.1; 442 -6.2; 486 -6.3; 535 -6.4; 588 -6.6; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.7; 947 -7.2; 1042 -7.8; 1146 -8.5; 1261 -9.3; 1387 -10.2; 1526 -10.6; 1678 -10.7; 1846 -10.7; 2031 -10.9; 2234 -11.1; 2457 -11.3; 2703 -11.0; 2973 -10.2; 3270 -9.4; 3597 -8.7; 3957 -8.2; 4353 -7.5; 4788 -6.5; 5267 -4.8; 5793 -2.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -9.5; 16529 -6.6; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic Research ER4SR GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic Research ER4SR ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.37 | 6.4 dB  |
| Peaking | 2181 Hz  | 0.91 | -5.1 dB |
| Peaking | 6170 Hz  | 3.62 | 6.4 dB  |
| Peaking | 15146 Hz | 5.03 | -3.3 dB |
| Peaking | 18 Hz    | 2.47 | 0.7 dB  |
| Peaking | 847 Hz   | 1.84 | 0.9 dB  |
| Peaking | 1454 Hz  | 2.05 | -1.4 dB |
| Peaking | 1956 Hz  | 2.04 | 1.0 dB  |
| Peaking | 2633 Hz  | 4.38 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.9 dB  |
| Peaking | 125 Hz   | 1.41 | 1.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -5.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Etymotic%20Research%20ER4SR/Etymotic%20Research%20ER4SR.png)