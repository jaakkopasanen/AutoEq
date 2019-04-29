# Audeze iSine 10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.1; 23 -2.2; 25 -2.3; 28 -2.4; 31 -2.5; 34 -2.6; 37 -2.6; 41 -2.8; 45 -3.0; 49 -3.2; 54 -3.4; 60 -3.7; 66 -4.0; 72 -4.4; 79 -4.8; 87 -5.3; 96 -5.7; 106 -6.2; 116 -6.7; 128 -7.1; 141 -7.6; 155 -7.9; 170 -8.1; 187 -8.5; 206 -8.7; 227 -8.9; 249 -9.1; 274 -9.3; 302 -9.5; 332 -9.5; 365 -9.7; 402 -10.0; 442 -10.2; 486 -10.5; 535 -10.9; 588 -11.1; 647 -11.5; 712 -12.1; 783 -12.8; 861 -12.9; 947 -13.2; 1042 -13.1; 1146 -13.0; 1261 -13.2; 1387 -13.0; 1526 -10.6; 1678 -9.8; 1846 -8.7; 2031 -5.3; 2234 -1.8; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.4; 7010 -5.6; 7711 -6.2; 8482 -7.2; 9330 -10.3; 10263 -10.5; 11289 -6.6; 12418 -6.5; 13660 -14.9; 15026 -23.9; 16529 -25.2; 18182 -21.8; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze iSine 10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine 10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.54 | 4.5 dB   |
| Peaking | 1445 Hz  | 0.42 | -20.3 dB |
| Peaking | 2564 Hz  | 0.44 | 20.7 dB  |
| Peaking | 15380 Hz | 3.21 | -9.5 dB  |
| Peaking | 17569 Hz | 0.73 | -17.1 dB |
| Peaking | 2330 Hz  | 8.99 | 1.9 dB   |
| Peaking | 5531 Hz  | 2.01 | 4.7 dB   |
| Peaking | 9067 Hz  | 0.48 | -3.6 dB  |
| Peaking | 9814 Hz  | 6.24 | -3.2 dB  |
| Peaking | 12178 Hz | 2.77 | 7.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB   |
| Peaking | 62 Hz    | 1.41 | 2.3 dB   |
| Peaking | 125 Hz   | 1.41 | -0.6 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -8.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -22.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audeze%20iSine%2010/Audeze%20iSine%2010.png)