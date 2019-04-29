# Sennheiser Momentum In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.7; 23 -10.0; 25 -10.3; 28 -10.7; 31 -11.0; 34 -11.2; 37 -11.4; 41 -11.6; 45 -11.8; 49 -11.9; 54 -12.1; 60 -12.4; 66 -12.6; 72 -12.8; 79 -13.0; 87 -13.2; 96 -13.4; 106 -13.6; 116 -13.7; 128 -13.7; 141 -13.7; 155 -13.6; 170 -13.4; 187 -13.1; 206 -12.8; 227 -12.4; 249 -12.0; 274 -11.5; 302 -10.9; 332 -10.3; 365 -9.6; 402 -9.1; 442 -8.5; 486 -7.9; 535 -7.3; 588 -6.7; 647 -6.1; 712 -5.4; 783 -4.8; 861 -4.3; 947 -4.1; 1042 -4.3; 1146 -4.7; 1261 -4.9; 1387 -5.0; 1526 -4.6; 1678 -4.0; 1846 -3.2; 2031 -2.3; 2234 -1.2; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.9; 5793 -3.1; 6373 -7.6; 7010 -11.9; 7711 -11.4; 8482 -7.3; 9330 -6.5; 10263 -6.6; 11289 -6.9; 12418 -10.5; 13660 -19.4; 15026 -25.0; 16529 -24.8; 18182 -20.6; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 62 Hz    | 0.33 | -5.2 dB  |
| Peaking | 187 Hz   | 0.71 | -4.1 dB  |
| Peaking | 7178 Hz  | 2.54 | -15.2 dB |
| Peaking | 7929 Hz  | 0.36 | 17.0 dB  |
| Peaking | 15608 Hz | 0.66 | -28.5 dB |
| Peaking | 912 Hz   | 1.29 | 4.5 dB   |
| Peaking | 1143 Hz  | 0.72 | -3.5 dB  |
| Peaking | 2378 Hz  | 2.25 | 1.9 dB   |
| Peaking | 11851 Hz | 5.31 | 3.1 dB   |
| Peaking | 13942 Hz | 5.43 | -3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -4.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -22.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)