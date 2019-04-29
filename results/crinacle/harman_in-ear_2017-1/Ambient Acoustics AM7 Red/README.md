# Ambient Acoustics AM7 Red
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.5; 23 -8.9; 25 -9.2; 28 -9.6; 31 -10.0; 34 -10.2; 37 -10.4; 41 -10.5; 45 -10.7; 49 -10.8; 54 -11.0; 60 -11.2; 66 -11.4; 72 -11.6; 79 -11.8; 87 -12.0; 96 -12.2; 106 -12.4; 116 -12.6; 128 -12.6; 141 -12.7; 155 -12.6; 170 -12.5; 187 -12.4; 206 -12.2; 227 -11.9; 249 -11.6; 274 -11.2; 302 -10.7; 332 -10.1; 365 -9.5; 402 -9.0; 442 -8.4; 486 -7.7; 535 -7.0; 588 -6.3; 647 -5.6; 712 -4.9; 783 -4.1; 861 -3.6; 947 -3.3; 1042 -3.4; 1146 -3.9; 1261 -4.4; 1387 -5.0; 1526 -5.7; 1678 -7.2; 1846 -10.2; 2031 -11.3; 2234 -7.9; 2457 -4.3; 2703 -2.6; 2973 -3.4; 3270 -6.2; 3597 -2.1; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -1.9; 6373 -3.2; 7010 -6.5; 7711 -7.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.6; 15026 -15.1; 16529 -25.3; 18182 -32.7; 20000 -28.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ambient Acoustics AM7 Red GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ambient Acoustics AM7 Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 67 Hz    | 0.29 | -3.7 dB  |
| Peaking | 246 Hz   | 0.43 | -4.5 dB  |
| Peaking | 1958 Hz  | 1.95 | -11.1 dB |
| Peaking | 5181 Hz  | 0.12 | 8.4 dB   |
| Peaking | 18558 Hz | 0.63 | -32.5 dB |
| Peaking | 2648 Hz  | 5.51 | 1.6 dB   |
| Peaking | 3298 Hz  | 5.91 | -6.0 dB  |
| Peaking | 3937 Hz  | 1.7  | 2.2 dB   |
| Peaking | 7470 Hz  | 3.72 | -4.1 dB  |
| Peaking | 13278 Hz | 3.37 | 6.4 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -20.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Ambient%20Acoustics%20AM7%20Red/Ambient%20Acoustics%20AM7%20Red.png)