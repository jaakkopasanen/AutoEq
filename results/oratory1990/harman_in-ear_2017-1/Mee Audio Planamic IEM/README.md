# Mee Audio Planamic IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.5; 25 -10.6; 28 -10.8; 31 -10.9; 34 -11.0; 37 -11.1; 41 -11.2; 45 -11.4; 49 -11.5; 54 -11.6; 60 -11.8; 66 -12.0; 72 -12.2; 79 -12.4; 87 -12.6; 96 -12.8; 106 -12.8; 116 -12.8; 128 -12.8; 141 -12.9; 155 -12.8; 170 -12.6; 187 -12.2; 206 -12.0; 227 -12.1; 249 -11.8; 274 -11.3; 302 -10.7; 332 -9.9; 365 -9.0; 402 -8.3; 442 -7.9; 486 -7.5; 535 -6.9; 588 -6.3; 647 -5.8; 712 -5.3; 783 -4.9; 861 -4.6; 947 -4.8; 1042 -5.2; 1146 -5.5; 1261 -5.9; 1387 -6.1; 1526 -6.3; 1678 -6.7; 1846 -6.8; 2031 -6.9; 2234 -7.1; 2457 -7.9; 2703 -8.1; 2973 -8.2; 3270 -8.6; 3597 -9.6; 3957 -11.0; 4353 -8.4; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.2; 15026 -19.7; 16529 -19.1; 18182 -13.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Planamic IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Planamic IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.37 | -5.3 dB  |
| Peaking | 193 Hz   | 0.99 | -3.9 dB  |
| Peaking | 4106 Hz  | 1.88 | -11.7 dB |
| Peaking | 5112 Hz  | 1.47 | 12.4 dB  |
| Peaking | 16061 Hz | 1.58 | -15.3 dB |
| Peaking | 18 Hz    | 1.98 | -0.9 dB  |
| Peaking | 844 Hz   | 1.97 | 2.4 dB   |
| Peaking | 7898 Hz  | 5.26 | -2.0 dB  |
| Peaking | 12678 Hz | 2.62 | 4.3 dB   |
| Peaking | 14414 Hz | 4.15 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.1 dB  |
| Peaking | 62 Hz    | 1.41 | -4.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.7 dB  |
| Peaking | 500 Hz   | 1.41 | 0.2 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 16000 Hz | 1.41 | -14.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Mee%20Audio%20Planamic%20IEM/Mee%20Audio%20Planamic%20IEM.png)