# Mee Audio Planamic IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.6; 25 -11.7; 28 -11.9; 31 -12.1; 34 -12.2; 37 -12.3; 41 -12.4; 45 -12.5; 49 -12.6; 54 -12.8; 60 -12.9; 66 -13.1; 72 -13.3; 79 -13.5; 87 -13.7; 96 -13.9; 106 -14.0; 116 -14.0; 128 -13.9; 141 -14.0; 155 -13.9; 170 -13.7; 187 -13.4; 206 -13.2; 227 -13.3; 249 -13.0; 274 -12.4; 302 -11.9; 332 -11.2; 365 -10.4; 402 -9.7; 442 -9.4; 486 -9.0; 535 -8.4; 588 -7.9; 647 -7.4; 712 -6.9; 783 -6.5; 861 -6.2; 947 -6.3; 1042 -6.6; 1146 -7.1; 1261 -7.7; 1387 -8.2; 1526 -8.7; 1678 -9.1; 1846 -9.3; 2031 -9.7; 2234 -10.5; 2457 -11.9; 2703 -12.5; 2973 -12.8; 3270 -13.1; 3597 -13.9; 3957 -14.9; 4353 -11.8; 4788 -6.4; 5267 -2.0; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Planamic IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Planamic IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 37 Hz   | 0.3  | -5.3 dB  |
| Peaking | 133 Hz  | 0.76 | -4.4 dB  |
| Peaking | 271 Hz  | 1.3  | -3.4 dB  |
| Peaking | 3962 Hz | 1.05 | -12.3 dB |
| Peaking | 5572 Hz | 1.95 | 13.9 dB  |
| Peaking | 490 Hz  | 2.45 | -0.7 dB  |
| Peaking | 913 Hz  | 1.58 | 1.7 dB   |
| Peaking | 1552 Hz | 1.21 | -0.7 dB  |
| Peaking | 6621 Hz | 8.88 | 1.7 dB   |
| Peaking | 7662 Hz | 4.22 | -1.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.9 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -5.4 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | -5.0 dB |
| Peaking | 8000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Mee%20Audio%20Planamic%20IEM/Mee%20Audio%20Planamic%20IEM.png)