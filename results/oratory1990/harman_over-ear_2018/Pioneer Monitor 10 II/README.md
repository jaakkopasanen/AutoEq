# Pioneer Monitor 10 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.0; 60 -1.6; 66 -2.2; 72 -2.7; 79 -3.3; 87 -3.8; 96 -4.2; 106 -5.0; 116 -6.1; 128 -7.5; 141 -8.6; 155 -9.7; 170 -10.8; 187 -11.6; 206 -12.4; 227 -12.9; 249 -13.1; 274 -13.6; 302 -14.2; 332 -14.0; 365 -13.7; 402 -13.2; 442 -12.6; 486 -11.9; 535 -11.0; 588 -9.9; 647 -8.8; 712 -7.8; 783 -7.3; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.3; 1387 -6.2; 1526 -6.4; 1678 -5.8; 1846 -3.2; 2031 -0.9; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.3; 15026 -15.1; 16529 -16.3; 18182 -15.0; 20000 -16.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.36 | 6.7 dB   |
| Peaking | 278 Hz   | 0.69 | -8.7 dB  |
| Peaking | 2282 Hz  | 2.87 | 3.7 dB   |
| Peaking | 4452 Hz  | 0.72 | 6.7 dB   |
| Peaking | 18123 Hz | 0.54 | -10.4 dB |
| Peaking | 846 Hz   | 3.2  | 1.3 dB   |
| Peaking | 1578 Hz  | 6.63 | -1.7 dB  |
| Peaking | 7963 Hz  | 5.37 | -2.4 dB  |
| Peaking | 12567 Hz | 2.52 | 3.5 dB   |
| Peaking | 15238 Hz | 2.84 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.5 dB   |
| Peaking | 125 Hz   | 1.41 | -0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -7.7 dB  |
| Peaking | 500 Hz   | 1.41 | -4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -11.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)