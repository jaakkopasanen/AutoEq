# BGVP DM6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.6; 25 -4.1; 28 -4.8; 31 -5.2; 34 -5.6; 37 -5.9; 41 -6.4; 45 -6.8; 49 -7.2; 54 -7.5; 60 -7.9; 66 -8.3; 72 -8.7; 79 -9.1; 87 -9.5; 96 -9.9; 106 -10.4; 116 -10.7; 128 -11.0; 141 -11.2; 155 -11.3; 170 -11.4; 187 -11.4; 206 -11.4; 227 -11.3; 249 -11.0; 274 -10.8; 302 -10.5; 332 -10.2; 365 -9.8; 402 -9.3; 442 -8.9; 486 -8.4; 535 -7.9; 588 -7.3; 647 -6.7; 712 -5.9; 783 -5.2; 861 -4.6; 947 -4.2; 1042 -4.2; 1146 -4.6; 1261 -5.0; 1387 -5.0; 1526 -4.6; 1678 -3.9; 1846 -3.0; 2031 -2.0; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -2.5; 4353 -5.1; 4788 -3.9; 5267 -3.4; 5793 -7.1; 6373 -11.8; 7010 -12.0; 7711 -11.6; 8482 -7.1; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -13.4; 16529 -17.0; 18182 -12.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`BGVP DM6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `BGVP DM6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.86 | 4.5 dB   |
| Peaking | 182 Hz   | 0.49 | -5.2 dB  |
| Peaking | 5213 Hz  | 0.32 | 8.2 dB   |
| Peaking | 6945 Hz  | 1.61 | -13.5 dB |
| Peaking | 16529 Hz | 1.42 | -12.9 dB |
| Peaking | 953 Hz   | 1.38 | 4.0 dB   |
| Peaking | 1402 Hz  | 0.68 | -4.4 dB  |
| Peaking | 2376 Hz  | 1.05 | 3.2 dB   |
| Peaking | 4395 Hz  | 6.95 | -3.3 dB  |
| Peaking | 5293 Hz  | 8.53 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.6 dB |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/BGVP%20DM6/BGVP%20DM6.png)