# Ultimate Ears Reference Monitors
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.8; 23 -3.1; 25 -3.4; 28 -3.7; 31 -4.0; 34 -4.3; 37 -4.5; 41 -4.7; 45 -4.9; 49 -5.1; 54 -5.4; 60 -5.8; 66 -6.1; 72 -6.5; 79 -6.9; 87 -7.4; 96 -7.9; 106 -8.4; 116 -8.8; 128 -9.2; 141 -9.5; 155 -9.9; 170 -10.2; 187 -10.4; 206 -10.5; 227 -10.6; 249 -10.7; 274 -10.8; 302 -10.7; 332 -10.6; 365 -10.4; 402 -10.4; 442 -10.3; 486 -10.1; 535 -9.9; 588 -9.6; 647 -9.2; 712 -8.7; 783 -8.1; 861 -7.7; 947 -7.4; 1042 -7.4; 1146 -7.8; 1261 -8.1; 1387 -8.1; 1526 -7.8; 1678 -7.4; 1846 -7.0; 2031 -6.0; 2234 -4.4; 2457 -2.6; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.8; 3957 -1.2; 4353 -1.5; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -12.1; 10263 -13.8; 11289 -7.0; 12418 -6.5; 13660 -10.7; 15026 -16.0; 16529 -8.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultimate Ears Reference Monitors GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultimate Ears Reference Monitors ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 315 Hz   | 0.48 | -4.4 dB  |
| Peaking | 3028 Hz  | 2.35 | 5.7 dB   |
| Peaking | 5429 Hz  | 1.55 | 6.1 dB   |
| Peaking | 9878 Hz  | 5.07 | -9.4 dB  |
| Peaking | 14895 Hz | 3.64 | -10.8 dB |
| Peaking | 22 Hz    | 1.2  | 3.6 dB   |
| Peaking | 48 Hz    | 1.97 | 1.3 dB   |
| Peaking | 918 Hz   | 2.91 | 0.9 dB   |
| Peaking | 1471 Hz  | 2.35 | -1.5 dB  |
| Peaking | 17441 Hz | 4.91 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.9 dB |
| Peaking | 1000 Hz  | 1.41 | -1.1 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -6.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ultimate%20Ears%20Reference%20Monitors/Ultimate%20Ears%20Reference%20Monitors.png)