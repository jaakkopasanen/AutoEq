# Sennheiser IE800
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.5; 23 -11.5; 25 -11.5; 28 -11.5; 31 -11.4; 34 -11.4; 37 -11.4; 41 -11.4; 45 -11.3; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.4; 72 -11.4; 79 -11.4; 87 -11.4; 96 -11.4; 106 -11.3; 116 -11.2; 128 -11.2; 141 -11.3; 155 -11.4; 170 -11.2; 187 -11.0; 206 -10.6; 227 -10.3; 249 -9.8; 274 -9.5; 302 -9.0; 332 -8.6; 365 -8.2; 402 -7.8; 442 -7.5; 486 -7.2; 535 -6.9; 588 -6.7; 647 -6.5; 712 -6.3; 783 -6.1; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.7; 1261 -6.5; 1387 -6.0; 1526 -5.2; 1678 -4.2; 1846 -2.9; 2031 -1.3; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -1.8; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -10.7; 10263 -14.2; 11289 -13.6; 12418 -15.0; 13660 -23.2; 15026 -30.8; 16529 -30.5; 18182 -26.9; 20000 -26.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser IE800 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.2  | -4.9 dB  |
| Peaking | 178 Hz   | 0.94 | -2.5 dB  |
| Peaking | 4045 Hz  | 0.41 | 12.1 dB  |
| Peaking | 10646 Hz | 0.23 | 17.1 dB  |
| Peaking | 15601 Hz | 0.24 | -41.0 dB |
| Peaking | 1326 Hz  | 3.07 | -1.5 dB  |
| Peaking | 2169 Hz  | 4.54 | 2.1 dB   |
| Peaking | 6415 Hz  | 8.87 | 2.3 dB   |
| Peaking | 10068 Hz | 5.41 | -3.4 dB  |
| Peaking | 12133 Hz | 5.45 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.0 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 6.7 dB   |
| Peaking | 16000 Hz | 1.41 | -36.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20IE800/Sennheiser%20IE800.png)