# Eartech Quad
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.8; 28 -6.3; 31 -6.7; 34 -7.0; 37 -7.3; 41 -7.7; 45 -8.0; 49 -8.3; 54 -8.7; 60 -9.1; 66 -9.6; 72 -10.0; 79 -10.5; 87 -11.1; 96 -11.6; 106 -12.1; 116 -12.4; 128 -12.8; 141 -13.1; 155 -13.4; 170 -13.5; 187 -13.6; 206 -13.5; 227 -13.5; 249 -13.3; 274 -13.1; 302 -12.8; 332 -12.3; 365 -11.8; 402 -11.4; 442 -10.9; 486 -10.3; 535 -9.7; 588 -9.0; 647 -8.3; 712 -7.5; 783 -6.6; 861 -5.9; 947 -5.4; 1042 -5.2; 1146 -5.3; 1261 -5.3; 1387 -5.0; 1526 -4.3; 1678 -3.6; 1846 -2.8; 2031 -1.6; 2234 -0.6; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -2.3; 5793 -4.0; 6373 -3.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.9; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -12.6; 15026 -21.9; 16529 -19.9; 18182 -11.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Eartech Quad GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Eartech Quad ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 1.53 | 1.7 dB   |
| Peaking | 123 Hz   | 0.63 | -4.3 dB  |
| Peaking | 283 Hz   | 0.66 | -5.0 dB  |
| Peaking | 3220 Hz  | 0.61 | 6.7 dB   |
| Peaking | 15802 Hz | 1.89 | -17.8 dB |
| Peaking | 900 Hz   | 5.32 | 1.0 dB   |
| Peaking | 4750 Hz  | 7.93 | 1.3 dB   |
| Peaking | 8990 Hz  | 2    | -1.7 dB  |
| Peaking | 12717 Hz | 2.27 | 5.2 dB   |
| Peaking | 14304 Hz | 4.31 | -6.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.7 dB   |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -6.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -15.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Eartech%20Quad/Eartech%20Quad.png)