# Etymotic ER-4 (47 Ohm cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.4; 28 -1.9; 31 -2.3; 34 -2.7; 37 -2.9; 41 -3.2; 45 -3.4; 49 -3.6; 54 -3.8; 60 -4.0; 66 -4.1; 72 -4.1; 79 -4.3; 87 -4.5; 96 -4.5; 106 -4.5; 116 -4.5; 128 -4.4; 141 -4.7; 155 -4.8; 170 -4.8; 187 -4.8; 206 -4.8; 227 -4.7; 249 -4.4; 274 -4.5; 302 -4.4; 332 -4.5; 365 -4.9; 402 -5.1; 442 -5.1; 486 -5.1; 535 -5.1; 588 -4.8; 647 -4.8; 712 -5.1; 783 -5.1; 861 -5.1; 947 -5.4; 1042 -5.5; 1146 -5.8; 1261 -6.1; 1387 -6.5; 1526 -7.0; 1678 -7.8; 1846 -8.7; 2031 -9.6; 2234 -10.2; 2457 -10.4; 2703 -10.0; 2973 -8.9; 3270 -7.3; 3597 -5.8; 3957 -5.6; 4353 -6.8; 4788 -7.4; 5267 -6.4; 5793 -4.0; 6373 -1.1; 7010 -2.3; 7711 -4.6; 8482 -4.8; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Etymotic ER-4 (47 Ohm cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic ER-4 (47 Ohm cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.72 | 4.8 dB  |
| Peaking | 55 Hz   | 0.13 | 0.2 dB  |
| Peaking | 2323 Hz | 1.58 | -5.8 dB |
| Peaking | 4906 Hz | 5.65 | -2.4 dB |
| Peaking | 6527 Hz | 5.37 | 4.9 dB  |
| Peaking | 3560 Hz | 2.06 | -1.2 dB |
| Peaking | 3659 Hz | 4.63 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Etymotic%20ER-4%20(47%20Ohm%20cable)/Etymotic%20ER-4%20(47%20Ohm%20cable).png)