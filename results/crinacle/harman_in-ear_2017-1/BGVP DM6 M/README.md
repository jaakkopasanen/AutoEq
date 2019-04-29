# BGVP DM6 M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.8; 25 -5.4; 28 -6.1; 31 -6.6; 34 -7.1; 37 -7.5; 41 -7.9; 45 -8.4; 49 -8.8; 54 -9.2; 60 -9.6; 66 -10.0; 72 -10.4; 79 -10.9; 87 -11.3; 96 -11.8; 106 -12.2; 116 -12.6; 128 -12.9; 141 -13.1; 155 -13.2; 170 -13.3; 187 -13.4; 206 -13.4; 227 -13.2; 249 -13.0; 274 -12.8; 302 -12.4; 332 -12.0; 365 -11.5; 402 -11.0; 442 -10.5; 486 -10.0; 535 -9.4; 588 -8.8; 647 -8.1; 712 -7.4; 783 -6.6; 861 -6.0; 947 -5.7; 1042 -5.7; 1146 -6.0; 1261 -6.2; 1387 -6.0; 1526 -5.5; 1678 -4.7; 1846 -3.6; 2031 -2.4; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -2.0; 4788 -1.0; 5267 -0.5; 5793 -1.1; 6373 -3.9; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -15.8; 15026 -28.6; 16529 -31.2; 18182 -25.4; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 98 Hz    | 0.85 | -2.2 dB  |
| Peaking | 229 Hz   | 0.5  | -6.2 dB  |
| Peaking | 4908 Hz  | 0.46 | 12.4 dB  |
| Peaking | 12309 Hz | 1.46 | 16.6 dB  |
| Peaking | 15746 Hz | 0.53 | -33.0 dB |
| Peaking | 20 Hz    | 2.35 | 2.9 dB   |
| Peaking | 914 Hz   | 2.28 | 1.5 dB   |
| Peaking | 1440 Hz  | 1.38 | -2.1 dB  |
| Peaking | 2345 Hz  | 2.35 | 2.1 dB   |
| Peaking | 4321 Hz  | 9.56 | -1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -2.7 dB  |
| Peaking | 125 Hz   | 1.41 | -5.3 dB  |
| Peaking | 250 Hz   | 1.41 | -5.9 dB  |
| Peaking | 500 Hz   | 1.41 | -2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 16000 Hz | 1.41 | -28.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/BGVP%20DM6%20M/BGVP%20DM6%20M.png)