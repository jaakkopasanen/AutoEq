# Empire Ears Legend X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.1; 23 -13.1; 25 -13.1; 28 -13.0; 31 -13.0; 34 -12.9; 37 -12.8; 41 -12.7; 45 -12.6; 49 -12.5; 54 -12.3; 60 -12.2; 66 -12.1; 72 -12.0; 79 -12.0; 87 -11.9; 96 -11.9; 106 -11.8; 116 -11.7; 128 -11.5; 141 -11.3; 155 -11.0; 170 -10.7; 187 -10.3; 206 -9.9; 227 -9.4; 249 -9.0; 274 -8.5; 302 -8.0; 332 -7.5; 365 -7.0; 402 -6.6; 442 -6.1; 486 -5.7; 535 -5.3; 588 -4.9; 647 -4.4; 712 -3.9; 783 -3.2; 861 -3.0; 947 -3.3; 1042 -4.1; 1146 -5.2; 1261 -6.4; 1387 -7.2; 1526 -7.7; 1678 -7.8; 1846 -7.7; 2031 -7.4; 2234 -6.8; 2457 -5.9; 2703 -4.9; 2973 -4.0; 3270 -3.0; 3597 -1.8; 3957 -1.5; 4353 -2.5; 4788 -0.5; 5267 -0.8; 5793 -3.1; 6373 -2.6; 7010 -4.7; 7711 -8.0; 8482 -8.7; 9330 -6.7; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -8.0; 15026 -10.8; 16529 -11.3; 18182 -11.4; 20000 -9.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Empire Ears Legend X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Empire Ears Legend X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.24 | -6.7 dB |
| Peaking | 146 Hz   | 0.82 | -2.9 dB |
| Peaking | 789 Hz   | 2.19 | 3.7 dB  |
| Peaking | 4657 Hz  | 1.71 | 5.9 dB  |
| Peaking | 17641 Hz | 0.73 | -5.7 dB |
| Peaking | 1752 Hz  | 2.34 | -2.3 dB |
| Peaking | 3364 Hz  | 4.43 | 1.7 dB  |
| Peaking | 6534 Hz  | 6.49 | 2.2 dB  |
| Peaking | 8076 Hz  | 4.31 | -3.5 dB |
| Peaking | 12082 Hz | 2.91 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.1 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -5.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Empire%20Ears%20Legend%20X/Empire%20Ears%20Legend%20X.png)