# Pioneer Monitor 10 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -1.9; 31 -2.3; 34 -2.5; 37 -2.8; 41 -3.2; 45 -3.5; 49 -3.8; 54 -4.3; 60 -4.9; 66 -5.4; 72 -5.9; 79 -6.6; 87 -7.1; 96 -7.4; 106 -8.2; 116 -9.4; 128 -10.8; 141 -11.9; 155 -13.0; 170 -14.1; 187 -14.8; 206 -15.7; 227 -16.1; 249 -16.3; 274 -16.9; 302 -17.5; 332 -17.2; 365 -17.0; 402 -16.5; 442 -15.9; 486 -15.1; 535 -14.2; 588 -13.2; 647 -12.0; 712 -11.1; 783 -10.6; 861 -10.0; 947 -9.8; 1042 -9.7; 1146 -9.7; 1261 -9.5; 1387 -9.5; 1526 -9.6; 1678 -9.1; 1846 -6.5; 2031 -4.1; 2234 -0.9; 2457 -0.7; 2703 -0.7; 2973 -0.7; 3270 -0.7; 3597 -0.7; 3957 -0.7; 4353 -0.7; 4788 -0.7; 5267 -0.7; 5793 -0.8; 6373 -1.3; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -7.9; 13660 -13.5; 15026 -18.4; 16529 -19.5; 18182 -18.3; 20000 -19.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer Monitor 10 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer Monitor 10 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.11 | 5.9 dB   |
| Peaking | 299 Hz   | 0.4  | -13.1 dB |
| Peaking | 1503 Hz  | 1.79 | -7.0 dB  |
| Peaking | 3103 Hz  | 0.28 | 8.6 dB   |
| Peaking | 17915 Hz | 0.42 | -14.0 dB |
| Peaking | 2296 Hz  | 8.46 | 1.9 dB   |
| Peaking | 7930 Hz  | 4.78 | -2.9 dB  |
| Peaking | 11944 Hz | 3.01 | 4.0 dB   |
| Peaking | 14851 Hz | 2.91 | -3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | 1.8 dB   |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -10.0 dB |
| Peaking | 500 Hz   | 1.41 | -6.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -16.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Pioneer%20Monitor%2010%20II/Pioneer%20Monitor%2010%20II.png)