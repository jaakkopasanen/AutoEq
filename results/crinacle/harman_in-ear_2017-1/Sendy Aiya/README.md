# Sendy Aiya
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.5; 23 -15.6; 25 -15.6; 28 -15.7; 31 -15.7; 34 -15.6; 37 -15.5; 41 -15.5; 45 -15.4; 49 -15.2; 54 -15.1; 60 -14.9; 66 -14.8; 72 -14.7; 79 -14.6; 87 -14.5; 96 -14.4; 106 -14.2; 116 -14.1; 128 -13.8; 141 -13.6; 155 -13.2; 170 -12.8; 187 -12.4; 206 -11.9; 227 -11.3; 249 -10.8; 274 -10.2; 302 -9.5; 332 -8.7; 365 -8.0; 402 -7.4; 442 -6.7; 486 -6.1; 535 -5.4; 588 -4.8; 647 -4.1; 712 -3.5; 783 -3.0; 861 -2.8; 947 -3.0; 1042 -3.4; 1146 -4.0; 1261 -4.4; 1387 -4.5; 1526 -4.3; 1678 -4.2; 1846 -4.3; 2031 -4.5; 2234 -4.9; 2457 -5.7; 2703 -6.3; 2973 -6.3; 3270 -6.6; 3597 -8.5; 3957 -9.7; 4353 -11.2; 4788 -5.8; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.3; 15026 -22.8; 16529 -24.4; 18182 -17.4; 20000 -11.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sendy Aiya GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sendy Aiya ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.09 | -9.0 dB  |
| Peaking | 743 Hz   | 0.8  | 3.7 dB   |
| Peaking | 4439 Hz  | 1.04 | -29.5 dB |
| Peaking | 5029 Hz  | 0.73 | 29.0 dB  |
| Peaking | 16339 Hz | 1.26 | -22.2 dB |
| Peaking | 1916 Hz  | 5.67 | 0.5 dB   |
| Peaking | 6363 Hz  | 4.37 | 2.0 dB   |
| Peaking | 7771 Hz  | 3.02 | -3.1 dB  |
| Peaking | 12917 Hz | 3.26 | 6.8 dB   |
| Peaking | 14551 Hz | 2.11 | -3.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.7 dB  |
| Peaking | 62 Hz    | 1.41 | -6.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -3.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | -2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 16000 Hz | 1.41 | -19.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sendy%20Aiya/Sendy%20Aiya.png)