# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.0; 23 -12.2; 25 -12.4; 28 -12.6; 31 -12.7; 34 -12.7; 37 -12.7; 41 -12.6; 45 -12.6; 49 -12.6; 54 -12.7; 60 -12.9; 66 -13.1; 72 -13.3; 79 -13.6; 87 -13.8; 96 -14.1; 106 -14.3; 116 -14.4; 128 -14.5; 141 -14.5; 155 -14.5; 170 -14.3; 187 -14.0; 206 -13.7; 227 -13.1; 249 -12.5; 274 -13.0; 302 -12.2; 332 -11.4; 365 -10.6; 402 -9.9; 442 -9.2; 486 -8.4; 535 -7.6; 588 -6.8; 647 -5.9; 712 -5.1; 783 -4.3; 861 -3.6; 947 -3.2; 1042 -3.0; 1146 -2.9; 1261 -2.6; 1387 -2.2; 1526 -1.8; 1678 -1.5; 1846 -1.3; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.5; 5793 -4.1; 6373 -8.3; 7010 -10.7; 7711 -9.8; 8482 -7.9; 9330 -9.2; 10263 -10.9; 11289 -10.1; 12418 -11.9; 13660 -17.4; 15026 -22.2; 16529 -23.5; 18182 -19.0; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.35 | -5.1 dB  |
| Peaking | 166 Hz   | 0.42 | -7.6 dB  |
| Peaking | 3294 Hz  | 0.26 | 7.2 dB   |
| Peaking | 6109 Hz  | 2.66 | -5.9 dB  |
| Peaking | 16223 Hz | 0.77 | -18.9 dB |
| Peaking | 824 Hz   | 3.46 | 0.9 dB   |
| Peaking | 5739 Hz  | 1.48 | 7.7 dB   |
| Peaking | 7021 Hz  | 3.69 | -6.3 dB  |
| Peaking | 7298 Hz  | 0.42 | -2.9 dB  |
| Peaking | 11999 Hz | 4.43 | 3.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 16000 Hz | 1.41 | -21.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)