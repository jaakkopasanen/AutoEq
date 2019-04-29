# Warbler Prelude sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.2; 34 -1.8; 37 -2.4; 41 -3.0; 45 -3.7; 49 -4.4; 54 -5.0; 60 -5.5; 66 -6.1; 72 -6.7; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.9; 116 -9.5; 128 -9.9; 141 -10.3; 155 -10.5; 170 -10.7; 187 -11.0; 206 -11.2; 227 -11.2; 249 -11.1; 274 -11.1; 302 -11.2; 332 -11.1; 365 -10.9; 402 -10.6; 442 -10.4; 486 -10.2; 535 -9.9; 588 -9.5; 647 -9.0; 712 -8.5; 783 -7.9; 861 -7.3; 947 -7.0; 1042 -7.0; 1146 -7.4; 1261 -7.8; 1387 -7.8; 1526 -7.3; 1678 -6.5; 1846 -5.6; 2031 -4.9; 2234 -4.6; 2457 -4.7; 2703 -5.3; 2973 -6.3; 3270 -6.4; 3597 -4.7; 3957 -1.9; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Warbler Prelude sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Warbler Prelude sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.61 | 6.4 dB  |
| Peaking | 233 Hz  | 0.41 | -5.0 dB |
| Peaking | 2234 Hz | 3.33 | 1.9 dB  |
| Peaking | 3215 Hz | 4.53 | -2.4 dB |
| Peaking | 4926 Hz | 1.63 | 7.0 dB  |
| Peaking | 939 Hz  | 3.84 | 1.0 dB  |
| Peaking | 1361 Hz | 4.16 | -1.1 dB |
| Peaking | 5188 Hz | 4.29 | -2.6 dB |
| Peaking | 6250 Hz | 1.78 | 4.3 dB  |
| Peaking | 7543 Hz | 1.76 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.5 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Warbler%20Prelude%20sample%202/Warbler%20Prelude%20sample%202.png)