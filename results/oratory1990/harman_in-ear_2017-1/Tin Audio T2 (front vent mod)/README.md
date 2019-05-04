# Tin Audio T2 (front vent mod)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.5; 25 -14.4; 28 -14.3; 31 -14.2; 34 -14.0; 37 -13.9; 41 -13.7; 45 -13.6; 49 -13.5; 54 -13.3; 60 -13.2; 66 -13.1; 72 -13.0; 79 -12.9; 87 -12.8; 96 -12.7; 106 -12.6; 116 -12.5; 128 -12.3; 141 -12.1; 155 -11.8; 170 -11.4; 187 -11.0; 206 -10.5; 227 -10.7; 249 -10.3; 274 -9.8; 302 -9.3; 332 -8.8; 365 -8.3; 402 -8.0; 442 -7.6; 486 -7.2; 535 -6.8; 588 -6.5; 647 -6.1; 712 -5.8; 783 -5.4; 861 -5.3; 947 -5.6; 1042 -5.2; 1146 -5.1; 1261 -4.8; 1387 -4.2; 1526 -3.5; 1678 -2.8; 1846 -2.1; 2031 -1.4; 2234 -1.0; 2457 -1.2; 2703 -1.8; 2973 -2.0; 3270 -1.3; 3597 -0.9; 3957 -1.2; 4353 -2.2; 4788 -4.0; 5267 -4.8; 5793 -2.2; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -6.0; 11289 -8.0; 12418 -8.4; 13660 -12.7; 15026 -21.6; 16529 -23.4; 18182 -19.7; 20000 -24.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Tin Audio T2 (front vent mod) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Tin Audio T2 (front vent mod) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.47 | -6.9 dB  |
| Peaking | 99 Hz    | 0.28 | -6.0 dB  |
| Peaking | 6722 Hz  | 0.27 | 14.2 dB  |
| Peaking | 13373 Hz | 0.98 | 12.1 dB  |
| Peaking | 15254 Hz | 0.39 | -32.8 dB |
| Peaking | 1177 Hz  | 1.63 | -2.1 dB  |
| Peaking | 2685 Hz  | 0.26 | 1.1 dB   |
| Peaking | 5125 Hz  | 4.45 | -4.0 dB  |
| Peaking | 6328 Hz  | 5.17 | 3.4 dB   |
| Peaking | 7542 Hz  | 3.66 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.8 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 16000 Hz | 1.41 | -21.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Tin%20Audio%20T2%20(front%20vent%20mod)/Tin%20Audio%20T2%20(front%20vent%20mod).png)