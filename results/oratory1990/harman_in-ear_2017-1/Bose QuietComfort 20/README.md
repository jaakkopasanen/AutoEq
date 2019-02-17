# Bose QuietComfort 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -7.2; 25 -8.1; 28 -9.0; 31 -9.5; 34 -9.6; 37 -9.7; 41 -9.6; 45 -9.5; 49 -9.3; 54 -9.2; 60 -9.2; 66 -9.3; 72 -9.6; 79 -9.9; 87 -10.4; 96 -10.8; 106 -11.0; 116 -11.0; 128 -10.9; 141 -10.6; 155 -10.3; 170 -10.1; 187 -10.0; 206 -10.1; 227 -10.1; 249 -10.1; 274 -10.1; 302 -10.0; 332 -9.8; 365 -9.8; 402 -9.9; 442 -9.9; 486 -9.7; 535 -8.8; 588 -7.4; 647 -6.4; 712 -5.8; 783 -5.0; 861 -4.3; 947 -4.5; 1042 -5.5; 1146 -6.6; 1261 -7.4; 1387 -7.9; 1526 -10.2; 1678 -12.2; 1846 -12.3; 2031 -10.6; 2234 -8.8; 2457 -8.0; 2703 -7.2; 2973 -6.8; 3270 -6.8; 3597 -7.6; 3957 -9.0; 4353 -9.1; 4788 -6.7; 5267 -2.8; 5793 -0.5; 6373 -1.0; 7010 -6.6; 7711 -9.2; 8482 -6.3; 9330 -5.7; 10263 -7.1; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -11.8; 16529 -16.1; 18182 -15.5; 20000 -13.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 1.36 | -3.4 dB  |
| Peaking | 126 Hz   | 0.53 | -5.6 dB  |
| Peaking | 401 Hz   | 1.75 | -3.4 dB  |
| Peaking | 1819 Hz  | 2.26 | -7.4 dB  |
| Peaking | 17995 Hz | 0.96 | -12.5 dB |
| Peaking | 885 Hz   | 4.01 | 2.4 dB   |
| Peaking | 4268 Hz  | 2.88 | -5.6 dB  |
| Peaking | 6009 Hz  | 2.32 | 7.6 dB   |
| Peaking | 7427 Hz  | 4.46 | -6.8 dB  |
| Peaking | 13061 Hz | 3.94 | 3.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -3.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Bose%20QuietComfort%2020/Bose%20QuietComfort%2020.png)