# Audeze iSine 20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.4; 25 -2.5; 28 -2.6; 31 -2.7; 34 -2.8; 37 -2.9; 41 -3.0; 45 -3.2; 49 -3.4; 54 -3.7; 60 -3.9; 66 -4.3; 72 -4.7; 79 -5.1; 87 -5.6; 96 -6.1; 106 -6.5; 116 -7.0; 128 -7.4; 141 -7.8; 155 -8.1; 170 -8.5; 187 -8.7; 206 -9.0; 227 -9.2; 249 -9.4; 274 -9.6; 302 -9.8; 332 -9.9; 365 -10.0; 402 -10.3; 442 -10.5; 486 -10.8; 535 -11.1; 588 -11.6; 647 -12.1; 712 -12.7; 783 -13.4; 861 -14.0; 947 -13.6; 1042 -13.0; 1146 -13.3; 1261 -13.7; 1387 -14.1; 1526 -13.2; 1678 -11.2; 1846 -8.1; 2031 -3.8; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.7; 10263 -9.1; 11289 -6.5; 12418 -6.5; 13660 -15.3; 15026 -23.6; 16529 -23.1; 18182 -18.5; 20000 -10.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine 20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.32 | 4.3 dB   |
| Peaking | 1083 Hz  | 0.31 | -24.5 dB |
| Peaking | 1586 Hz  | 1.95 | -9.7 dB  |
| Peaking | 1985 Hz  | 0.28 | 26.2 dB  |
| Peaking | 16161 Hz | 0.85 | -20.8 dB |
| Peaking | 822 Hz   | 7.86 | -0.9 dB  |
| Peaking | 5959 Hz  | 3.61 | 2.4 dB   |
| Peaking | 9634 Hz  | 1.58 | -6.7 dB  |
| Peaking | 12233 Hz | 1.57 | 9.3 dB   |
| Peaking | 14464 Hz | 3.36 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB   |
| Peaking | 62 Hz    | 1.41 | 2.1 dB   |
| Peaking | 125 Hz   | 1.41 | -0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -9.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -20.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audeze%20iSine%2020/Audeze%20iSine%2020.png)